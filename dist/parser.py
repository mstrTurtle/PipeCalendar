import sys
from antlr4 import *
from dist.MyGrammerLexer import MyGrammerLexer
from dist.MyGrammerParser import MyGrammerParser
from dist.MyGrammerVisitor import MyGrammerVisitor
from core.types.asciimodel import MetaInfo, VarLit, StrLit, IntLit, KeyValueTerm, IntervalTerm, \
    DateTermMmDd, \
    DateTerm, DateTermYyMmDd, DateTermWnWd, DateSubSeqSingle, DateSubSeqFromTo, DateSubSeqBegDup, DateSubSeqBegLen, \
    DateSubSeq, TimeMoment, TimeMomentPostfix, TimeTermSingle, TimeTermFromTo, MomentSubSeq, PunchTerm, ArrangeTerm, At, \
    Calendar, Context


def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[0]


class MyVisitor(MyGrammerVisitor):

    def visitKeyValueTerm(self, ctx: MyGrammerParser.KeyValueTermContext):
        k = self.visit(ctx.key)
        v = self.visit(ctx.val)
        # print(k, v)
        pair = KeyValueTerm(k, v)
        return pair

    def visitNumberExpr(self, ctx) -> list[(VarLit | StrLit | IntLit)]:
        value = ctx.getText()
        return int(value)

    def visitCalendar(self, ctx: MyGrammerParser.CalendarContext):
        metainfo = self.visit(ctx.metainfo())
        ats = self.visit(ctx.ats())
        return Calendar(metainfo, ats)

    def visitMetaTermsNullInit(self, ctx: MyGrammerParser.MetaTermsNullInitContext):
        return []

    def visitMetaTermsAppend(self, ctx: MyGrammerParser.MetaTermsAppendContext):
        k = self.visit(ctx.kvTerm())
        l = self.visit(ctx.metaTerms())
        return [k] + l

    def visitMetaInfoExist(self, ctx: MyGrammerParser.MetaInfoExistContext):
        return self.visit(ctx.metaTerms())

    def visitMetaInfoNoneExist(self, ctx: MyGrammerParser.MetaInfoNoneExistContext):
        return []

    def visitTermsAppend(self, ctx: MyGrammerParser.TermsAppendContext):
        k = self.visit(ctx.term())
        l = self.visit(ctx.terms())
        return [k] + l

    def visitTermsInit(self, ctx: MyGrammerParser.TermsInitContext):
        k = self.visit(ctx.term())
        return [k]

    def visitAtsNullInit(self, ctx: MyGrammerParser.AtsNullInitContext):
        return []

    def visitAtsAppend(self, ctx: MyGrammerParser.AtsAppendContext):
        v = self.visit(ctx.at())
        l = self.visit(ctx.ats())
        return [v] + l

    def visitAt(self, ctx: MyGrammerParser.AtContext):
        tagspace = self.visit(ctx.tagspace())
        terms = self.visit(ctx.terms())
        return At(tagspace, terms)

    def visitTagSpaceAppend(self, ctx: MyGrammerParser.TagSpaceAppendContext):
        v = self.visit(ctx.var())
        l = self.visit(ctx.tagspace())
        return [v] + l

    def visitTagSpaceInit(self, ctx: MyGrammerParser.TagSpaceInitContext):
        v = self.visit(ctx.var())
        return [v]

    def visitListAppend(self, ctx: MyGrammerParser.ListAppendContext) -> list[(VarLit | StrLit | IntLit)]:
        v: list[(VarLit | StrLit | IntLit)] = self.visit(ctx.rval())  # 这是小树左边的叶子(而且一定是叶子)
        l: list[(VarLit | StrLit | IntLit)] = self.visit(ctx.listInternal())  # 这是小树右边的树(可能是叶子可能是树)
        return [v] + l

    def visitListInit(self, ctx: MyGrammerParser.ListInitContext):
        v = self.visit(ctx.rval())
        return [v]

    def visitDateSeqAppend(self, ctx: MyGrammerParser.DateSeqAppendContext):
        v = self.visit(ctx.dateSubSeq())
        l = self.visit(ctx.dateSeq())
        return [v] + l

    def visitDateSeqInit(self, ctx: MyGrammerParser.DateSeqInitContext):
        v = self.visit(ctx.dateSubSeq())
        return [v]

    def visitDateTermYyMmDd(self, ctx: MyGrammerParser.DateTermYyMmDdContext):
        year = self.visit(ctx.year)
        mmdd = self.visit(ctx.mmdd)
        return DateTermYyMmDd(year, mmdd)

    def visitDateTermMmDd(self, ctx: MyGrammerParser.DateTermMmDdContext):
        mmdd = self.visit(ctx.mmdd)
        return DateTermMmDd(mmdd)

    def visitDateTermWnWd(self, ctx: MyGrammerParser.DateTermWnWdContext):
        weekx = self.visit(ctx.weekx)
        weekdayabbr = self.visit(ctx.weekdayabbr)
        return DateTermWnWd(weekx, weekdayabbr)

    def visitIntervalOptionExist(self, ctx: MyGrammerParser.IntervalOptionExistContext):
        term = self.visit(ctx.intervalTerm())
        return term

    def visitIntervalOptionNotExist(self, ctx: MyGrammerParser.IntervalOptionNotExistContext):
        return None

    def visitDateSubSeqSingle(self, ctx: MyGrammerParser.DateSubSeqSingleContext):
        dateTerm = self.visit(ctx.dateTerm())
        return DateSubSeqSingle(dateTerm)

    def visitDateSubSeqBegDup(self, ctx: MyGrammerParser.DateSubSeqBegDupContext):
        beg = self.visit(ctx.beg())
        cnt = self.visit(ctx.cnt())
        opt = self.visit(ctx.opt())
        return DateSubSeqBegDup(beg, cnt, opt)

    def visitDateSubSeqBegLen(self, ctx: MyGrammerParser.DateSubSeqBegLenContext):
        beg = self.visit(ctx.beg)
        len = self.visit(ctx.len)
        opt = self.visit(ctx.opt)
        return DateSubSeqBegLen(beg, len, opt)

    def visitDateSubSeqFromTo(self, ctx: MyGrammerParser.DateSubSeqFromToContext):
        beg = self.visit(ctx.beg)
        end = self.visit(ctx.end)
        opt = self.visit(ctx.opt)
        return DateSubSeqFromTo(beg, end, opt)

    def visitTimeMomentPostfix(self, ctx: MyGrammerParser.TimeMomentPostfixContext):
        hour = self.visit(ctx.int_())
        postfix = self.visit(ctx.postfix)
        return TimeMomentPostfix(hour, postfix)

    def visitIntervalTermOne(self, ctx: MyGrammerParser.IntervalTermOneContext):
        fstVal: IntLit = self.visit(ctx.fstVal())
        fstUnit: VarLit = self.visit(ctx.fstUnit())
        return IntervalTerm(fstVal, fstUnit, None, None)

    def visitIntervalTermTwo(self, ctx: MyGrammerParser.IntervalTermTwoContext):
        fstVal: IntLit = self.visit(ctx.fstVal())
        fstUnit: VarLit = self.visit(ctx.fstUnit())
        sndVal: IntLit = self.visit(ctx.sndVal())
        sndUnit: VarLit = self.visit(ctx.sndUnit())
        return IntervalTerm(fstVal, fstUnit, sndVal, sndUnit)

    def visitTimeTermSingle(self, ctx: MyGrammerParser.TimeTermSingleContext):
        timeMoment = self.visit(ctx.timeMoment())
        return TimeTermSingle(timeMoment)

    def visitTimeTermFromTo(self, ctx: MyGrammerParser.TimeTermFromToContext):
        beg = self.visit(ctx.beg())
        end = self.visit(ctx.end())
        return TimeTermFromTo(beg, end)

    def visitTimeSeqAppend(self, ctx: MyGrammerParser.TimeSeqAppendContext):
        v = self.visit(ctx.timeTerm())
        l = self.visit(ctx.timeSeq())
        return [v] + l

    def visitTimeSeqInit(self, ctx: MyGrammerParser.TimeSeqInitContext):
        v = self.visit(ctx.timeTerm())
        return [v]

    def visitMomentSeqAppend(self, ctx: MyGrammerParser.MomentSeqAppendContext):
        v = self.visit(ctx.momentSubSeq())
        l = self.visit(ctx.momentSeq())
        return [v] + l

    def visitMomentSeqInit(self, ctx: MyGrammerParser.MomentSeqInitContext):
        v = self.visit(ctx.momentSubSeq())
        return [v]

    def visitMomentSubSeq(self, ctx: MyGrammerParser.MomentSubSeqContext):
        dateSeq = self.visit(ctx.dateSeq())
        timeSeq = self.visit(ctx.timeSeq())
        return MomentSubSeq(dateSeq, timeSeq)

    def visitDisplayTermsNullInit(self, ctx: MyGrammerParser.DisplayTermsNullInitContext):
        return []

    def visitDisplayTermsAppend(self, ctx: MyGrammerParser.DisplayTermsAppendContext):
        v = self.visit(ctx.displayTerm())
        l = self.visit(ctx.displayTerms())
        return [v] + l

    def visitPunchTermExist(self, ctx: MyGrammerParser.PunchTermExistContext):
        punchType = self.visit(ctx.punchType())
        rval = self.visit(ctx.rval())
        return PunchTerm(punchType, rval)

    def visitPunchTermNotExist(self, ctx: MyGrammerParser.PunchTermNotExistContext):
        return None

    # 其实这没必要
    def visitPunchTypeList(self, ctx: MyGrammerParser.PunchTypeListContext):
        return self.visit(ctx.list_())

    def visitPunchTypeVar(self, ctx: MyGrammerParser.PunchTypeVarContext):
        return self.visit(ctx.var())

    # 这是有必要的. 不然就会返回'[', 就None了.
    def visitListForward(self, ctx: MyGrammerParser.ListForwardContext):
        return self.visit(ctx.listInternal())

    def visitArrangeTerm(self, ctx: MyGrammerParser.ArrangeTermContext):
        momentSeq = self.visit(ctx.momentSeq())
        displayTerms = self.visit(ctx.displayTerms())
        punchTerms = self.visit(ctx.punchTerm())
        return ArrangeTerm(momentSeq, displayTerms, punchTerms)

    def visitVarLit(self, ctx: MyGrammerParser.VarLitContext):
        return VarLit(val=ctx.getText())

    def visitStrLit(self, ctx: MyGrammerParser.StrLitContext):
        return StrLit(val=ctx.getText())

    def visitIntLit(self, ctx: MyGrammerParser.IntLitContext):
        return IntLit(val=int(ctx.getText()))

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        operation = {
            '+': lambda: l + r,
            '-': lambda: l - r,
            '*': lambda: l * r,
            '/': lambda: l / r,
        }
        return operation.get(op, lambda: None)()

    def visitByeExpr(self, ctx):
        print(f"goodbye {get_username()}")
        sys.exit(0)

    def visitHelloExpr(self, ctx):
        return f"{ctx.getText()} {get_username()}"


# 测试用的main函数. 从input.txt弄进来, 并打印一些东西.
if __name__ == "__main__":
    input_stream = FileStream("input.txt", encoding='utf-8')
    # with open('input.txt', encoding='utf-8') as f:
    #     str = f.read()
    # input_stream = InputStream(str)
    # lexer
    lexer = MyGrammerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    # parser
    parser = MyGrammerParser(stream)
    tree = parser.calen()
    # evaluator
    visitor = MyVisitor()
    output: Calendar = visitor.visit(tree)
    print(output.toStr())
    cal = output.compute(Context())
    print(cal)


# 暴露外界使用的类. 或许是否改个好听的名字?
class MyAntlrParser:

    # IDE提示我生成的, 实际上没有用, 仅作为linter的辅助作用.
    def __init__(self):
        self.calendar = None
        self.visitor = None
        self.tree = None
        self.parser = None
        self.stream = None
        self.lexer = None
        self.input_stream = None
        self.output = None

    # 传入字符串, 然后什么都得不到. 内部会生成一些结构.
    def loadByStr(self, theStr):
        if(self.output):
            raise Exception('exception: has been opened')
        self.input_stream = InputStream(theStr)
        # lexer
        self.lexer = MyGrammerLexer(input_stream)
        self.stream = CommonTokenStream(lexer)
        # parser
        self.parser = MyGrammerParser(stream)
        self.tree = parser.calen()
        # evaluator
        self.visitor = MyVisitor()
        self.output = visitor.visit(tree)

    # 经过compute, 得到一个calendar. 可以当做是parse的成果. 毕竟得到那堆结构体, 你也没什么用.
    # 而且这是惰性的, 而且是记忆化的.
    def getCalendar(self):
        if not self.calendar:
            self.calendar = self.output.compute(Context())
        return self.calendar

    # 反序列化内部的model为ascii model, 输出为内置的str.
    def deserModel(self):
        return self.output.toStr()

    # 这是parse后得到的结构体. 仅作为parser内部的结构, 还有debug使用. 作用十分有限(因为表示太tm复杂了, 宁愿处理calendar也不处理这个).
    def getRawOutput(self):
        return self.output
