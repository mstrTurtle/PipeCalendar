import datetime as dt


class CourseRange:
    courseTime = [None,
     dt.time(9,50),
     dt.time(10,50),
     dt.time(11, 30),
     dt.time(12, 15),
     dt.time(14,00),
     dt.time(14, 40),
     dt.time(15, 30),
     dt.time(16, 30),
     dt.time(17, 20),
     dt.time(19, 50),
     ]

    def __init__(self, obj) -> None:
        self.beg = None
        self.end = None
        match obj:
            case str():
                [beg, end] = obj.strip('-')
                self.beg = beg
                self.end = end

    def toTimePitch(self):
        return (self.courseTime[self.beg], self.courseTime[self.end])