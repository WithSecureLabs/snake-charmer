#!/bin/bash

# TODO: Log properly

FILE=''
LOCAL=''
MONGO_PID=0
MONGO_PORT=6001
SNAKE_API='http://localhost:6000'
SNAKE_DIR='/tmp/snake'
SNAKE_PID=0
UPDATE=''

check_requirements() {
  # Snake Charmer requirements
  output=$(which pip3 2>&1)
  if [[ $? -ne 0 ]]; then
    echo "Snake Charmer requires 'pip3'"
    shutdown 1
  fi
  output=$(pip3 list --format columns | grep pymongo)
  if [[ $output != *"pymongo"* ]]; then
    echo "Snake Charmer requires 'pymongo'"
    shutdown 1
  fi
  output=$(pip3 list --format columns | grep pytest)
  if [[ $output != *"pytest"* ]]; then
    echo "Snake Charmer requires 'pytest'"
    shutdown 1
  fi
  output=$(pip3 list --format columns | grep pytest-regtest)
  if [[ $output != *"pytest-regtest"* ]]; then
    echo "Snake Charmer requires 'pytest-regtest'"
    shutdown 1
  fi
  output=$(pip3 list --format columns | grep requests)
  if [[ $output != *"requests"* ]]; then
    echo "Snake Charmer requires 'requests'"
    shutdown 1
  fi

  # Snake requirements
  output=$(which mongod 2>&1)
  if [[ $? -ne 0 ]]; then
    echo "Snake requires 'mongodb'"
    shutdown 1
  fi

  output=$(which redis-server 2>&1)
  if [[ $? -ne 0 ]]; then
    echo "Snake requires 'redis'"
    shutdown 1
  fi
}

configure_env() {
  export MONGO_PORT
  export SNAKE_API
}

print_banner() {
  echo '''
           _____
          / . . \
          \     /       Snake Charmer v1.0
          |\ _ /|       By Countercept
          | | | |
        __|_____|__
       |___________|
      /_ _ _ _ _ _ _\
     | _ _ _ _ _ _ _ |
      \             /
       \           /
        \         /
         \_______/

  '''
}

run_tests() {
  echo "Running regression tests... Done!"
  if [[ $UPDATE != '' ]]; then
    py.test --color=yes --regtest-reset $UPDATE
  elif [[ $FILE != '' ]]; then
    py.test --color=yes $FILE
  else
    py.test --color=yes
  fi
  if [[ $? -ne 0 ]]; then
    cat "${SNAKE_DIR}/log/celery.log"
    cat "${SNAKE_DIR}/log/snake.log"
    shutdown 1
  fi
}

shutdown() {
  if [[ $MONGO_PID -ne 0 ]]; then
      setsid kill -- $MONGO_PID
  fi
  if [[ $REDIS_PID -ne 0 ]]; then
      setsid kill -- $REDIS_PID
  fi
  if [[ $CELERY_PID -ne 0 ]]; then
      setsid kill -- $CELERY_PID
  fi
  if [[ $SNAKE_PID -ne 0 ]]; then
      setsid kill -- $SNAKE_PID
  fi
  exit $1
}

start_celery() {
  echo -n "Starting Celery..."
  if [[ $LOCAL != '' ]]; then
    dir=$(pwd)
    cd $LOCAL
    celery worker --app snake.worker --worker_config="$dir/snake.conf" &>${SNAKE_DIR}/log/celery.log &
    CELERY_PID=$!
    sleep 4
    if [[ $(ps | grep $CELERY_PID) == '' ]]; then
      echo "Could not start celery"
      CELERY_PID=0
      shutdown 1
    fi
    cd $dir
  else
    output=$(which snaked 2>&1)
    if [[ $? -ne 0 ]]; then
      echo "Could not find snake"
      shutdown 1
    fi
    celery worker --app snake.worker --worker_config="$dir/snake.conf" &>${SNAKE_DIR}/log/celery.log &
    CELERY_PID=$!
    sleep 4
    if [[ $(ps | grep $CELERY_PID) == '' ]]; then
      echo "Could not start celery"
      CELERY_PID=0
      shutdown 1
    fi
  fi
  echo " Done!"
}

start_mongodb() {
  # Never use the production mongodb
  echo -n "Starting mongodb..."
  if [[ -d '/tmp/snake/mongo' ]]; then
    rm -Rf '/tmp/snake/mongo'
  fi
  mkdir -p /tmp/snake/mongo
  mongod --dbpath /tmp/snake/mongo -port 6001 &>/dev/null &
  MONGO_PID=$!
  sleep 4
  if [[ $(ps | grep $MONGO_PID) == '' ]]; then
    echo "Could not start mongod"
    MONGO_PID=0
    shutdown 1
  fi
  echo " Done!"
}

start_redis() {
  # Never use the production mongodb
  echo -n "Starting redis..."
  redis-server --port 6002 &>/dev/null &
  REDIS_PID=$!
  sleep 4
  if [[ $(ps | grep $REDIS_PID) == '' ]]; then
    echo "Could not start redis"
    REDIS_PID=0
    shutdown 1
  fi
  echo " Done!"
}

start_snake() {
  echo -n "Starting Snake..."
  if [[ $LOCAL != '' ]]; then
    dir=$(pwd)
    cd $LOCAL
    python3 -m snake.snaked -d -c "$dir/snake.conf" &>${SNAKE_DIR}/log/snake.log &
    SNAKE_PID=$!
    sleep 30
    if [[ $(ps | grep $SNAKE_PID) == '' ]]; then
      echo "Could not start snake"
      cat "${SNAKE_DIR}/log/snake.log"
      SNAKE_PID=0
      shutdown 1
    fi
    cd $dir
  else
    output=$(which snaked 2>&1)
    if [[ $? -ne 0 ]]; then
      echo "Could not find snake"
      shutdown 1
    fi
    snaked -d -c "$dir/snake.conf" &>${SNAKE_DIR}/log/snake.log &
    SNAKE_PID=$!
    sleep 30
    if [[ $(ps | grep $SNAKE_PID) == '' ]]; then
      echo "Could not start snake"
      cat "${SNAKE_DIR}/log/snake.log"
      SNAKE_PID=0
      shutdown 1
    fi
  fi
  echo " Done!"
}


#
# Main
#

trap "shutdown" SIGINT SIGTERM

print_banner

# Parse arguments
while (( "$#" )); do
  case $1 in
      -f|--file) FILE=$2
        if [[ $2 == '' ]]; then
          echo "-l requires a test file to run"
          shutdown 1
        fi
        shift
      ;;
      -l|--local) LOCAL=$2
        if [[ $2 == '' ]]; then
          echo "-l requires a directory to snake"
          shutdown 1
        fi
        shift
      ;;
      -u|--update) UPDATE=$2
        if [[ $2 == '' ]]; then
          echo "-u requires a test file to update"
          shutdown 1
        fi
      ;;
      *) break
  esac
  shift
done

check_requirements
configure_env
mkdir -p $SNAKE_DIR
mkdir -p "${SNAKE_DIR}/cache"
mkdir -p "${SNAKE_DIR}/files"
mkdir -p "${SNAKE_DIR}/log"
start_mongodb
start_redis
start_celery
start_snake
sleep 5
run_tests
shutdown 0
