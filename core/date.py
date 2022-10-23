import datetime as dt

from core.util import Success


class Date:
    beg_time = dt.date(2022, 10, 23)

    def __init__(self, obj) -> None:
        self.dtobj = None
        match obj:
            case str():
                self.dtobj = self.parseStr(obj)
            case dt.date():
                self.dtobj = obj

    def parse_wa(self, s):
        dt1 = dt.datetime.strptime(s, '%w%d')
        weeknum = dt1.isocalendar()[1]
        weekday = dt.date.weekday()
        td = dt.timedelta(days=weeknum * 7 + weekday)
        return Date.beg_time + td

    def parseStr(self, s):
        # 'Jan, Mon', 'Jan, 1'
        strptime = dt.datetime.strptime
        a = Success(s) \
            .bind(lambda s: strptime(s, '%b,%a')) \
            .bind(lambda s: strptime(s, '%b,%d')) \
            .bind(self.parsewa) \
            .get()


def genRange(beg: Date, end: Date, step: int):
    pass


def genSeq(beg: Date, step: int, count: int):
    pass
