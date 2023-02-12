# Deploying a Poetry-based Pyramid app to Heroku

First, read [main branch `README.md`](https://github.com/zupo/tutorial/blob/main/README.md).

This branch shows my exploration of deploying a Poetry-based Pyramid project to Heroku.

Steps:
* `poetry export -f requirements.txt --output requirements.txt --without-hashes`
* `echo "-e ." >> requirements.txt`
* `python --version | tr '[:upper:]' '[:lower:]' | tr ' ' '-' > runtime.txt `
* `git push heroku exploration/heroku_requirements.txt:main`

## Caveats

* This tutorial does not do anything for setting up a Postgres database. It's only concerned with deploying a Pyramid app so that Heroku can find and run all necessary Python files.

* We have to use `--without-hashes` for now, because pip does not support mixing `-e .` into a list of dependencies with hashes in `requirements.txt` file. More info on https://github.com/pypa/pip/issues/4995.
