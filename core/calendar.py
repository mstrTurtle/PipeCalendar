from dataclasses import dataclass
from datetime import datetime


@dataclass
class TimeDescriptor:
    isWholeDay: int
    isTimePoint: int  # Set default value
    date: datetime
    timepoint: datetime
    timerange: tuple[datetime,datetime]


@dataclass
class Item:
    title: str
    detail: str
    tag: str
    descriptor: TimeDescriptor


@dataclass
class Calendar:
    items: list[Item]
