from n.Todo import Todo as Todo, Item as Item
import n.Range as R
import n.Date as D
import n.tagUtil as T
from datetime import date as Date


class JuniorTodo(Todo):
    def __init__(self) -> None:
        super().__init__()
        
    def genRule(self): # impl interface
        健康 = T('健康')
        早饭 = T('成功吃早饭')

        a = Item(R(Date(2022, 9, 1)), '自制/成功早睡', type=bool, hint='是否早睡')
        b = Item(R(D('Apr7')), '自强不息', type=bool)
        c = Item(R(D('W6, MON')))

        return [a,
                b,
                c,
                Item(R('Apr1'), 健康/早饭, type=str, hint='吃了啥')
                ]

