# pre-commits

## Description:

Just a repo to test out pre-commit hooks for python and Github Actions


## Setup

Setup a environment
```bash
conda create -n precommit python=3.10
```

Install packages:
```bash
pip install -r requirements.txt
```


## Pre-commits

When `git commit -m 'your commit message' ` is run, the checks take place, no commit is allowed until the checks have passed

## Pytest

Check if tests have passed by running `pytest` in your terminal.


## CI pipeline

The CI Pipeline and tests will run when a PR is created.





References:
- https://datatalks.club/blog/practical-guide-better-code.html
