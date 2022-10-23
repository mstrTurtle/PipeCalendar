import junoirTodo as jT
import calendar as C
import gui as G

if __name__ == '__main__':
    calList = list(map(C.toCalendar, [jT.juniorTodo]))
    c = C.Calendar(C.mergeCalendar(calList))

    G.QtWrapper.setCal(c)
    G.loop()

