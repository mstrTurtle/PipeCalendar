# Generated from MyGrammer.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MyGrammerParser import MyGrammerParser
else:
    from MyGrammerParser import MyGrammerParser

# This class defines a complete generic visitor for a parse tree produced by MyGrammerParser.

class MyGrammerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MyGrammerParser#Calendar.
    def visitCalendar(self, ctx:MyGrammerParser.CalendarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#MetaInfoExist.
    def visitMetaInfoExist(self, ctx:MyGrammerParser.MetaInfoExistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#MetaInfoNoneExist.
    def visitMetaInfoNoneExist(self, ctx:MyGrammerParser.MetaInfoNoneExistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#MetaTermsAppend.
    def visitMetaTermsAppend(self, ctx:MyGrammerParser.MetaTermsAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#MetaTermsNullInit.
    def visitMetaTermsNullInit(self, ctx:MyGrammerParser.MetaTermsNullInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#TestIt.
    def visitTestIt(self, ctx:MyGrammerParser.TestItContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#rval.
    def visitRval(self, ctx:MyGrammerParser.RvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#VarLit.
    def visitVarLit(self, ctx:MyGrammerParser.VarLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#StrLit.
    def visitStrLit(self, ctx:MyGrammerParser.StrLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#IntLit.
    def visitIntLit(self, ctx:MyGrammerParser.IntLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#AtsAppend.
    def visitAtsAppend(self, ctx:MyGrammerParser.AtsAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#AtsNullInit.
    def visitAtsNullInit(self, ctx:MyGrammerParser.AtsNullInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#at.
    def visitAt(self, ctx:MyGrammerParser.AtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#TagSpaceAppend.
    def visitTagSpaceAppend(self, ctx:MyGrammerParser.TagSpaceAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#TagSpaceInit.
    def visitTagSpaceInit(self, ctx:MyGrammerParser.TagSpaceInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#TermsAppend.
    def visitTermsAppend(self, ctx:MyGrammerParser.TermsAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#TermsInit.
    def visitTermsInit(self, ctx:MyGrammerParser.TermsInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#term.
    def visitTerm(self, ctx:MyGrammerParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#KeyValueTerm.
    def visitKeyValueTerm(self, ctx:MyGrammerParser.KeyValueTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#ArrangeTerm.
    def visitArrangeTerm(self, ctx:MyGrammerParser.ArrangeTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#kvTermKey.
    def visitKvTermKey(self, ctx:MyGrammerParser.KvTermKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#kvTermVal.
    def visitKvTermVal(self, ctx:MyGrammerParser.KvTermValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#MomentSeqAppend.
    def visitMomentSeqAppend(self, ctx:MyGrammerParser.MomentSeqAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#MomentSeqInit.
    def visitMomentSeqInit(self, ctx:MyGrammerParser.MomentSeqInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#momentSubSeq.
    def visitMomentSubSeq(self, ctx:MyGrammerParser.MomentSubSeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DateSeqAppend.
    def visitDateSeqAppend(self, ctx:MyGrammerParser.DateSeqAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DateSeqInit.
    def visitDateSeqInit(self, ctx:MyGrammerParser.DateSeqInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DateSubSeqFromTo.
    def visitDateSubSeqFromTo(self, ctx:MyGrammerParser.DateSubSeqFromToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DateSubSeqBegLen.
    def visitDateSubSeqBegLen(self, ctx:MyGrammerParser.DateSubSeqBegLenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DateSubSeqBegDup.
    def visitDateSubSeqBegDup(self, ctx:MyGrammerParser.DateSubSeqBegDupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DateSubSeqSingle.
    def visitDateSubSeqSingle(self, ctx:MyGrammerParser.DateSubSeqSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#IntervalOptionExist.
    def visitIntervalOptionExist(self, ctx:MyGrammerParser.IntervalOptionExistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#IntervalOptionNotExist.
    def visitIntervalOptionNotExist(self, ctx:MyGrammerParser.IntervalOptionNotExistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DateTermWnWd.
    def visitDateTermWnWd(self, ctx:MyGrammerParser.DateTermWnWdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DateTermMmDd.
    def visitDateTermMmDd(self, ctx:MyGrammerParser.DateTermMmDdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DateTermYyMmDd.
    def visitDateTermYyMmDd(self, ctx:MyGrammerParser.DateTermYyMmDdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#TimeSeqAppend.
    def visitTimeSeqAppend(self, ctx:MyGrammerParser.TimeSeqAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#TimeSeqInit.
    def visitTimeSeqInit(self, ctx:MyGrammerParser.TimeSeqInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#TimeTermFromTo.
    def visitTimeTermFromTo(self, ctx:MyGrammerParser.TimeTermFromToContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#TimeTermSingle.
    def visitTimeTermSingle(self, ctx:MyGrammerParser.TimeTermSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#TimeMomentPostfix.
    def visitTimeMomentPostfix(self, ctx:MyGrammerParser.TimeMomentPostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DisplayTermsAppend.
    def visitDisplayTermsAppend(self, ctx:MyGrammerParser.DisplayTermsAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#DisplayTermsNullInit.
    def visitDisplayTermsNullInit(self, ctx:MyGrammerParser.DisplayTermsNullInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#displayTerm.
    def visitDisplayTerm(self, ctx:MyGrammerParser.DisplayTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#PunchTermExist.
    def visitPunchTermExist(self, ctx:MyGrammerParser.PunchTermExistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#PunchTermNotExist.
    def visitPunchTermNotExist(self, ctx:MyGrammerParser.PunchTermNotExistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#PunchTypeVar.
    def visitPunchTypeVar(self, ctx:MyGrammerParser.PunchTypeVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#PunchTypeList.
    def visitPunchTypeList(self, ctx:MyGrammerParser.PunchTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#ListForward.
    def visitListForward(self, ctx:MyGrammerParser.ListForwardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#ListAppend.
    def visitListAppend(self, ctx:MyGrammerParser.ListAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#ListInit.
    def visitListInit(self, ctx:MyGrammerParser.ListInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#IntervalTermOne.
    def visitIntervalTermOne(self, ctx:MyGrammerParser.IntervalTermOneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MyGrammerParser#IntervalTermTwo.
    def visitIntervalTermTwo(self, ctx:MyGrammerParser.IntervalTermTwoContext):
        return self.visitChildren(ctx)



del MyGrammerParser