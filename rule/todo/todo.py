import abc
from dataclasses import dataclass

from core import calendar as c
from core.rule import rule
from core.date import Date


@dataclass
class Item:
    seq: list[Date]


class Todo(rule):
    def toCalendar(self) -> c.Calendar:
        pass

    def __init__(self) -> None:
        super().__init__()
