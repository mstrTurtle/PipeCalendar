import abc
import calendar as c


class rule(abc.ABC):
    @abc.abstractmethod
    def toCalendar(self) -> c.Calendar:
        """
            将rule转换成Calendar
        """
