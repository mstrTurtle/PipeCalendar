grammar MyGrammer;
//expr: left=expr op=('*'|'/') right=expr        # InfixExpr
//    | left=expr op=('+'|'-') right=expr        # InfixExpr
//    | atom=INT                                 # NumberExpr
//    | '(' expr ')'                             # ParenExpr
//    | atom=HELLO                               # HelloExpr
//    | atom=BYE                                 # ByeExpr
//    ;


calen:metainfo ats EOF#Calendar;

metainfo:'---' metaTerms'---' #MetaInfoExist
        |                               #MetaInfoNoneExist
        ;

metaTerms: kvTerm metaTerms #MetaTermsAppend
         |            #MetaTermsNullInit
         ;

lval
:var #TestIt;

rval:var
|str|int;

var:VARORLITERAL #VarLit;
str:STRLITERAL   #StrLit;
int:INT          #IntLit;

ats : at ats#AtsAppend
    |#AtsNullInit
    ;

at:'@' tagspace terms;

tagspace : var '/' tagspace #TagSpaceAppend
         | var #TagSpaceInit
         ;

terms:term terms #TermsAppend
     |term       #TermsInit
     ;

term: kvTerm|arrTerm;

kvTerm: key=kvTermKey '->' val=kvTermVal #KeyValueTerm;
arrTerm: '$' momentSeq displayTerms punchTerm #ArrangeTerm;

kvTermKey: lval;

kvTermVal: rval;

momentSeq:momentSubSeq'::'momentSeq #MomentSeqAppend
         |momentSubSeq #MomentSeqInit
         ;

momentSubSeq:dateSeq'!!'timeSeq;

dateSeq : dateSubSeq':'dateSeq #DateSeqAppend
        | dateSubSeq           #DateSeqInit
        ;

// TODO: 这个需要补充.
dateSubSeq : beg=dateTerm'-'end=dateTerm opt=intervalOption #DateSubSeqFromTo
           | beg=dateTerm'+'len=intervalTerm opt=intervalOption#DateSubSeqBegLen
           | beg=dateTerm'*'cnt=int opt=intervalOption#DateSubSeqBegDup
           | dateTerm#DateSubSeqSingle
           ;

intervalOption: '%'intervalTerm #IntervalOptionExist
                        | #IntervalOptionNotExist
                        ;

dateTerm: weekx=var '#' weekdayabbr=var #DateTermWnWd
        | mmdd=var #DateTermMmDd
        | year=int mmdd=var #DateTermYyMmDd
        ;

timeSeq :timeTerm':'timeSeq #TimeSeqAppend
        |timeTerm           #TimeSeqInit
        ;
timeTerm:beg=timeMoment '-' end=timeMoment #TimeTermFromTo
        | timeMoment #TimeTermSingle
        ;

//timeMoment:INT|INT 'am'|INT 'pm';
//ex. 2|3pm|4am
timeMoment: int postfix=var #TimeMomentPostfix
            ;

displayTerms:displayTerm displayTerms #DisplayTermsAppend
            | #DisplayTermsNullInit
            ;

displayTerm:',' var;

punchTerm: '>>' punchType rval #PunchTermExist
         | #PunchTermNotExist
         ;

//punchType:'Str'|'Bool'|enum;

punchType: var #PunchTypeVar
         | list#PunchTypeList
         ;

list:'[' listInternal']' #ListForward;

listInternal: rval ',' listInternal #ListAppend
            | rval                  #ListInit
            ;

// 决定不去搞打卡的"提示"?
// 或许能引入名称的语义. 如下划线收尾的就当成已经做完. 双下划收尾的当成不显示. 或者tag在某子树下的当成完成.
//internalSeq: internalSubSeq':'internalSeq|internalSubSeq;
//
//internalSubSeq:internalTerm*int'%'internalTerm;
//
//internalTerm : INT 'min'
//             | INT 'h'
//             | INT 'h' INT 'min'
//             | INT'd'
//             | INT'w'
//             ;
//

intervalTerm : fstVal=int fstUnit=var #IntervalTermOne
             | fstVal=int fstUnit=var sndVal=int sndUnit=var#IntervalTermTwo
             ;



//
//HELLO: ('hello'|'hi')  ;
////BYE  : ('bye'| 'tata') ;
//WEEKDAYABBR:('MON'|'TUE'|'WED'|'THU'|'FRI'|'SAT'|'SUN');
//MONTHABBR:('Jan'|'Feb'|'Mar'|'Apr'|'May'|'Jun'|'Jul'|'Aug'|'Sep'|'Oct'|'Nov'|'Dec');




//COMMENT : '//' ~[\r\n]* '\r'? '\n';
VARORLITERAL:NameStartChar NameChar*;
fragment
NameChar
    : NameStartChar
    | '0'..'9'
    | '_'
    | '\u00B7'
    | '\u0300'..'\u036F'
    | '\u203F'..'\u2040'
    ;
fragment
NameStartChar
    : 'A'..'Z' | 'a'..'z'
    | '\u00C0'..'\u00D6'
    | '\u00D8'..'\u00F6'
    | '\u00F8'..'\u02FF'
    | '\u0370'..'\u037D'
    | '\u037F'..'\u1FFF'
    | '\u200C'..'\u200D'
    | '\u2070'..'\u218F'
    | '\u2C00'..'\u2FEF'
    | '\u3001'..'\uD7FF'
    | '\uF900'..'\uFDCF'
    | '\uFDF0'..'\uFFFD'
    ;

INT  : [0-9]+         ;
STRLITERAL: '{'(('\\{'|'\\}'|~[{}])*)'}';
WS   : [ \t\n\r]+ -> skip ;