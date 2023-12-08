# Generated from HW2/gen/main.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("H\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3\27\n\3\f\3\16\3\32\13")
        buf.write("\3\3\4\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\7\5+\n\5\f\5\16\5.\13\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\7\69\n\6\f\6\16\6<\13\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7F\n\7\3\7\2\5\4\b\n\b\2\4\6\b\n")
        buf.write("\f\2\2\2K\2\16\3\2\2\2\4\21\3\2\2\2\6\33\3\2\2\2\b!\3")
        buf.write("\2\2\2\n/\3\2\2\2\fE\3\2\2\2\16\17\5\4\3\2\17\20\7\2\2")
        buf.write("\3\20\3\3\2\2\2\21\22\b\3\1\2\22\23\5\6\4\2\23\30\3\2")
        buf.write("\2\2\24\25\f\4\2\2\25\27\5\6\4\2\26\24\3\2\2\2\27\32\3")
        buf.write("\2\2\2\30\26\3\2\2\2\30\31\3\2\2\2\31\5\3\2\2\2\32\30")
        buf.write("\3\2\2\2\33\34\7\f\2\2\34\35\7\13\2\2\35\37\5\b\5\2\36")
        buf.write(" \7\16\2\2\37\36\3\2\2\2\37 \3\2\2\2 \7\3\2\2\2!\"\b\5")
        buf.write("\1\2\"#\5\n\6\2#,\3\2\2\2$%\f\5\2\2%&\7\7\2\2&+\5\n\6")
        buf.write("\2\'(\f\4\2\2()\7\b\2\2)+\5\n\6\2*$\3\2\2\2*\'\3\2\2\2")
        buf.write("+.\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\t\3\2\2\2.,\3\2\2\2/\60")
        buf.write("\b\6\1\2\60\61\5\f\7\2\61:\3\2\2\2\62\63\f\5\2\2\63\64")
        buf.write("\7\t\2\2\649\5\f\7\2\65\66\f\4\2\2\66\67\7\n\2\2\679\5")
        buf.write("\f\7\28\62\3\2\2\28\65\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3")
        buf.write("\2\2\2;\13\3\2\2\2<:\3\2\2\2=F\7\4\2\2>F\7\3\2\2?F\7\f")
        buf.write("\2\2@F\7\r\2\2AB\7\5\2\2BC\5\b\5\2CD\7\6\2\2DF\3\2\2\2")
        buf.write("E=\3\2\2\2E>\3\2\2\2E?\3\2\2\2E@\3\2\2\2EA\3\2\2\2F\r")
        buf.write("\3\2\2\2\t\30\37*,8:E")
        return buf.getvalue()


class mainParser ( Parser ):

    grammarFileName = "main.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'='", "<INVALID>", "<INVALID>", 
                     "'\n'" ]

    symbolicNames = [ "<INVALID>", "Comment", "BComment", "OP", "CP", "Plus", 
                      "MINUS", "MUL", "DIVIDE", "ASSIGN", "Id", "Number", 
                      "Newline", "Whitespace" ]

    RULE_start = 0
    RULE_prog = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_fact = 5

    ruleNames =  [ "start", "prog", "assign", "expr", "term", "fact" ]

    EOF = Token.EOF
    Comment=1
    BComment=2
    OP=3
    CP=4
    Plus=5
    MINUS=6
    MUL=7
    DIVIDE=8
    ASSIGN=9
    Id=10
    Number=11
    Newline=12
    Whitespace=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog(self):
            return self.getTypedRuleContext(mainParser.ProgContext,0)


        def EOF(self):
            return self.getToken(mainParser.EOF, 0)

        def getRuleIndex(self):
            return mainParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = mainParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.prog(0)
            self.state = 13
            self.match(mainParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(mainParser.AssignContext,0)


        def prog(self):
            return self.getTypedRuleContext(mainParser.ProgContext,0)


        def getRuleIndex(self):
            return mainParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)



    def prog(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mainParser.ProgContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_prog, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.assign()
            self._ctx.stop = self._input.LT(-1)
            self.state = 22
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = mainParser.ProgContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_prog)
                    self.state = 18
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 19
                    self.assign() 
                self.state = 24
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(mainParser.Id, 0)

        def ASSIGN(self):
            return self.getToken(mainParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def Newline(self):
            return self.getToken(mainParser.Newline, 0)

        def getRuleIndex(self):
            return mainParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = mainParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(mainParser.Id)
            self.state = 26
            self.match(mainParser.ASSIGN)
            self.state = 27
            self.expr(0)
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 28
                self.match(mainParser.Newline)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mainParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Rule_minusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)

        def MINUS(self):
            return self.getToken(mainParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_minus" ):
                listener.enterRule_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_minus" ):
                listener.exitRule_minus(self)


    class Rule_plusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)

        def Plus(self):
            return self.getToken(mainParser.Plus, 0)
        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_plus" ):
                listener.enterRule_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_plus" ):
                listener.exitRule_plus(self)


    class Rule3Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mainParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule3" ):
                listener.enterRule3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule3" ):
                listener.exitRule3(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mainParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = mainParser.Rule3Context(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 32
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 40
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = mainParser.Rule_plusContext(self, mainParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 35
                        self.match(mainParser.Plus)
                        self.state = 36
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = mainParser.Rule_minusContext(self, mainParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 38
                        self.match(mainParser.MINUS)
                        self.state = 39
                        self.term(0)
                        pass

             
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fact(self):
            return self.getTypedRuleContext(mainParser.FactContext,0)


        def term(self):
            return self.getTypedRuleContext(mainParser.TermContext,0)


        def MUL(self):
            return self.getToken(mainParser.MUL, 0)

        def DIVIDE(self):
            return self.getToken(mainParser.DIVIDE, 0)

        def getRuleIndex(self):
            return mainParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mainParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.fact()
            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = mainParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 48
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 49
                        self.match(mainParser.MUL)
                        self.state = 50
                        self.fact()
                        pass

                    elif la_ == 2:
                        localctx = mainParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 51
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 52
                        self.match(mainParser.DIVIDE)
                        self.state = 53
                        self.fact()
                        pass

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BComment(self):
            return self.getToken(mainParser.BComment, 0)

        def Comment(self):
            return self.getToken(mainParser.Comment, 0)

        def Id(self):
            return self.getToken(mainParser.Id, 0)

        def Number(self):
            return self.getToken(mainParser.Number, 0)

        def OP(self):
            return self.getToken(mainParser.OP, 0)

        def expr(self):
            return self.getTypedRuleContext(mainParser.ExprContext,0)


        def CP(self):
            return self.getToken(mainParser.CP, 0)

        def getRuleIndex(self):
            return mainParser.RULE_fact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFact" ):
                listener.enterFact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFact" ):
                listener.exitFact(self)




    def fact(self):

        localctx = mainParser.FactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fact)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mainParser.BComment]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(mainParser.BComment)
                pass
            elif token in [mainParser.Comment]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(mainParser.Comment)
                pass
            elif token in [mainParser.Id]:
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(mainParser.Id)
                pass
            elif token in [mainParser.Number]:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.match(mainParser.Number)
                pass
            elif token in [mainParser.OP]:
                self.enterOuterAlt(localctx, 5)
                self.state = 63
                self.match(mainParser.OP)
                self.state = 64
                self.expr(0)
                self.state = 65
                self.match(mainParser.CP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.prog_sempred
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def prog_sempred(self, localctx:ProgContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




