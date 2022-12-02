# 这玩意儿相当于是一个ViewModel吧. 或者是GUI的state, store之类的.
from dataclasses import dataclass, field
from typing import TypeAlias

from core.types.commontypes import Date, Time


@dataclass
class Moment:
    date: Date
    time: Time


MomentSeq: TypeAlias = list[Moment]


@dataclass
class Event:
    name: str
    momentSeq: MomentSeq
