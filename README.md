# Pyramid's "SQLAlchemy + URL dispatch" wiki tutorial based on Poetry

An example "tutorial" repo that follows https://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/wiki2/index.html but uses Poetry instead of pip/setuptools.


These are the commands used in the tutorial, but changed to use Poetry:

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
