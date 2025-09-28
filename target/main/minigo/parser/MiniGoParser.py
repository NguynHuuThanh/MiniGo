# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3@")
        buf.write("\u0265\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u0094\n")
        buf.write("\3\3\4\3\4\5\4\u0098\n\4\3\5\3\5\5\5\u009c\n\5\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a8\n\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00b7")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u00be\n\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00cb\n")
        buf.write("\13\3\f\3\f\5\f\u00cf\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u00d6")
        buf.write("\n\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00e4\n\17\3\20\3\20\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\22\3\22\5\22\u00ef\n\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u00f6\n\23\3\24\3\24\3\24\3\24\3\25\3\25\5")
        buf.write("\25\u00fe\n\25\3\26\3\26\3\26\3\26\3\26\5\26\u0105\n\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u010d\n\27\f\27\16")
        buf.write("\27\u0110\13\27\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u0118")
        buf.write("\n\30\f\30\16\30\u011b\13\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\7\31\u0123\n\31\f\31\16\31\u0126\13\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\7\32\u012e\n\32\f\32\16\32\u0131")
        buf.write("\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0139\n\33\f")
        buf.write("\33\16\33\u013c\13\33\3\34\3\34\3\34\5\34\u0141\n\34\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\5\35\u0152\n\35\7\35\u0154\n\35\f")
        buf.write("\35\16\35\u0157\13\35\3\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\5\36\u0160\n\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 ")
        buf.write("\3 \5 \u016b\n \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\5\"")
        buf.write("\u0177\n\"\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\5&\u0188\n&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\5\'\u0193\n")
        buf.write("\'\3(\3(\3(\3(\3(\5(\u019a\n(\3)\3)\3)\3)\3)\5)\u01a1")
        buf.write("\n)\3*\3*\5*\u01a5\n*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3,\3,\5,\u01b5\n,\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\5/\u01c5\n/\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\5\61\u01d2\n\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\5\62\u01dc\n\62\3\63\3\63\5")
        buf.write("\63\u01e0\n\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\7\65")
        buf.write("\u01f4\n\65\f\65\16\65\u01f7\13\65\3\66\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\5\67\u0203\n\67\3\67\5")
        buf.write("\67\u0206\n\67\3\67\3\67\38\38\38\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\59\u021c\n9\3:\3:\3:\5:\u0221")
        buf.write("\n:\3:\3:\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\5")
        buf.write("=\u0233\n=\3>\3>\3>\3>\3?\3?\3?\5?\u023c\n?\3?\3?\3?\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3@\3@\3A\3A\3A\3B\3B\3B\3C\3C\3C\3")
        buf.write("D\3D\3D\3D\3D\3D\3E\3E\3E\3E\5E\u025d\nE\3F\3F\5F\u0261")
        buf.write("\nF\3F\3F\3F\2\t,.\60\62\648hG\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\2\t\4\2\13\16\66\66\3\2\66\67\3\2\34!\3\2\27\30\3\2\31")
        buf.write("\33\4\2\30\30$$\3\2&+\2\u0265\2\u008c\3\2\2\2\4\u0093")
        buf.write("\3\2\2\2\6\u0097\3\2\2\2\b\u009b\3\2\2\2\n\u009d\3\2\2")
        buf.write("\2\f\u00a7\3\2\2\2\16\u00a9\3\2\2\2\20\u00b6\3\2\2\2\22")
        buf.write("\u00bd\3\2\2\2\24\u00ca\3\2\2\2\26\u00ce\3\2\2\2\30\u00d5")
        buf.write("\3\2\2\2\32\u00d7\3\2\2\2\34\u00e3\3\2\2\2\36\u00e5\3")
        buf.write("\2\2\2 \u00e7\3\2\2\2\"\u00ee\3\2\2\2$\u00f5\3\2\2\2&")
        buf.write("\u00f7\3\2\2\2(\u00fd\3\2\2\2*\u0104\3\2\2\2,\u0106\3")
        buf.write("\2\2\2.\u0111\3\2\2\2\60\u011c\3\2\2\2\62\u0127\3\2\2")
        buf.write("\2\64\u0132\3\2\2\2\66\u0140\3\2\2\28\u0142\3\2\2\2:\u015f")
        buf.write("\3\2\2\2<\u0161\3\2\2\2>\u016a\3\2\2\2@\u016e\3\2\2\2")
        buf.write("B\u0176\3\2\2\2D\u0178\3\2\2\2F\u017b\3\2\2\2H\u0180\3")
        buf.write("\2\2\2J\u0182\3\2\2\2L\u0192\3\2\2\2N\u0199\3\2\2\2P\u01a0")
        buf.write("\3\2\2\2R\u01a4\3\2\2\2T\u01a6\3\2\2\2V\u01b4\3\2\2\2")
        buf.write("X\u01b6\3\2\2\2Z\u01b9\3\2\2\2\\\u01c4\3\2\2\2^\u01c6")
        buf.write("\3\2\2\2`\u01d1\3\2\2\2b\u01db\3\2\2\2d\u01df\3\2\2\2")
        buf.write("f\u01e3\3\2\2\2h\u01e8\3\2\2\2j\u01f8\3\2\2\2l\u01fc\3")
        buf.write("\2\2\2n\u0209\3\2\2\2p\u021b\3\2\2\2r\u0220\3\2\2\2t\u0224")
        buf.write("\3\2\2\2v\u0228\3\2\2\2x\u0232\3\2\2\2z\u0234\3\2\2\2")
        buf.write("|\u0238\3\2\2\2~\u0240\3\2\2\2\u0080\u0249\3\2\2\2\u0082")
        buf.write("\u024c\3\2\2\2\u0084\u024f\3\2\2\2\u0086\u0252\3\2\2\2")
        buf.write("\u0088\u025c\3\2\2\2\u008a\u025e\3\2\2\2\u008c\u008d\5")
        buf.write("\4\3\2\u008d\u008e\7\2\2\3\u008e\3\3\2\2\2\u008f\u0090")
        buf.write("\5> \2\u0090\u0091\5\4\3\2\u0091\u0094\3\2\2\2\u0092\u0094")
        buf.write("\5> \2\u0093\u008f\3\2\2\2\u0093\u0092\3\2\2\2\u0094\5")
        buf.write("\3\2\2\2\u0095\u0098\5\b\5\2\u0096\u0098\3\2\2\2\u0097")
        buf.write("\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098\7\3\2\2\2\u0099")
        buf.write("\u009c\5\n\6\2\u009a\u009c\5\32\16\2\u009b\u0099\3\2\2")
        buf.write("\2\u009b\u009a\3\2\2\2\u009c\t\3\2\2\2\u009d\u009e\t\2")
        buf.write("\2\2\u009e\13\3\2\2\2\u009f\u00a8\7\67\2\2\u00a0\u00a8")
        buf.write("\78\2\2\u00a1\u00a8\79\2\2\u00a2\u00a8\7\25\2\2\u00a3")
        buf.write("\u00a8\7\26\2\2\u00a4\u00a8\5\16\b\2\u00a5\u00a8\5 \21")
        buf.write("\2\u00a6\u00a8\7\24\2\2\u00a7\u009f\3\2\2\2\u00a7\u00a0")
        buf.write("\3\2\2\2\u00a7\u00a1\3\2\2\2\u00a7\u00a2\3\2\2\2\u00a7")
        buf.write("\u00a3\3\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a6\3\2\2\2\u00a8\r\3\2\2\2\u00a9\u00aa\5\32")
        buf.write("\16\2\u00aa\u00ab\7/\2\2\u00ab\u00ac\5\30\r\2\u00ac\u00ad")
        buf.write("\7\60\2\2\u00ad\17\3\2\2\2\u00ae\u00b7\7\67\2\2\u00af")
        buf.write("\u00b7\78\2\2\u00b0\u00b7\7\66\2\2\u00b1\u00b7\79\2\2")
        buf.write("\u00b2\u00b7\7\25\2\2\u00b3\u00b7\7\26\2\2\u00b4\u00b7")
        buf.write("\5 \21\2\u00b5\u00b7\7\24\2\2\u00b6\u00ae\3\2\2\2\u00b6")
        buf.write("\u00af\3\2\2\2\u00b6\u00b0\3\2\2\2\u00b6\u00b1\3\2\2\2")
        buf.write("\u00b6\u00b2\3\2\2\2\u00b6\u00b3\3\2\2\2\u00b6\u00b4\3")
        buf.write("\2\2\2\u00b6\u00b5\3\2\2\2\u00b7\21\3\2\2\2\u00b8\u00b9")
        buf.write("\5\20\t\2\u00b9\u00ba\7\63\2\2\u00ba\u00bb\5\22\n\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00be\5\20\t\2\u00bd\u00b8\3\2\2")
        buf.write("\2\u00bd\u00bc\3\2\2\2\u00be\23\3\2\2\2\u00bf\u00c0\7")
        buf.write("/\2\2\u00c0\u00c1\5\24\13\2\u00c1\u00c2\7\60\2\2\u00c2")
        buf.write("\u00cb\3\2\2\2\u00c3\u00c4\7/\2\2\u00c4\u00c5\5\24\13")
        buf.write("\2\u00c5\u00c6\7\63\2\2\u00c6\u00c7\5\24\13\2\u00c7\u00c8")
        buf.write("\7\60\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00cb\5\22\n\2\u00ca")
        buf.write("\u00bf\3\2\2\2\u00ca\u00c3\3\2\2\2\u00ca\u00c9\3\2\2\2")
        buf.write("\u00cb\25\3\2\2\2\u00cc\u00cf\5\20\t\2\u00cd\u00cf\5\24")
        buf.write("\13\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf\27")
        buf.write("\3\2\2\2\u00d0\u00d1\5\26\f\2\u00d1\u00d2\7\63\2\2\u00d2")
        buf.write("\u00d3\5\30\r\2\u00d3\u00d6\3\2\2\2\u00d4\u00d6\5\26\f")
        buf.write("\2\u00d5\u00d0\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\31\3")
        buf.write("\2\2\2\u00d7\u00d8\5\34\17\2\u00d8\u00d9\5\b\5\2\u00d9")
        buf.write("\33\3\2\2\2\u00da\u00db\7\61\2\2\u00db\u00dc\5\36\20\2")
        buf.write("\u00dc\u00dd\7\62\2\2\u00dd\u00de\5\34\17\2\u00de\u00e4")
        buf.write("\3\2\2\2\u00df\u00e0\7\61\2\2\u00e0\u00e1\5\36\20\2\u00e1")
        buf.write("\u00e2\7\62\2\2\u00e2\u00e4\3\2\2\2\u00e3\u00da\3\2\2")
        buf.write("\2\u00e3\u00df\3\2\2\2\u00e4\35\3\2\2\2\u00e5\u00e6\t")
        buf.write("\3\2\2\u00e6\37\3\2\2\2\u00e7\u00e8\7\66\2\2\u00e8\u00e9")
        buf.write("\7/\2\2\u00e9\u00ea\5\"\22\2\u00ea\u00eb\7\60\2\2\u00eb")
        buf.write("!\3\2\2\2\u00ec\u00ef\5$\23\2\u00ed\u00ef\3\2\2\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef#\3\2\2\2\u00f0")
        buf.write("\u00f1\5&\24\2\u00f1\u00f2\7\63\2\2\u00f2\u00f3\5$\23")
        buf.write("\2\u00f3\u00f6\3\2\2\2\u00f4\u00f6\5&\24\2\u00f5\u00f0")
        buf.write("\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6%\3\2\2\2\u00f7\u00f8")
        buf.write("\7\66\2\2\u00f8\u00f9\7\65\2\2\u00f9\u00fa\5,\27\2\u00fa")
        buf.write("\'\3\2\2\2\u00fb\u00fe\5*\26\2\u00fc\u00fe\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fc\3\2\2\2\u00fe)\3\2\2\2\u00ff")
        buf.write("\u0100\5,\27\2\u0100\u0101\7\63\2\2\u0101\u0102\5*\26")
        buf.write("\2\u0102\u0105\3\2\2\2\u0103\u0105\5,\27\2\u0104\u00ff")
        buf.write("\3\2\2\2\u0104\u0103\3\2\2\2\u0105+\3\2\2\2\u0106\u0107")
        buf.write("\b\27\1\2\u0107\u0108\5.\30\2\u0108\u010e\3\2\2\2\u0109")
        buf.write("\u010a\f\4\2\2\u010a\u010b\7#\2\2\u010b\u010d\5.\30\2")
        buf.write("\u010c\u0109\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3")
        buf.write("\2\2\2\u010e\u010f\3\2\2\2\u010f-\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0111\u0112\b\30\1\2\u0112\u0113\5\60\31\2\u0113")
        buf.write("\u0119\3\2\2\2\u0114\u0115\f\4\2\2\u0115\u0116\7\"\2\2")
        buf.write("\u0116\u0118\5\60\31\2\u0117\u0114\3\2\2\2\u0118\u011b")
        buf.write("\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a\3\2\2\2\u011a")
        buf.write("/\3\2\2\2\u011b\u0119\3\2\2\2\u011c\u011d\b\31\1\2\u011d")
        buf.write("\u011e\5\62\32\2\u011e\u0124\3\2\2\2\u011f\u0120\f\4\2")
        buf.write("\2\u0120\u0121\t\4\2\2\u0121\u0123\5\62\32\2\u0122\u011f")
        buf.write("\3\2\2\2\u0123\u0126\3\2\2\2\u0124\u0122\3\2\2\2\u0124")
        buf.write("\u0125\3\2\2\2\u0125\61\3\2\2\2\u0126\u0124\3\2\2\2\u0127")
        buf.write("\u0128\b\32\1\2\u0128\u0129\5\64\33\2\u0129\u012f\3\2")
        buf.write("\2\2\u012a\u012b\f\4\2\2\u012b\u012c\t\5\2\2\u012c\u012e")
        buf.write("\5\64\33\2\u012d\u012a\3\2\2\2\u012e\u0131\3\2\2\2\u012f")
        buf.write("\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130\63\3\2\2\2\u0131")
        buf.write("\u012f\3\2\2\2\u0132\u0133\b\33\1\2\u0133\u0134\5\66\34")
        buf.write("\2\u0134\u013a\3\2\2\2\u0135\u0136\f\4\2\2\u0136\u0137")
        buf.write("\t\6\2\2\u0137\u0139\5\66\34\2\u0138\u0135\3\2\2\2\u0139")
        buf.write("\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\65\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013e\t\7")
        buf.write("\2\2\u013e\u0141\5\66\34\2\u013f\u0141\58\35\2\u0140\u013d")
        buf.write("\3\2\2\2\u0140\u013f\3\2\2\2\u0141\67\3\2\2\2\u0142\u0143")
        buf.write("\b\35\1\2\u0143\u0144\5:\36\2\u0144\u0155\3\2\2\2\u0145")
        buf.write("\u0146\f\5\2\2\u0146\u0147\7\61\2\2\u0147\u0148\5,\27")
        buf.write("\2\u0148\u0149\7\62\2\2\u0149\u0154\3\2\2\2\u014a\u014b")
        buf.write("\f\4\2\2\u014b\u014c\7,\2\2\u014c\u0151\7\66\2\2\u014d")
        buf.write("\u014e\7-\2\2\u014e\u014f\5(\25\2\u014f\u0150\7.\2\2\u0150")
        buf.write("\u0152\3\2\2\2\u0151\u014d\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0154\3\2\2\2\u0153\u0145\3\2\2\2\u0153\u014a\3")
        buf.write("\2\2\2\u0154\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u01569\3\2\2\2\u0157\u0155\3\2\2\2\u0158\u0160")
        buf.write("\5\f\7\2\u0159\u0160\7\66\2\2\u015a\u0160\5<\37\2\u015b")
        buf.write("\u015c\7-\2\2\u015c\u015d\5,\27\2\u015d\u015e\7.\2\2\u015e")
        buf.write("\u0160\3\2\2\2\u015f\u0158\3\2\2\2\u015f\u0159\3\2\2\2")
        buf.write("\u015f\u015a\3\2\2\2\u015f\u015b\3\2\2\2\u0160;\3\2\2")
        buf.write("\2\u0161\u0162\7\66\2\2\u0162\u0163\7-\2\2\u0163\u0164")
        buf.write("\5(\25\2\u0164\u0165\7.\2\2\u0165=\3\2\2\2\u0166\u016b")
        buf.write("\5@!\2\u0167\u016b\5F$\2\u0168\u016b\5H%\2\u0169\u016b")
        buf.write("\5R*\2\u016a\u0166\3\2\2\2\u016a\u0167\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u0169\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016d\7\64\2\2\u016d?\3\2\2\2\u016e\u016f\7\20\2\2\u016f")
        buf.write("\u0170\7\66\2\2\u0170\u0171\5B\"\2\u0171A\3\2\2\2\u0172")
        buf.write("\u0177\5\b\5\2\u0173\u0174\5\6\4\2\u0174\u0175\5D#\2\u0175")
        buf.write("\u0177\3\2\2\2\u0176\u0172\3\2\2\2\u0176\u0173\3\2\2\2")
        buf.write("\u0177C\3\2\2\2\u0178\u0179\7%\2\2\u0179\u017a\5,\27\2")
        buf.write("\u017aE\3\2\2\2\u017b\u017c\7\17\2\2\u017c\u017d\7\66")
        buf.write("\2\2\u017d\u017e\7%\2\2\u017e\u017f\5,\27\2\u017fG\3\2")
        buf.write("\2\2\u0180\u0181\5J&\2\u0181I\3\2\2\2\u0182\u0187\7\7")
        buf.write("\2\2\u0183\u0184\7-\2\2\u0184\u0185\7\66\2\2\u0185\u0186")
        buf.write("\7\66\2\2\u0186\u0188\7.\2\2\u0187\u0183\3\2\2\2\u0187")
        buf.write("\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\7\66\2")
        buf.write("\2\u018a\u018b\7-\2\2\u018b\u018c\5L\'\2\u018c\u018d\7")
        buf.write(".\2\2\u018d\u018e\5\6\4\2\u018e\u018f\5j\66\2\u018fK\3")
        buf.write("\2\2\2\u0190\u0193\5N(\2\u0191\u0193\3\2\2\2\u0192\u0190")
        buf.write("\3\2\2\2\u0192\u0191\3\2\2\2\u0193M\3\2\2\2\u0194\u0195")
        buf.write("\5P)\2\u0195\u0196\7\63\2\2\u0196\u0197\5N(\2\u0197\u019a")
        buf.write("\3\2\2\2\u0198\u019a\5P)\2\u0199\u0194\3\2\2\2\u0199\u0198")
        buf.write("\3\2\2\2\u019aO\3\2\2\2\u019b\u019c\7\66\2\2\u019c\u019d")
        buf.write("\7\63\2\2\u019d\u01a1\5P)\2\u019e\u019f\7\66\2\2\u019f")
        buf.write("\u01a1\5\b\5\2\u01a0\u019b\3\2\2\2\u01a0\u019e\3\2\2\2")
        buf.write("\u01a1Q\3\2\2\2\u01a2\u01a5\5T+\2\u01a3\u01a5\5Z.\2\u01a4")
        buf.write("\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5S\3\2\2\2\u01a6")
        buf.write("\u01a7\7\b\2\2\u01a7\u01a8\7\66\2\2\u01a8\u01a9\7\t\2")
        buf.write("\2\u01a9\u01aa\7/\2\2\u01aa\u01ab\5V,\2\u01ab\u01ac\7")
        buf.write("\60\2\2\u01acU\3\2\2\2\u01ad\u01ae\5X-\2\u01ae\u01af\7")
        buf.write("\64\2\2\u01af\u01b0\5V,\2\u01b0\u01b5\3\2\2\2\u01b1\u01b2")
        buf.write("\5X-\2\u01b2\u01b3\7\64\2\2\u01b3\u01b5\3\2\2\2\u01b4")
        buf.write("\u01ad\3\2\2\2\u01b4\u01b1\3\2\2\2\u01b5W\3\2\2\2\u01b6")
        buf.write("\u01b7\7\66\2\2\u01b7\u01b8\5\b\5\2\u01b8Y\3\2\2\2\u01b9")
        buf.write("\u01ba\7\b\2\2\u01ba\u01bb\7\66\2\2\u01bb\u01bc\7\n\2")
        buf.write("\2\u01bc\u01bd\7/\2\2\u01bd\u01be\5\\/\2\u01be\u01bf\7")
        buf.write("\60\2\2\u01bf[\3\2\2\2\u01c0\u01c1\5^\60\2\u01c1\u01c2")
        buf.write("\5\\/\2\u01c2\u01c5\3\2\2\2\u01c3\u01c5\5^\60\2\u01c4")
        buf.write("\u01c0\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5]\3\2\2\2\u01c6")
        buf.write("\u01c7\7\66\2\2\u01c7\u01c8\7-\2\2\u01c8\u01c9\5L\'\2")
        buf.write("\u01c9\u01ca\7.\2\2\u01ca\u01cb\5\6\4\2\u01cb\u01cc\7")
        buf.write("\64\2\2\u01cc_\3\2\2\2\u01cd\u01ce\5b\62\2\u01ce\u01cf")
        buf.write("\5`\61\2\u01cf\u01d2\3\2\2\2\u01d0\u01d2\5b\62\2\u01d1")
        buf.write("\u01cd\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2a\3\2\2\2\u01d3")
        buf.write("\u01dc\5d\63\2\u01d4\u01dc\5f\64\2\u01d5\u01dc\5l\67\2")
        buf.write("\u01d6\u01dc\5r:\2\u01d7\u01dc\5\u0080A\2\u01d8\u01dc")
        buf.write("\5\u0082B\2\u01d9\u01dc\5\u0084C\2\u01da\u01dc\5\u008a")
        buf.write("F\2\u01db\u01d3\3\2\2\2\u01db\u01d4\3\2\2\2\u01db\u01d5")
        buf.write("\3\2\2\2\u01db\u01d6\3\2\2\2\u01db\u01d7\3\2\2\2\u01db")
        buf.write("\u01d8\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01da\3\2\2\2")
        buf.write("\u01dcc\3\2\2\2\u01dd\u01e0\5@!\2\u01de\u01e0\5F$\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01e2\7\64\2\2\u01e2e\3\2\2\2\u01e3\u01e4\5h\65")
        buf.write("\2\u01e4\u01e5\t\b\2\2\u01e5\u01e6\5,\27\2\u01e6\u01e7")
        buf.write("\7\64\2\2\u01e7g\3\2\2\2\u01e8\u01e9\b\65\1\2\u01e9\u01ea")
        buf.write("\7\66\2\2\u01ea\u01f5\3\2\2\2\u01eb\u01ec\f\5\2\2\u01ec")
        buf.write("\u01ed\7\61\2\2\u01ed\u01ee\5,\27\2\u01ee\u01ef\7\62\2")
        buf.write("\2\u01ef\u01f4\3\2\2\2\u01f0\u01f1\f\4\2\2\u01f1\u01f2")
        buf.write("\7,\2\2\u01f2\u01f4\7\66\2\2\u01f3\u01eb\3\2\2\2\u01f3")
        buf.write("\u01f0\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6i\3\2\2\2\u01f7\u01f5\3\2\2")
        buf.write("\2\u01f8\u01f9\7/\2\2\u01f9\u01fa\5`\61\2\u01fa\u01fb")
        buf.write("\7\60\2\2\u01fbk\3\2\2\2\u01fc\u01fd\7\3\2\2\u01fd\u01fe")
        buf.write("\7-\2\2\u01fe\u01ff\5,\27\2\u01ff\u0200\7.\2\2\u0200\u0202")
        buf.write("\5j\66\2\u0201\u0203\5p9\2\u0202\u0201\3\2\2\2\u0202\u0203")
        buf.write("\3\2\2\2\u0203\u0205\3\2\2\2\u0204\u0206\5n8\2\u0205\u0204")
        buf.write("\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0207\3\2\2\2\u0207")
        buf.write("\u0208\7\64\2\2\u0208m\3\2\2\2\u0209\u020a\7\4\2\2\u020a")
        buf.write("\u020b\5j\66\2\u020bo\3\2\2\2\u020c\u020d\7\4\2\2\u020d")
        buf.write("\u020e\7\3\2\2\u020e\u020f\7-\2\2\u020f\u0210\5,\27\2")
        buf.write("\u0210\u0211\7.\2\2\u0211\u0212\5j\66\2\u0212\u0213\5")
        buf.write("p9\2\u0213\u021c\3\2\2\2\u0214\u0215\7\4\2\2\u0215\u0216")
        buf.write("\7\3\2\2\u0216\u0217\7-\2\2\u0217\u0218\5,\27\2\u0218")
        buf.write("\u0219\7.\2\2\u0219\u021a\5j\66\2\u021a\u021c\3\2\2\2")
        buf.write("\u021b\u020c\3\2\2\2\u021b\u0214\3\2\2\2\u021cq\3\2\2")
        buf.write("\2\u021d\u0221\5t;\2\u021e\u0221\5v<\2\u021f\u0221\5~")
        buf.write("@\2\u0220\u021d\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u021f")
        buf.write("\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u0223\7\64\2\2\u0223")
        buf.write("s\3\2\2\2\u0224\u0225\7\5\2\2\u0225\u0226\5,\27\2\u0226")
        buf.write("\u0227\5j\66\2\u0227u\3\2\2\2\u0228\u0229\7\5\2\2\u0229")
        buf.write("\u022a\5x=\2\u022a\u022b\7\64\2\2\u022b\u022c\5,\27\2")
        buf.write("\u022c\u022d\7\64\2\2\u022d\u022e\5z>\2\u022e\u022f\5")
        buf.write("j\66\2\u022fw\3\2\2\2\u0230\u0233\5z>\2\u0231\u0233\5")
        buf.write("|?\2\u0232\u0230\3\2\2\2\u0232\u0231\3\2\2\2\u0233y\3")
        buf.write("\2\2\2\u0234\u0235\7\66\2\2\u0235\u0236\t\b\2\2\u0236")
        buf.write("\u0237\5,\27\2\u0237{\3\2\2\2\u0238\u0239\7\20\2\2\u0239")
        buf.write("\u023b\7\66\2\2\u023a\u023c\5\b\5\2\u023b\u023a\3\2\2")
        buf.write("\2\u023b\u023c\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023e")
        buf.write("\7%\2\2\u023e\u023f\5,\27\2\u023f}\3\2\2\2\u0240\u0241")
        buf.write("\7\5\2\2\u0241\u0242\7\66\2\2\u0242\u0243\7\63\2\2\u0243")
        buf.write("\u0244\7\66\2\2\u0244\u0245\7+\2\2\u0245\u0246\7\23\2")
        buf.write("\2\u0246\u0247\5,\27\2\u0247\u0248\5j\66\2\u0248\177\3")
        buf.write("\2\2\2\u0249\u024a\7\22\2\2\u024a\u024b\7\64\2\2\u024b")
        buf.write("\u0081\3\2\2\2\u024c\u024d\7\21\2\2\u024d\u024e\7\64\2")
        buf.write("\2\u024e\u0083\3\2\2\2\u024f\u0250\5\u0086D\2\u0250\u0251")
        buf.write("\7\64\2\2\u0251\u0085\3\2\2\2\u0252\u0253\5\u0088E\2\u0253")
        buf.write("\u0254\7\66\2\2\u0254\u0255\7-\2\2\u0255\u0256\5(\25\2")
        buf.write("\u0256\u0257\7.\2\2\u0257\u0087\3\2\2\2\u0258\u0259\5")
        buf.write("8\35\2\u0259\u025a\7,\2\2\u025a\u025d\3\2\2\2\u025b\u025d")
        buf.write("\3\2\2\2\u025c\u0258\3\2\2\2\u025c\u025b\3\2\2\2\u025d")
        buf.write("\u0089\3\2\2\2\u025e\u0260\7\6\2\2\u025f\u0261\5,\27\2")
        buf.write("\u0260\u025f\3\2\2\2\u0260\u0261\3\2\2\2\u0261\u0262\3")
        buf.write("\2\2\2\u0262\u0263\7\64\2\2\u0263\u008b\3\2\2\2\60\u0093")
        buf.write("\u0097\u009b\u00a7\u00b6\u00bd\u00ca\u00ce\u00d5\u00e3")
        buf.write("\u00ee\u00f5\u00fd\u0104\u010e\u0119\u0124\u012f\u013a")
        buf.write("\u0140\u0151\u0153\u0155\u015f\u016a\u0176\u0187\u0192")
        buf.write("\u0199\u01a0\u01a4\u01b4\u01c4\u01d1\u01db\u01df\u01f3")
        buf.write("\u01f5\u0202\u0205\u021b\u0220\u0232\u023b\u025c\u0260")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "':='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "RETURN", "FUNC", 
                      "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", 
                      "BOOL", "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", 
                      "NIL", "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", 
                      "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", 
                      "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", "COLON_ASSIGN", 
                      "DOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "COMMA", "SEMI", "COLON", "ID", "INT_LIT", 
                      "FLOAT_LIT", "STRING_LIT", "NEWLINE", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_program_element_list = 1
    RULE_optional_variable_type = 2
    RULE_variable_type = 3
    RULE_primitive_type = 4
    RULE_literal = 5
    RULE_array_literal = 6
    RULE_array_pre_element = 7
    RULE_array_pre_element_list = 8
    RULE_array_pre_element_array_lit = 9
    RULE_array_element = 10
    RULE_array_block = 11
    RULE_array_type = 12
    RULE_multiple_dimension = 13
    RULE_dim_literal = 14
    RULE_struct_literal = 15
    RULE_optional_field_values = 16
    RULE_field_values = 17
    RULE_field_value = 18
    RULE_optional_list_expression = 19
    RULE_list_expression = 20
    RULE_expression1 = 21
    RULE_expression2 = 22
    RULE_expression3 = 23
    RULE_expression4 = 24
    RULE_expression5 = 25
    RULE_expression6 = 26
    RULE_expression7 = 27
    RULE_expression8 = 28
    RULE_function_call = 29
    RULE_declaration = 30
    RULE_variable_declaration = 31
    RULE_variable_characteristic = 32
    RULE_initialization = 33
    RULE_constant_declaration = 34
    RULE_func_declaration = 35
    RULE_function_method_declaration = 36
    RULE_list_param = 37
    RULE_no_null_list_param = 38
    RULE_parameter = 39
    RULE_type_declaration = 40
    RULE_struct_declaration = 41
    RULE_list_of_fields = 42
    RULE_struct_parameter = 43
    RULE_interface_declaration = 44
    RULE_list_of_interface_methods = 45
    RULE_interface_method = 46
    RULE_list_statement = 47
    RULE_statement = 48
    RULE_declaration_stmt = 49
    RULE_assign_statement = 50
    RULE_lhs_assign = 51
    RULE_statement_block = 52
    RULE_if_statement = 53
    RULE_else_statement = 54
    RULE_else_if_statement = 55
    RULE_for_statement = 56
    RULE_basic_for_loop = 57
    RULE_for_loop_icu = 58
    RULE_init_statement = 59
    RULE_init_assign = 60
    RULE_init_declared = 61
    RULE_for_loop_range = 62
    RULE_break_statement = 63
    RULE_continue_statement = 64
    RULE_call_statement = 65
    RULE_function_method_call_stmt = 66
    RULE_optional_instance_stmt = 67
    RULE_return_statement = 68

    ruleNames =  [ "program", "program_element_list", "optional_variable_type", 
                   "variable_type", "primitive_type", "literal", "array_literal", 
                   "array_pre_element", "array_pre_element_list", "array_pre_element_array_lit", 
                   "array_element", "array_block", "array_type", "multiple_dimension", 
                   "dim_literal", "struct_literal", "optional_field_values", 
                   "field_values", "field_value", "optional_list_expression", 
                   "list_expression", "expression1", "expression2", "expression3", 
                   "expression4", "expression5", "expression6", "expression7", 
                   "expression8", "function_call", "declaration", "variable_declaration", 
                   "variable_characteristic", "initialization", "constant_declaration", 
                   "func_declaration", "function_method_declaration", "list_param", 
                   "no_null_list_param", "parameter", "type_declaration", 
                   "struct_declaration", "list_of_fields", "struct_parameter", 
                   "interface_declaration", "list_of_interface_methods", 
                   "interface_method", "list_statement", "statement", "declaration_stmt", 
                   "assign_statement", "lhs_assign", "statement_block", 
                   "if_statement", "else_statement", "else_if_statement", 
                   "for_statement", "basic_for_loop", "for_loop_icu", "init_statement", 
                   "init_assign", "init_declared", "for_loop_range", "break_statement", 
                   "continue_statement", "call_statement", "function_method_call_stmt", 
                   "optional_instance_stmt", "return_statement" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    RETURN=4
    FUNC=5
    TYPE=6
    STRUCT=7
    INTERFACE=8
    STRING=9
    INT=10
    FLOAT=11
    BOOL=12
    CONST=13
    VAR=14
    CONTINUE=15
    BREAK=16
    RANGE=17
    NIL=18
    TRUE=19
    FALSE=20
    ADD=21
    SUB=22
    MUL=23
    DIV=24
    MOD=25
    EQ=26
    NEQ=27
    LT=28
    LE=29
    GT=30
    GE=31
    AND=32
    OR=33
    NOT=34
    ASSIGN=35
    ADD_ASSIGN=36
    SUB_ASSIGN=37
    MUL_ASSIGN=38
    DIV_ASSIGN=39
    MOD_ASSIGN=40
    COLON_ASSIGN=41
    DOT=42
    LPAREN=43
    RPAREN=44
    LBRACE=45
    RBRACE=46
    LBRACK=47
    RBRACK=48
    COMMA=49
    SEMI=50
    COLON=51
    ID=52
    INT_LIT=53
    FLOAT_LIT=54
    STRING_LIT=55
    NEWLINE=56
    WS=57
    LINE_COMMENT=58
    BLOCK_COMMENT=59
    UNCLOSE_STRING=60
    ILLEGAL_ESCAPE=61
    ERROR_CHAR=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def program_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Program_element_listContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.program_element_list()
            self.state = 139
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(MiniGoParser.DeclarationContext,0)


        def program_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Program_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_element_list" ):
                return visitor.visitProgram_element_list(self)
            else:
                return visitor.visitChildren(self)




    def program_element_list(self):

        localctx = MiniGoParser.Program_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program_element_list)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.declaration()
                self.state = 142
                self.program_element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_variable_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_type(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_variable_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_variable_type" ):
                return visitor.visitOptional_variable_type(self)
            else:
                return visitor.visitChildren(self)




    def optional_variable_type(self):

        localctx = MiniGoParser.Optional_variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_optional_variable_type)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOL, MiniGoParser.LBRACK, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.variable_type()
                pass
            elif token in [MiniGoParser.ASSIGN, MiniGoParser.LBRACE, MiniGoParser.SEMI]:
                self.enterOuterAlt(localctx, 2)

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


    class Variable_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variable_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_type" ):
                return visitor.visitVariable_type(self)
            else:
                return visitor.visitChildren(self)




    def variable_type(self):

        localctx = MiniGoParser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_type)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRING, MiniGoParser.INT, MiniGoParser.FLOAT, MiniGoParser.BOOL, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.primitive_type()
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.array_type()
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


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def BOOL(self):
            return self.getToken(MiniGoParser.BOOL, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOL) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [MiniGoParser.FLOAT_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [MiniGoParser.TRUE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [MiniGoParser.FALSE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 161
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 6)
                self.state = 162
                self.array_literal()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 7)
                self.state = 163
                self.struct_literal()
                pass
            elif token in [MiniGoParser.NIL]:
                self.enterOuterAlt(localctx, 8)
                self.state = 164
                self.match(MiniGoParser.NIL)
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


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(MiniGoParser.Array_typeContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def array_block(self):
            return self.getTypedRuleContext(MiniGoParser.Array_blockContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.array_type()
            self.state = 168
            self.match(MiniGoParser.LBRACE)
            self.state = 169
            self.array_block()
            self.state = 170
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_pre_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_pre_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_pre_element" ):
                return visitor.visitArray_pre_element(self)
            else:
                return visitor.visitChildren(self)




    def array_pre_element(self):

        localctx = MiniGoParser.Array_pre_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_array_pre_element)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(MiniGoParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(MiniGoParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.match(MiniGoParser.STRING_LIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 176
                self.match(MiniGoParser.TRUE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 177
                self.match(MiniGoParser.FALSE)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 178
                self.struct_literal()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 179
                self.match(MiniGoParser.NIL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_pre_element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_pre_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_pre_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def array_pre_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_pre_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_pre_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_pre_element_list" ):
                return visitor.visitArray_pre_element_list(self)
            else:
                return visitor.visitChildren(self)




    def array_pre_element_list(self):

        localctx = MiniGoParser.Array_pre_element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_pre_element_list)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.array_pre_element()
                self.state = 183
                self.match(MiniGoParser.COMMA)
                self.state = 184
                self.array_pre_element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.array_pre_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_pre_element_array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def array_pre_element_array_lit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_pre_element_array_litContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_pre_element_array_litContext,i)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def array_pre_element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Array_pre_element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_pre_element_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_pre_element_array_lit" ):
                return visitor.visitArray_pre_element_array_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_pre_element_array_lit(self):

        localctx = MiniGoParser.Array_pre_element_array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_pre_element_array_lit)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                self.match(MiniGoParser.LBRACE)
                self.state = 190
                self.array_pre_element_array_lit()
                self.state = 191
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 193
                self.match(MiniGoParser.LBRACE)
                self.state = 194
                self.array_pre_element_array_lit()
                self.state = 195
                self.match(MiniGoParser.COMMA)
                self.state = 196
                self.array_pre_element_array_lit()
                self.state = 197
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.array_pre_element_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_elementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_pre_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_pre_elementContext,0)


        def array_pre_element_array_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Array_pre_element_array_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element" ):
                return visitor.visitArray_element(self)
            else:
                return visitor.visitChildren(self)




    def array_element(self):

        localctx = MiniGoParser.Array_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_element)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.array_pre_element()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.array_pre_element_array_lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_element(self):
            return self.getTypedRuleContext(MiniGoParser.Array_elementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def array_block(self):
            return self.getTypedRuleContext(MiniGoParser.Array_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_block" ):
                return visitor.visitArray_block(self)
            else:
                return visitor.visitChildren(self)




    def array_block(self):

        localctx = MiniGoParser.Array_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_block)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.array_element()
                self.state = 207
                self.match(MiniGoParser.COMMA)
                self.state = 208
                self.array_block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.array_element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiple_dimension(self):
            return self.getTypedRuleContext(MiniGoParser.Multiple_dimensionContext,0)


        def variable_type(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = MiniGoParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.multiple_dimension()
            self.state = 214
            self.variable_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiple_dimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def dim_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Dim_literalContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def multiple_dimension(self):
            return self.getTypedRuleContext(MiniGoParser.Multiple_dimensionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_multiple_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple_dimension" ):
                return visitor.visitMultiple_dimension(self)
            else:
                return visitor.visitChildren(self)




    def multiple_dimension(self):

        localctx = MiniGoParser.Multiple_dimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_multiple_dimension)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(MiniGoParser.LBRACK)
                self.state = 217
                self.dim_literal()
                self.state = 218
                self.match(MiniGoParser.RBRACK)
                self.state = 219
                self.multiple_dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(MiniGoParser.LBRACK)
                self.state = 222
                self.dim_literal()
                self.state = 223
                self.match(MiniGoParser.RBRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dim_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dim_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim_literal" ):
                return visitor.visitDim_literal(self)
            else:
                return visitor.visitChildren(self)




    def dim_literal(self):

        localctx = MiniGoParser.Dim_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dim_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def optional_field_values(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_field_valuesContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MiniGoParser.ID)
            self.state = 230
            self.match(MiniGoParser.LBRACE)
            self.state = 231
            self.optional_field_values()
            self.state = 232
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_field_valuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_values(self):
            return self.getTypedRuleContext(MiniGoParser.Field_valuesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_field_values

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_field_values" ):
                return visitor.visitOptional_field_values(self)
            else:
                return visitor.visitChildren(self)




    def optional_field_values(self):

        localctx = MiniGoParser.Optional_field_valuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_optional_field_values)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.field_values()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

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


    class Field_valuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_value(self):
            return self.getTypedRuleContext(MiniGoParser.Field_valueContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def field_values(self):
            return self.getTypedRuleContext(MiniGoParser.Field_valuesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_values

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_values" ):
                return visitor.visitField_values(self)
            else:
                return visitor.visitChildren(self)




    def field_values(self):

        localctx = MiniGoParser.Field_valuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_field_values)
        try:
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.field_value()
                self.state = 239
                self.match(MiniGoParser.COMMA)
                self.state = 240
                self.field_values()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.field_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_value" ):
                return visitor.visitField_value(self)
            else:
                return visitor.visitChildren(self)




    def field_value(self):

        localctx = MiniGoParser.Field_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_field_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(MiniGoParser.ID)
            self.state = 246
            self.match(MiniGoParser.COLON)
            self.state = 247
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_list_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_list_expression" ):
                return visitor.visitOptional_list_expression(self)
            else:
                return visitor.visitChildren(self)




    def optional_list_expression(self):

        localctx = MiniGoParser.Optional_list_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_optional_list_expression)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.SUB, MiniGoParser.NOT, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.list_expression()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

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


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.List_expressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = MiniGoParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_list_expression)
        try:
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.expression1(0)
                self.state = 254
                self.match(MiniGoParser.COMMA)
                self.state = 255
                self.list_expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.expression1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)



    def expression1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_expression1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.expression2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression1)
                    self.state = 263
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 264
                    self.match(MiniGoParser.OR)
                    self.state = 265
                    self.expression2(0) 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(MiniGoParser.Expression2Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expression2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 279
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 274
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 275
                    self.match(MiniGoParser.AND)
                    self.state = 276
                    self.expression3(0) 
                self.state = 281
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(MiniGoParser.Expression3Context,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 290
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 285
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 286
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 287
                    self.expression4(0) 
                self.state = 292
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(MiniGoParser.Expression4Context,0)


        def ADD(self):
            return self.getToken(MiniGoParser.ADD, 0)

        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.expression5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 301
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 296
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 297
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.ADD or _la==MiniGoParser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 298
                    self.expression5(0) 
                self.state = 303
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def expression5(self):
            return self.getTypedRuleContext(MiniGoParser.Expression5Context,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)



    def expression5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expression5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.expression6()
            self._ctx.stop = self._input.LT(-1)
            self.state = 312
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expression5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression5)
                    self.state = 307
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 308
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 309
                    self.expression6() 
                self.state = 314
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self):
            return self.getTypedRuleContext(MiniGoParser.Expression6Context,0)


        def SUB(self):
            return self.getToken(MiniGoParser.SUB, 0)

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = MiniGoParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SUB, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SUB or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 316
                self.expression6()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.expression7(0)
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


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression8(self):
            return self.getTypedRuleContext(MiniGoParser.Expression8Context,0)


        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def optional_list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_list_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)



    def expression7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expression7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expression7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.expression8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 339
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 337
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expression7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                        self.state = 323
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 324
                        self.match(MiniGoParser.LBRACK)
                        self.state = 325
                        self.expression1(0)
                        self.state = 326
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expression7Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7)
                        self.state = 328
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 329
                        self.match(MiniGoParser.DOT)
                        self.state = 330
                        self.match(MiniGoParser.ID)
                        self.state = 335
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                        if la_ == 1:
                            self.state = 331
                            self.match(MiniGoParser.LPAREN)
                            self.state = 332
                            self.optional_list_expression()
                            self.state = 333
                            self.match(MiniGoParser.RPAREN)


                        pass

             
                self.state = 341
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(MiniGoParser.Function_callContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)




    def expression8(self):

        localctx = MiniGoParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expression8)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 344
                self.function_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 345
                self.match(MiniGoParser.LPAREN)
                self.state = 346
                self.expression1(0)
                self.state = 347
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def optional_list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_list_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = MiniGoParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(MiniGoParser.ID)
            self.state = 352
            self.match(MiniGoParser.LPAREN)
            self.state = 353
            self.optional_list_expression()
            self.state = 354
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def variable_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declarationContext,0)


        def constant_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Constant_declarationContext,0)


        def func_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Func_declarationContext,0)


        def type_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Type_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.state = 356
                self.variable_declaration()
                pass
            elif token in [MiniGoParser.CONST]:
                self.state = 357
                self.constant_declaration()
                pass
            elif token in [MiniGoParser.FUNC]:
                self.state = 358
                self.func_declaration()
                pass
            elif token in [MiniGoParser.TYPE]:
                self.state = 359
                self.type_declaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 362
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def variable_characteristic(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_characteristicContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = MiniGoParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MiniGoParser.VAR)
            self.state = 365
            self.match(MiniGoParser.ID)
            self.state = 366
            self.variable_characteristic()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_characteristicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_type(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_typeContext,0)


        def optional_variable_type(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_variable_typeContext,0)


        def initialization(self):
            return self.getTypedRuleContext(MiniGoParser.InitializationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_variable_characteristic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_characteristic" ):
                return visitor.visitVariable_characteristic(self)
            else:
                return visitor.visitChildren(self)




    def variable_characteristic(self):

        localctx = MiniGoParser.Variable_characteristicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_variable_characteristic)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.variable_type()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.optional_variable_type()
                self.state = 370
                self.initialization()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = MiniGoParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_initialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(MiniGoParser.ASSIGN)
            self.state = 375
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constant_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constant_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant_declaration" ):
                return visitor.visitConstant_declaration(self)
            else:
                return visitor.visitChildren(self)




    def constant_declaration(self):

        localctx = MiniGoParser.Constant_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_constant_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self.match(MiniGoParser.CONST)
            self.state = 378
            self.match(MiniGoParser.ID)
            self.state = 379
            self.match(MiniGoParser.ASSIGN)
            self.state = 380
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_method_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Function_method_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declaration" ):
                return visitor.visitFunc_declaration(self)
            else:
                return visitor.visitChildren(self)




    def func_declaration(self):

        localctx = MiniGoParser.Func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_func_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.function_method_declaration()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def list_param(self):
            return self.getTypedRuleContext(MiniGoParser.List_paramContext,0)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def optional_variable_type(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_variable_typeContext,0)


        def statement_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_function_method_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_method_declaration" ):
                return visitor.visitFunction_method_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_method_declaration(self):

        localctx = MiniGoParser.Function_method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_function_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(MiniGoParser.FUNC)
            self.state = 389
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.LPAREN:
                self.state = 385
                self.match(MiniGoParser.LPAREN)
                self.state = 386
                self.match(MiniGoParser.ID)
                self.state = 387
                self.match(MiniGoParser.ID)
                self.state = 388
                self.match(MiniGoParser.RPAREN)


            self.state = 391
            self.match(MiniGoParser.ID)
            self.state = 392
            self.match(MiniGoParser.LPAREN)
            self.state = 393
            self.list_param()
            self.state = 394
            self.match(MiniGoParser.RPAREN)
            self.state = 395
            self.optional_variable_type()
            self.state = 396
            self.statement_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def no_null_list_param(self):
            return self.getTypedRuleContext(MiniGoParser.No_null_list_paramContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_param" ):
                return visitor.visitList_param(self)
            else:
                return visitor.visitChildren(self)




    def list_param(self):

        localctx = MiniGoParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_list_param)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.no_null_list_param()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

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


    class No_null_list_paramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def no_null_list_param(self):
            return self.getTypedRuleContext(MiniGoParser.No_null_list_paramContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_no_null_list_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNo_null_list_param" ):
                return visitor.visitNo_null_list_param(self)
            else:
                return visitor.visitChildren(self)




    def no_null_list_param(self):

        localctx = MiniGoParser.No_null_list_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_no_null_list_param)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.parameter()
                self.state = 403
                self.match(MiniGoParser.COMMA)
                self.state = 404
                self.no_null_list_param()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def parameter(self):
            return self.getTypedRuleContext(MiniGoParser.ParameterContext,0)


        def variable_type(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniGoParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_parameter)
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(MiniGoParser.ID)
                self.state = 410
                self.match(MiniGoParser.COMMA)
                self.state = 411
                self.parameter()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.match(MiniGoParser.ID)
                self.state = 413
                self.variable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_declarationContext,0)


        def interface_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_type_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_declaration" ):
                return visitor.visitType_declaration(self)
            else:
                return visitor.visitChildren(self)




    def type_declaration(self):

        localctx = MiniGoParser.Type_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_type_declaration)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.struct_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.interface_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_of_fields(self):
            return self.getTypedRuleContext(MiniGoParser.List_of_fieldsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_declaration" ):
                return visitor.visitStruct_declaration(self)
            else:
                return visitor.visitChildren(self)




    def struct_declaration(self):

        localctx = MiniGoParser.Struct_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_struct_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(MiniGoParser.TYPE)
            self.state = 421
            self.match(MiniGoParser.ID)
            self.state = 422
            self.match(MiniGoParser.STRUCT)
            self.state = 423
            self.match(MiniGoParser.LBRACE)
            self.state = 424
            self.list_of_fields()
            self.state = 425
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_fieldsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_parameter(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_parameterContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def list_of_fields(self):
            return self.getTypedRuleContext(MiniGoParser.List_of_fieldsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_of_fields

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_fields" ):
                return visitor.visitList_of_fields(self)
            else:
                return visitor.visitChildren(self)




    def list_of_fields(self):

        localctx = MiniGoParser.List_of_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_list_of_fields)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.struct_parameter()
                self.state = 428
                self.match(MiniGoParser.SEMI)
                self.state = 429
                self.list_of_fields()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 431
                self.struct_parameter()
                self.state = 432
                self.match(MiniGoParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def variable_type(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_parameter" ):
                return visitor.visitStruct_parameter(self)
            else:
                return visitor.visitChildren(self)




    def struct_parameter(self):

        localctx = MiniGoParser.Struct_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_struct_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(MiniGoParser.ID)
            self.state = 437
            self.variable_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_of_interface_methods(self):
            return self.getTypedRuleContext(MiniGoParser.List_of_interface_methodsContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_declaration" ):
                return visitor.visitInterface_declaration(self)
            else:
                return visitor.visitChildren(self)




    def interface_declaration(self):

        localctx = MiniGoParser.Interface_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_interface_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(MiniGoParser.TYPE)
            self.state = 440
            self.match(MiniGoParser.ID)
            self.state = 441
            self.match(MiniGoParser.INTERFACE)
            self.state = 442
            self.match(MiniGoParser.LBRACE)
            self.state = 443
            self.list_of_interface_methods()
            self.state = 444
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_of_interface_methodsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def interface_method(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_methodContext,0)


        def list_of_interface_methods(self):
            return self.getTypedRuleContext(MiniGoParser.List_of_interface_methodsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_of_interface_methods

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_of_interface_methods" ):
                return visitor.visitList_of_interface_methods(self)
            else:
                return visitor.visitChildren(self)




    def list_of_interface_methods(self):

        localctx = MiniGoParser.List_of_interface_methodsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_list_of_interface_methods)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.interface_method()
                self.state = 447
                self.list_of_interface_methods()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
                self.interface_method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_param(self):
            return self.getTypedRuleContext(MiniGoParser.List_paramContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def optional_variable_type(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_variable_typeContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_method" ):
                return visitor.visitInterface_method(self)
            else:
                return visitor.visitChildren(self)




    def interface_method(self):

        localctx = MiniGoParser.Interface_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_interface_method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(MiniGoParser.ID)
            self.state = 453
            self.match(MiniGoParser.LPAREN)
            self.state = 454
            self.list_param()
            self.state = 455
            self.match(MiniGoParser.RPAREN)
            self.state = 456
            self.optional_variable_type()
            self.state = 457
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_list_statement)
        try:
            self.state = 463
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.statement()
                self.state = 460
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Declaration_stmtContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(MiniGoParser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_statementContext,0)


        def call_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Call_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Return_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 473
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 465
                self.declaration_stmt()
                pass

            elif la_ == 2:
                self.state = 466
                self.assign_statement()
                pass

            elif la_ == 3:
                self.state = 467
                self.if_statement()
                pass

            elif la_ == 4:
                self.state = 468
                self.for_statement()
                pass

            elif la_ == 5:
                self.state = 469
                self.break_statement()
                pass

            elif la_ == 6:
                self.state = 470
                self.continue_statement()
                pass

            elif la_ == 7:
                self.state = 471
                self.call_statement()
                pass

            elif la_ == 8:
                self.state = 472
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def variable_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_declarationContext,0)


        def constant_declaration(self):
            return self.getTypedRuleContext(MiniGoParser.Constant_declarationContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declaration_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_stmt" ):
                return visitor.visitDeclaration_stmt(self)
            else:
                return visitor.visitChildren(self)




    def declaration_stmt(self):

        localctx = MiniGoParser.Declaration_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_declaration_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.VAR]:
                self.state = 475
                self.variable_declaration()
                pass
            elif token in [MiniGoParser.CONST]:
                self.state = 476
                self.constant_declaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 479
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_assignContext,0)


        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def COLON_ASSIGN(self):
            return self.getToken(MiniGoParser.COLON_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = MiniGoParser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.lhs_assign(0)
            self.state = 482
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN) | (1 << MiniGoParser.COLON_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 483
            self.expression1(0)
            self.state = 484
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lhs_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Lhs_assignContext,0)


        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs_assign" ):
                return visitor.visitLhs_assign(self)
            else:
                return visitor.visitChildren(self)



    def lhs_assign(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Lhs_assignContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_lhs_assign, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 499
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,37,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 497
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Lhs_assignContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_assign)
                        self.state = 489
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 490
                        self.match(MiniGoParser.LBRACK)
                        self.state = 491
                        self.expression1(0)
                        self.state = 492
                        self.match(MiniGoParser.RBRACK)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Lhs_assignContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs_assign)
                        self.state = 494
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 495
                        self.match(MiniGoParser.DOT)
                        self.state = 496
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 501
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,37,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Statement_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_statement_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_block" ):
                return visitor.visitStatement_block(self)
            else:
                return visitor.visitChildren(self)




    def statement_block(self):

        localctx = MiniGoParser.Statement_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_statement_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.match(MiniGoParser.LBRACE)
            self.state = 503
            self.list_statement()
            self.state = 504
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def statement_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_blockContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def else_if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = MiniGoParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(MiniGoParser.IF)
            self.state = 507
            self.match(MiniGoParser.LPAREN)
            self.state = 508
            self.expression1(0)
            self.state = 509
            self.match(MiniGoParser.RPAREN)
            self.state = 510
            self.statement_block()
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 511
                self.else_if_statement()


            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 514
                self.else_statement()


            self.state = 517
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def statement_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = MiniGoParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 519
            self.match(MiniGoParser.ELSE)
            self.state = 520
            self.statement_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_if_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def statement_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_blockContext,0)


        def else_if_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Else_if_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_else_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_if_statement" ):
                return visitor.visitElse_if_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_if_statement(self):

        localctx = MiniGoParser.Else_if_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_else_if_statement)
        try:
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.match(MiniGoParser.ELSE)
                self.state = 523
                self.match(MiniGoParser.IF)
                self.state = 524
                self.match(MiniGoParser.LPAREN)
                self.state = 525
                self.expression1(0)
                self.state = 526
                self.match(MiniGoParser.RPAREN)
                self.state = 527
                self.statement_block()
                self.state = 528
                self.else_if_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.match(MiniGoParser.ELSE)
                self.state = 531
                self.match(MiniGoParser.IF)
                self.state = 532
                self.match(MiniGoParser.LPAREN)
                self.state = 533
                self.expression1(0)
                self.state = 534
                self.match(MiniGoParser.RPAREN)
                self.state = 535
                self.statement_block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def basic_for_loop(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_for_loopContext,0)


        def for_loop_icu(self):
            return self.getTypedRuleContext(MiniGoParser.For_loop_icuContext,0)


        def for_loop_range(self):
            return self.getTypedRuleContext(MiniGoParser.For_loop_rangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = MiniGoParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_for_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 539
                self.basic_for_loop()
                pass

            elif la_ == 2:
                self.state = 540
                self.for_loop_icu()
                pass

            elif la_ == 3:
                self.state = 541
                self.for_loop_range()
                pass


            self.state = 544
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_for_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def statement_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for_loop

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for_loop" ):
                return visitor.visitBasic_for_loop(self)
            else:
                return visitor.visitChildren(self)




    def basic_for_loop(self):

        localctx = MiniGoParser.Basic_for_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_basic_for_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.match(MiniGoParser.FOR)
            self.state = 547
            self.expression1(0)
            self.state = 548
            self.statement_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_icuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def init_statement(self):
            return self.getTypedRuleContext(MiniGoParser.Init_statementContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMI)
            else:
                return self.getToken(MiniGoParser.SEMI, i)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def init_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Init_assignContext,0)


        def statement_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_icu

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_icu" ):
                return visitor.visitFor_loop_icu(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_icu(self):

        localctx = MiniGoParser.For_loop_icuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_for_loop_icu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.match(MiniGoParser.FOR)
            self.state = 551
            self.init_statement()
            self.state = 552
            self.match(MiniGoParser.SEMI)
            self.state = 553
            self.expression1(0)
            self.state = 554
            self.match(MiniGoParser.SEMI)
            self.state = 555
            self.init_assign()
            self.state = 556
            self.statement_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Init_assignContext,0)


        def init_declared(self):
            return self.getTypedRuleContext(MiniGoParser.Init_declaredContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_statement" ):
                return visitor.visitInit_statement(self)
            else:
                return visitor.visitChildren(self)




    def init_statement(self):

        localctx = MiniGoParser.Init_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_init_statement)
        try:
            self.state = 560
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.init_assign()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
                self.init_declared()
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


    class Init_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def COLON_ASSIGN(self):
            return self.getToken(MiniGoParser.COLON_ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_init_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_assign" ):
                return visitor.visitInit_assign(self)
            else:
                return visitor.visitChildren(self)




    def init_assign(self):

        localctx = MiniGoParser.Init_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_init_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(MiniGoParser.ID)
            self.state = 563
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN) | (1 << MiniGoParser.COLON_ASSIGN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 564
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_declaredContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def variable_type(self):
            return self.getTypedRuleContext(MiniGoParser.Variable_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_declared

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_declared" ):
                return visitor.visitInit_declared(self)
            else:
                return visitor.visitChildren(self)




    def init_declared(self):

        localctx = MiniGoParser.Init_declaredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_init_declared)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
            self.match(MiniGoParser.VAR)
            self.state = 567
            self.match(MiniGoParser.ID)
            self.state = 569
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOL) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 568
                self.variable_type()


            self.state = 571
            self.match(MiniGoParser.ASSIGN)
            self.state = 572
            self.expression1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_loop_rangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def COLON_ASSIGN(self):
            return self.getToken(MiniGoParser.COLON_ASSIGN, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def statement_block(self):
            return self.getTypedRuleContext(MiniGoParser.Statement_blockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_loop_range

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_loop_range" ):
                return visitor.visitFor_loop_range(self)
            else:
                return visitor.visitChildren(self)




    def for_loop_range(self):

        localctx = MiniGoParser.For_loop_rangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_for_loop_range)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(MiniGoParser.FOR)
            self.state = 575
            self.match(MiniGoParser.ID)
            self.state = 576
            self.match(MiniGoParser.COMMA)
            self.state = 577
            self.match(MiniGoParser.ID)
            self.state = 578
            self.match(MiniGoParser.COLON_ASSIGN)
            self.state = 579
            self.match(MiniGoParser.RANGE)
            self.state = 580
            self.expression1(0)
            self.state = 581
            self.statement_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = MiniGoParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.match(MiniGoParser.BREAK)
            self.state = 584
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = MiniGoParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(MiniGoParser.CONTINUE)
            self.state = 587
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_method_call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Function_method_call_stmtContext,0)


        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_call_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = MiniGoParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_call_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.function_method_call_stmt()
            self.state = 590
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_method_call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optional_instance_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_instance_stmtContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def optional_list_expression(self):
            return self.getTypedRuleContext(MiniGoParser.Optional_list_expressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_function_method_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_method_call_stmt" ):
                return visitor.visitFunction_method_call_stmt(self)
            else:
                return visitor.visitChildren(self)




    def function_method_call_stmt(self):

        localctx = MiniGoParser.Function_method_call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_function_method_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.optional_instance_stmt()
            self.state = 593
            self.match(MiniGoParser.ID)
            self.state = 594
            self.match(MiniGoParser.LPAREN)
            self.state = 595
            self.optional_list_expression()
            self.state = 596
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_instance_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(MiniGoParser.Expression7Context,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_optional_instance_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_instance_stmt" ):
                return visitor.visitOptional_instance_stmt(self)
            else:
                return visitor.visitChildren(self)




    def optional_instance_stmt(self):

        localctx = MiniGoParser.Optional_instance_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_optional_instance_stmt)
        try:
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.expression7(0)
                self.state = 599
                self.match(MiniGoParser.DOT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def expression1(self):
            return self.getTypedRuleContext(MiniGoParser.Expression1Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = MiniGoParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(MiniGoParser.RETURN)
            self.state = 606
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.SUB) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.LPAREN) | (1 << MiniGoParser.LBRACK) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 605
                self.expression1(0)


            self.state = 608
            self.match(MiniGoParser.SEMI)
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
        self._predicates[21] = self.expression1_sempred
        self._predicates[22] = self.expression2_sempred
        self._predicates[23] = self.expression3_sempred
        self._predicates[24] = self.expression4_sempred
        self._predicates[25] = self.expression5_sempred
        self._predicates[27] = self.expression7_sempred
        self._predicates[51] = self.lhs_assign_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression1_sempred(self, localctx:Expression1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression5_sempred(self, localctx:Expression5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expression7_sempred(self, localctx:Expression7Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def lhs_assign_sempred(self, localctx:Lhs_assignContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         




