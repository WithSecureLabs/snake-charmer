# Snake Charmer

```
           _____
          / . . \
          \     /       Snake Charmer
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

```

The regression suite for Snake.

## Running

Snake Charmer is simple to run.

```bash
# 1. Install python requirements.
pip install -r requirements.txt

# 2. Run Snake Charmer
./snake-charmer.sh
```

## Running Locally

Snake Charmer can be run on a Snake instance that is not installed, perfect for development...

```bash
./snake-charmer.sh -l <PATH_TO_SNAKE>
```

## Updating a Test

Updating a test is as simple as pointing snake to the test file with the `-u` flag.

```bash
./snake-charmer.sh -u <PATH_TO_TEST>
```
