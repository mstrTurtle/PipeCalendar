import abc
import datetime
import functools
from collections import defaultdict
from copy import copy
from dataclasses import dataclass, field
from typing import TypeAlias

DisplayTerm: TypeAlias = str
monthNameMap = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10,
                    'nov': 11, 'dec': 12}

@dataclass
class IntLit:
    val: int


@dataclass
class StrLit:
    val: str


@dataclass
class VarLit:
    val: str


# 小间隔序列
class IntervalSubSeq(abc.ABC):
    pass

@dataclass
class PunchDescription:
    LISTMUTEX = 1
    LISTCOMBO = 2
    TEXT = 3

    type: int
    title: str

    @staticmethod
    def fromListMutex(list: list[str], title: str):
        return PunchDescription(PunchDescription.LISTMUTEX, title)

    @staticmethod
    def fromListCombo(list: list[str], title: str):
        return PunchDescription(PunchDescription.LISTCOMBO, title)

    @staticmethod
    def fromText(title: str):
        return PunchDescription(PunchDescription.LISTCOMBO, title)


@dataclass
class PunchContent:
    LISTMUTEX = 1
    LISTCOMBO = 2
    TEXT = 3

    type: int
    contentText: str | None
    contentChoiceIndexes: list[int] | None

    @staticmethod
    def fromListMutex(index: int):
        return PunchContent(PunchContent.LISTMUTEX, None, [index])

    @staticmethod
    def fromListCombo(indexes: list[int]):
        return PunchContent(PunchContent.LISTCOMBO, None, indexes)

    @staticmethod
    def fromText(text: str):
        return PunchContent(PunchContent.LISTCOMBO, text, None)

# 打卡项
@dataclass
class PunchTerm:
    punchType: (VarLit | list[(VarLit | StrLit | IntLit)])
    punchVal: (VarLit | StrLit | IntLit)

    def toStr(self):
        typeStr = None
        if self.punchType is VarLit:
            typeStr = self.punchType.val
        elif self.punchType is list:
            typeStr = '[' + ','.join(map(lambda lit: str(lit.val), self.punchType)) + ']'
        valStr = self.punchVal.val
        return f'>>{typeStr} {valStr}'
    def toPunchDescription(self,ctx):
        if self.punchType is VarLit:
            return PunchDescription.fromText(str(self.punchType.val))
        elif self.punchType is list:
            return PunchDescription.fromListCombo(list(map(lambda x: str(x.val),self.punchType)))

@dataclass
class Interval:
    month: int
    day: int

    def __mul__(self, count: int):
        self.month *= count
        self.day *= count
        return self


# 间隔项
@dataclass
class IntervalTerm:
    fstVal: IntLit
    fstUnit: VarLit
    sndVal: IntLit | None
    sndUnit: VarLit | None

    def toStr(self):
        if self.sndVal == None or self.sndUnit == None:
            return f'{self.fstVal.val} {self.fstUnit.val}'
        else:
            return f'{self.fstVal.val} {self.fstUnit.val} {self.sndVal.val} {self.sndUnit.val}'

    def toInterval(self, ctx) -> Interval:
        if self.sndVal is None:
            assert self.fstUnit.val == 'd'
            return Interval(month=0, day=self.fstVal.val)
        else:
            assert (self.fstUnit.val == 'm' and self.sndUnit.val == 'd')
            return Interval(month=self.fstVal.val, day=self.sndVal.val)


@dataclass
class Date:
    year: int
    month: int
    day: int

    @staticmethod
    def fromYyMmDd(yy, mm, dd):
        return Date(yy, mm, dd)

    @staticmethod
    def fromMmDd(mm, dd):
        return Date(datetime.datetime.today().year, mm, dd)

    @staticmethod
    def fromDd(dd):
        tod = datetime.datetime.today()
        return Date(tod.year, tod.month, dd)

    @staticmethod
    def fromToday():
        tod = datetime.datetime.today()
        return Date(tod.year, tod.month, tod.day)

    @staticmethod
    def fromMetaString(s1:str): # '2022Apr1', '22Apr01', 'Apr07', etc.
        s = copy(s1)
        s = s[1:-1]
        if(all(map(str.isdigit,s[0:4]))):
            year = int(s[0:4])
            month = monthNameMap[s[4:7].lower()]
            day = int(s[7:])
        elif(all(map(str.isdigit,s[0:2]))):
            year = int(s[0:2])
            month = monthNameMap[s[2:5].lower()]
            day = int(s[5:])
        else:
            raise Exception
        return Date(year,month,day)

    def fromtoby(self, that, interv: Interval) -> list:
        ret = []
        cur = datetime.date(self.year, self.month, self.day)
        end = datetime.date(that.year, that.month, that.day)
        step = datetime.timedelta(days=30 * interv.month + interv.day)
        while cur <= end:
            ret.append(Date(cur.year, cur.month, cur.day))
            cur += step
        return ret

    def __add__(self, interv: Interval):
        cur = datetime.date(self.year, self.month, self.day)
        step = datetime.timedelta(days=30 * interv.month + interv.day)
        cur += step
        return Date(cur.year, cur.month, cur.day)


class DateTerm(abc.ABC):
    @abc.abstractmethod
    def toStr(self):
        pass

    @abc.abstractmethod
    def toDate(self, ctx) -> Date:
        pass


def mmddToMonthDay(mmdd: VarLit) -> (int, int):

    month: int = monthNameMap[mmdd.val[0:3].lower()]
    day: int = int(mmdd.val[3:])
    return month, day


@dataclass
class DateTermYyMmDd(DateTerm):
    year: IntLit  # 2022
    mmdd: VarLit  # Apr4

    def toStr(self):
        return f'{self.year.val}{self.mmdd.val}'

    def toDate(self, ctx) -> Date:
        month, day = mmddToMonthDay(self.mmdd)
        return Date.fromYyMmDd(self.year.val, month, day)


@dataclass
class DateTermMmDd(DateTerm):
    mmdd: VarLit  # Apr4

    def toStr(self):
        return f'{self.mmdd.val}'

    def toDate(self, ctx) -> Date:
        month, day = mmddToMonthDay(self.mmdd)
        return Date.fromYyMmDd(ctx.year, month, day)


@dataclass
class DateTermWnWd(DateTerm):
    weeknum: VarLit  # W11
    weekday: VarLit  # TUE

    def toStr(self):
        return f'{self.weeknum.val}#{self.weekday.val}'

    def toDate(self, ctx) -> Date:
        WeekdayMap={'sun':0,'mon':1,'tue':2,'wed':3,'thu':4,'fri':5,'sat':6}
        print(ctx.begDate)
        begDate:Date = ctx.begDate
        date = datetime.date(begDate.year,begDate.month,begDate.day)
        while(date.weekday()!=0):
            date+=datetime.timedelta(days=1)
        delta = datetime.timedelta(days = int(self.weeknum.val[1:])*7+WeekdayMap[self.weekday.val.lower()])
        date = date+delta
        return Date(date.year,date.month,date.day)


# 小日期序列
class DateSubSeq(abc.ABC):
    @abc.abstractmethod
    def toStr(self):
        pass

    @abc.abstractmethod
    def toDateList(self, ctx) -> list[Date]:
        pass


@dataclass
class DateSubSeqFromTo(DateSubSeq):
    begDate: DateTerm
    endDate: DateTerm
    intervalTerm: IntervalTerm | None

    def toStr(self):
        ret = f'{self.begDate.toStr()}-{self.endDate.toStr()}'
        if self.intervalTerm:
            ret += f'%{self.intervalTerm.toStr()}'
        return ret

    def toDateList(self, ctx) -> list[Date]:
        if self.intervalTerm is None:
            return self.begDate.toDate(ctx).fromtoby(self.endDate.toDate(ctx), Interval(0, 1))
        else:
            return self.begDate.toDate(ctx).fromtoby(self.endDate.toDate(ctx), self.intervalTerm.toInterval(ctx))


@dataclass
class DateSubSeqBegLen(DateSubSeq):
    begDate: DateTerm
    len: IntervalTerm
    intervalTerm: IntervalTerm | None

    def toStr(self):
        return f'{self.begDate.toStr()}+{self.len.toStr()}%{self.intervalTerm.toStr()}'

    def toDateList(self, ctx) -> list[Date]:
        if self.intervalTerm is None:
            return self.begDate.toDate(ctx).fromtoby(self.begDate.toDate(ctx) + self.len.toInterval(ctx),
                                                     Interval(0, 1))
        else:
            return self.begDate.toDate(ctx).fromtoby(self.begDate.toDate(ctx) + self.len.toInterval(ctx),
                                                     self.intervalTerm.toInterval(ctx))


@dataclass
class DateSubSeqBegDup(DateSubSeq):
    begDate: DateTerm
    count: IntLit
    intervalTerm: IntervalTerm | None

    def toStr(self):
        return f'{self.begDate.toStr()}*{self.count.val}%{self.intervalTerm.toStr()}'

    def toDateList(self, ctx) -> list[Date]:
        if self.intervalTerm is None:
            return self.begDate.toDate(ctx).fromtoby(self.begDate.toDate(ctx) + Interval(0, self.count.val),
                                                     Interval(0, 1))
        else:
            return self.begDate.toDate(ctx).fromtoby(
                self.begDate.toDate(ctx) + self.intervalTerm.toInterval(ctx) * self.count.val,
                self.intervalTerm.toInterval(ctx))


@dataclass
class DateSubSeqSingle(DateSubSeq):
    date: DateTerm

    def toStr(self):
        return f'{self.date.toStr()}'

    def toDateList(self, ctx) -> list[Date]:
        return [self.date.toDate(ctx)]


@dataclass
class Time:
    WHOLEDAY = 1
    MOMENT = 2
    RANGE = 3
    COURSE = 4

    type: int
    hour: int | None
    min: int | None
    hourEnd: int | None
    minEnd: int | None
    session: int | None

    @staticmethod
    def fromCourse(session: int):
        return Time(Time.COURSE, None, None, None, None, session)

    @staticmethod
    def fromMoment(hour: int, min: int):
        return Time(Time.MOMENT, hour, min, None, None, None)

    @staticmethod
    def fromRange(hour: int, min: int, hourEnd: int, minEnd: int):
        return Time(Time.MOMENT, hour, min, hourEnd, minEnd, None)

    @staticmethod
    def fromTwoMoment(m1, m2):
        '''从两个Time(type=Time.MOMENT)中构造Time(type=TIME.RANGE)'''
        return Time(Time.RANGE, m1.hour, m1.min, m2.hour, m2.min, None)

    @staticmethod
    def fromWholeDay():
        return Time(Time.WHOLEDAY, None, None, None, None, None)


# 时刻. 虚基类
class TimeMoment(abc.ABC):
    @abc.abstractmethod
    def toStr(self):
        pass

    @abc.abstractmethod
    def toTime(self, ctx) -> Time:
        pass


@dataclass
class TimeMomentPostfix(TimeMoment):
    hour: IntLit
    postfix: StrLit

    def toStr(self):
        return f'{self.hour.val}{self.postfix.val}'

    def toTime(self, ctx) -> Time:
        if self.postfix.val == 'am':
            return Time.fromMoment(self.hour.val, 0)
        elif self.postfix.val == 'pm':
            return Time.fromMoment(self.hour.val + 12, 0)
        elif self.postfix.val == 'c':
            return Time.fromCourse(self.hour.val)
        else:
            raise Exception


# 时间项. 虚基类
class TimeTerm:
    @abc.abstractmethod
    def toStr(self):
        pass

    @abc.abstractmethod
    def toTime(self, ctx) -> Time:
        pass


@dataclass
class TimeTermSingle(TimeTerm):
    timeMoment: TimeMoment

    def toStr(self):
        return f'{self.timeMoment.toStr()}'

    def toTime(self, ctx) -> Time:
        return self.timeMoment.toTime(ctx)


@dataclass
class TimeTermFromTo(TimeTerm):
    beg: TimeMoment
    end: TimeMoment

    def toStr(self):
        return f'{self.beg.toStr()}-{self.end.toStr()}'

    def toTime(self, ctx) -> Time:
        return Time.fromTwoMoment(self.beg.toTime(ctx), self.end.toTime(ctx))


@dataclass
class MetaInfo:
    keys: list[str]
    vals: list[str | int]

    def toStr(self):
        pass




# 时间子项
@dataclass
class MomentSubSeq:
    dateSeq: list[DateSubSeq] = field(default_factory=list)
    timeSeq: list[TimeTerm] = field(default_factory=list)

    def toStr(self):
        dateSeqStr = '\n:'.join(map(lambda dss: dss.toStr(), self.dateSeq))
        timeSeqStr = '\n:'.join(map(lambda tss: tss.toStr(), self.timeSeq))
        return f'{dateSeqStr}\n!!\n{timeSeqStr}'

    def toTuple(self, ctx) -> (list[Date], list[Time]):
        #return list(map(lambda x: x.toDateList(ctx), self.dateSeq)), list(map(lambda x: x.toTime(ctx), self.timeSeq))
        dates = []
        for term in self.dateSeq:
            dates = [*dates, *term.toDateList(ctx)]
        times = []
        for term in self.timeSeq:
            times.append( term.toTime(ctx))
        return (dates,times)


# 作为虚基类
class Term(abc.ABC):
    @abc.abstractmethod
    def toStr(self):
        pass


@dataclass
class KeyValueTerm(Term):
    key: VarLit
    val: (VarLit | StrLit | IntLit)

    def toStr(self):
        return f'{self.key.val}->{self.val.val}'

    def toDictCompute(self, ctx): # 写Compute, 代表这玩意儿有副作用, 别反复执行. 这对应局部变量.
        ctx.localvars[self.key.val] = self.val.val
        return {self.key.val: self.val.val}

    def toGlobalDictCompute(self, ctx): # 写Compute, 代表这玩意儿有副作用, 别反复执行. 这对应MetaInfo里的
        ctx.globalvars[self.key.val] = self.val.val
        return {self.key.val: self.val.val}


@dataclass
class Arrange:
    dates: list[Date]
    times: list[Time]  # 至少要有一个WholeDay的项.
    displayStrs: list[str]  # 此时已经翻译(类似宏替换)为Str了, 不会再改变.
    punchInfo: PunchDescription


# 项
@dataclass
class ArrangeTerm(Term):
    """
    $
    W11#WED
    :W12#FRI
    :Apr2
    !!
    9am
    ::
    May3
    !!
    9am
    :2pm
    ,x,y
    >>[1,2,3] 1
    """
    momentSeq: list[MomentSubSeq] = field(default_factory=list)
    displayTerms: list[VarLit] = field(default_factory=list)
    punchTerm: PunchTerm = None

    def toStr(self):
        momentSeqStr = '\n::\n'.join(map(lambda mss: mss.toStr(), self.momentSeq)) + '\n'
        displayTermsStr = ''
        for varLit in self.displayTerms:
            displayTermsStr += ',' + varLit.val
        displayTermsStr += '\n'
        punchTermStr = ''
        if punchTermStr:
            punchTermStr = self.punchTerm.toStr() + '\n'
        return f'$\n{momentSeqStr}{displayTermsStr}{punchTermStr}'

    def toArrange(self, ctx) -> Arrange:
        datess:list[Date] = []
        timess:list[Time] = []
        for momentSubSeq in self.momentSeq:
            dates,times = momentSubSeq.toTuple(ctx)
            datess.append(dates)
            timess.append(times)
        def displayTermExpand(displayTerm:VarLit)->str:
            print(ctx)
            v = ctx.localvars.get(displayTerm.val)
            if v is None:
                v1 = ctx.globalvars.get(displayTerm.val)
                if v1 is None:
                    return displayTerm.val
                else:
                    return v1
            else:
                return v
        if self.punchTerm:
            return Arrange(datess,timess,list(map(displayTermExpand,self.displayTerms)),self.punchTerm.toPunchDescription(ctx))
        else:
            return Arrange(datess, timess, list(map(displayTermExpand, self.displayTerms)),None)


# 艾特
@dataclass
class At:
    tagSpace: list[VarLit]
    terms: list[ArrangeTerm|KeyValueTerm]

    def toStr(self):
        tagSpaceStr = '/'.join(map(lambda varLit: varLit.val, self.tagSpace))
        termsStr = '\n'.join(map(lambda t: t.toStr(), self.terms))
        return f'@{tagSpaceStr}\n{termsStr}'

    def compute(self, ctx):
        #print(self.terms)
        tags = list(map(lambda varLit:varLit.val, self.tagSpace))
        ctx.localvars = dict() # 清空本地变量
        _ = list(map(lambda kvTerm:kvTerm.toDictCompute(ctx), filter(lambda term:term.__class__== KeyValueTerm, self.terms)))
        arrangesComputed = list(map(lambda kvTerm: kvTerm.toArrange(ctx), filter(lambda term: term.__class__ == ArrangeTerm, self.terms)))
        ctx.calendarPutArranges(arrangesComputed)
        return (list(map(lambda x: x.val, self.tagSpace)), arrangesComputed)

# 日历
@dataclass
class Calendar:
    metaInfo: list[KeyValueTerm] = None
    ats: list[At] = field(default_factory=list)

    def toStr(self):
        metaInfoStrInner = '\n'.join(map(lambda t: t.toStr(), self.metaInfo))
        metaInfoStr = '---\n' + metaInfoStrInner + '\n---'
        atsStr = '\n\n'.join(map(lambda ats: ats.toStr(), self.ats))
        return f'{metaInfoStr}\n\n{atsStr}'

    def compute(self,ctx):
        _ = (list(map(lambda metaKv:metaKv.toGlobalDictCompute(ctx),self.metaInfo)))
        ctx.fillWithMetaInfoComputed()
        ret = []
        for at in self.ats:
            ret.append(at.compute(ctx))
        return ret

class Context:
    def __init__(self):
        self.globalvars:dict[str,str|int] = dict()
        self.localvars:dict[str,str|int] = dict()
        self.year:int = None
        self.begDate:Date = None

    def calendarPutArranges(self,arranges:list[Arrange]):
        print("here:")
        print(arranges)
        print("")

    def fillWithThisYear(self):
        self.year= datetime.datetime.today().year

    def fillWithMetaInfoComputed(self):
        if self.globalvars.get('year'):
            self.year = int(self.globalvars['year'])
        else:
            self.year = Date.fromToday().year
        self.begDate = Date.fromMetaString(self.globalvars['begDate'])
class AsciiState:
    d = defaultdict(dict)

    currentTagspace = ''

    def registerVar(self, pair: KeyValueTerm):
        self.d[self.currentTagspace][pair.key] = pair.val
