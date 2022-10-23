import datetime as dt

from core.util import Success


class Time:
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
            .bind(lambda s: strptime(s, '%H:%M')) \
            .bind(lambda s: strptime(s, '%H')) \
            .bind(lambda s: strptime(s, '%I%p:%M')) \
            .bind(lambda s: strptime(s, '%I%p')) \
            .get()