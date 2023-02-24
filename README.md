# SQLAlchemy-fsm exploration

First, read [main branch `README.md`](https://github.com/zupo/tutorial/blob/main/README.md).

This branch shows my exploration of [SQLAlchemy-fsm](https://pypi.org/project/sqlalchemy-fsm/) to a simple Finite-State-Machine as `state` field of SQLA models.

Steps:
* https://github.com/VRGhost/sqlalchemy-fsm#usage
* Run `alembic -c development.ini revision --autogenerate -m "fsm"` to add a new `state` column.
* Run `alembic -c development.ini upgrade head` to add the new column to DB.
* Run `pserve development.ini --reload` and go to `http://localhost:6543/`.
* On every view load `mymodel.state` is transitioned: `new` -> `in-progress` -> `done` -> back to `new`.


# References

* https://pypi.org/project/sqlalchemy-fsm/ (more active and better alternative but no OOTB support for SQLAlchemy)
* https://pypi.org/project/sqlalchemy-state-machine/ (similar but more basic, no side effects, no conditions)


# Caveats

In `sqlalchemy-fsm`, a transition method such as `post.publish()` does not do what is expected: to publish the blog post. But rather it tells you if `post`'s current state is the same as the target state for `publish()` transition. No idea why and who uses this. If you want to do the actual transition, you have to call `post.publish.set()`. This API is unfortunate.
