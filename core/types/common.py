from dataclasses import dataclass


# Date 和 Time 毕竟是ViewModel和AsciiModel的公有的结构.
# 稍后再在这一组结构上定义一些操作.
@dataclass
class Date:
    day: int
    month: int
    year: int


@dataclass
class Time:
    hour: int
    min: int
    sec: int
