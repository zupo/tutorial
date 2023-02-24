from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)
from sqlalchemy_fsm import FSMField, transition

from .meta import Base

from enum import StrEnum, auto


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)
    state = Column(FSMField, default='new', nullable=False)

    class states(StrEnum):
        new = auto()
        in_progress = auto()
        done = auto()

    @transition(source=states.new, target=states.in_progress)
    def start(self):
        self.value = 1


    @transition(source=states.in_progress, target=states.done)
    def finish(self):
        self.value = 2


    @transition(source=states.done, target=states.new)
    def reset(self):
        self.value = 3



Index('my_index', MyModel.name, unique=True, mysql_length=255)
