from __future__ import annotations


class Success:
    """
        这是一个Monad, 一路bind过去, 遇到成功的立即返回. 否则返回原来的value.
    """

    def __init__(self, value, successed=False):
        self.value = value
        self.successed = successed

    def get(self):
        return self.value

    def has_successed(self):
        return self.successed

    def __str__(self):
        return f'{self.value} {self.successed}'

    def bind(self, f) -> Success:
        if self.successed:
            return self
        try:
            x = f(self.get())
            return Success(x, True)
        except:
            return Success(self.value)  # 失败了, 把值丢进去让它继续试.


class InfixAdaptor:
    """
    >>> add = InfixAdaptor(lambda x,y:x+y)
    >>> 1 <<add>> 2
    3

    """

    def __init__(self, f):
        self.f = f

    def __rlshift__(self, lhs):
        self.lhs = lhs
        return self

    def __rshift__(self, rhs):
        return self.f(self.lhs, rhs)
