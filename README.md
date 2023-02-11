# Pyramid's "SQLAlchemy + URL dispatch" tutorial scaffold based on Poetry


An example "tutorial" repo that follows https://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/index.html but uses Poetry instead of pip/setuptools.

Using latest Pyramid 2 and SQLAlchemy 2.

These are the commands used in the tutorial, but changed to use [Poetry](https://python-poetry.org/):

```console
$ cd ~
$ git clone https://github.com/zupo/tutorial.git
$ cd tutorial
$ poetry install
$ poetry run alembic -c development.ini revision --autogenerate -m "init"
$ poetry run alembic -c development.ini upgrade head
$ poetry run initialize_tutorial_db development.ini
$ poetry run pytest -q
$ poetry run pserve development.ini --reload
```

## Nix support

If you want to skip the manual installation of prerequisites, this repo comes with [Nix](https://nixos.org/) support as well. Assuming you have [Nix](https://nixos.org/) & [direnv](https://direnv.net/) installed (but no Python, no Poetry, etc.), the commands above look like so:

```console
$ cd ~
$ git clone https://github.com/zupo/tutorial.git
$ cd tutorial
$ alembic -c development.ini revision --autogenerate -m "init"
$ alembic -c development.ini upgrade head
$ initialize_tutorial_db development.ini
$ pytest -q
$ pserve development.ini --reload
```
## Object history via SQLAlchemy-Continuum

Need to keep history of your objects so you can tell who changed what and when? See the [exploration/sqlalchemy-continuum](https://github.com/zupo/tutorial/tree/exploration/sqlalchemy-continuum) branch of this repo.

# References

* https://github.com/Pylons/pyramid-cookiecutter-starter/issues/69
* https://gist.github.com/mmerickel/33bc8edc633da132a8f92dbcb03ec1da
