
from dataclasses import dataclass, field
from typing import TypeAlias

DisplayTerm: TypeAlias = str


# 小间隔序列
class IntervalSubSeq:
    pass


# 打卡项
@dataclass
class PunchTerm:
    punchType: str = ''
    intervalSeq: list[IntervalSubSeq] = field(default_factory=list)


# 间隔项
class IntervalTerm:
    pass


# 小日期序列
class DateSubSeq:
    pass


# 日期项
class DateTerm:
    pass


# 时间项
class TimeTerm:
    pass


# 时间子项
@dataclass
class TimeSubTerm:
    dateSeq: list[DateSubSeq] = field(default_factory=list)
    timeSeq: list[TimeTerm] = field(default_factory=list)


# 项
@dataclass
class Term:
    timeSeq: list[TimeSubTerm] = field(default_factory=list)
    displayTerms: list[DisplayTerm] = field(default_factory=list)
    punchTerm: PunchTerm = None


# 时刻
class Moment:
    pass


# 艾特
@dataclass
class At:
    tagSpace: str = None
    terms: list[Term] = field(default_factory=list)


@dataclass
class MetaInfo:
    pass


# 日历
@dataclass
class Calendar:
    metaInfo: MetaInfo = None
    ats: list[At] = field(default_factory=list)
