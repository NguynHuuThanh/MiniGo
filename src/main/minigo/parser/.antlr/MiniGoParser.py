# Generated from /Users/hoangnguyen/Desktop/DSA/PPL/Ass4/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,62,611,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,146,
        8,1,1,2,1,2,3,2,150,8,2,1,3,1,3,3,3,154,8,3,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,3,5,166,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,3,7,181,8,7,1,8,1,8,1,8,1,8,1,8,3,8,188,8,8,
        1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,201,8,9,1,10,1,10,
        3,10,205,8,10,1,11,1,11,1,11,1,11,1,11,3,11,212,8,11,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,226,8,13,1,
        14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,3,16,237,8,16,1,17,1,
        17,1,17,1,17,1,17,3,17,244,8,17,1,18,1,18,1,18,1,18,1,19,1,19,3,
        19,252,8,19,1,20,1,20,1,20,1,20,1,20,3,20,259,8,20,1,21,1,21,1,21,
        1,21,1,21,1,21,5,21,267,8,21,10,21,12,21,270,9,21,1,22,1,22,1,22,
        1,22,1,22,1,22,5,22,278,8,22,10,22,12,22,281,9,22,1,23,1,23,1,23,
        1,23,1,23,1,23,5,23,289,8,23,10,23,12,23,292,9,23,1,24,1,24,1,24,
        1,24,1,24,1,24,5,24,300,8,24,10,24,12,24,303,9,24,1,25,1,25,1,25,
        1,25,1,25,1,25,5,25,311,8,25,10,25,12,25,314,9,25,1,26,1,26,1,26,
        3,26,319,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,
        1,27,1,27,1,27,1,27,1,27,3,27,336,8,27,5,27,338,8,27,10,27,12,27,
        341,9,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,350,8,28,1,29,1,
        29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,3,30,361,8,30,1,30,1,30,1,
        31,1,31,1,31,1,31,1,32,1,32,1,32,1,32,3,32,373,8,32,1,33,1,33,1,
        33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,36,1,36,1,36,1,36,1,36,3,
        36,390,8,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,3,37,401,
        8,37,1,38,1,38,1,38,1,38,1,38,3,38,408,8,38,1,39,1,39,1,39,1,39,
        1,39,3,39,415,8,39,1,40,1,40,3,40,419,8,40,1,41,1,41,1,41,1,41,1,
        41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,42,3,42,435,8,42,1,
        43,1,43,1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,
        45,3,45,451,8,45,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,
        47,1,47,3,47,464,8,47,1,48,1,48,1,48,1,48,1,48,1,48,1,48,1,48,3,
        48,474,8,48,1,49,1,49,3,49,478,8,49,1,49,1,49,1,50,1,50,1,50,1,50,
        1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,5,51,
        498,8,51,10,51,12,51,501,9,51,1,52,1,52,1,52,1,52,1,53,1,53,1,53,
        1,53,1,53,1,53,3,53,513,8,53,1,53,3,53,516,8,53,1,53,1,53,1,54,1,
        54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,
        55,1,55,1,55,1,55,3,55,538,8,55,1,56,1,56,1,56,3,56,543,8,56,1,56,
        1,56,1,57,1,57,1,57,1,57,1,58,1,58,1,58,1,58,1,58,1,58,1,58,1,58,
        1,59,1,59,3,59,561,8,59,1,60,1,60,1,60,1,60,1,61,1,61,1,61,3,61,
        570,8,61,1,61,1,61,1,61,1,62,1,62,1,62,1,62,1,62,1,62,1,62,1,62,
        1,62,1,63,1,63,1,63,1,64,1,64,1,64,1,65,1,65,1,65,1,66,1,66,1,66,
        1,66,1,66,1,66,1,67,1,67,1,67,1,67,3,67,603,8,67,1,68,1,68,3,68,
        607,8,68,1,68,1,68,1,68,0,7,42,44,46,48,50,54,102,69,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,
        100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,
        132,134,136,0,7,2,0,9,12,52,52,1,0,52,53,1,0,26,31,1,0,21,22,1,0,
        23,25,2,0,22,22,34,34,1,0,36,41,611,0,138,1,0,0,0,2,145,1,0,0,0,
        4,149,1,0,0,0,6,153,1,0,0,0,8,155,1,0,0,0,10,165,1,0,0,0,12,167,
        1,0,0,0,14,180,1,0,0,0,16,187,1,0,0,0,18,200,1,0,0,0,20,204,1,0,
        0,0,22,211,1,0,0,0,24,213,1,0,0,0,26,225,1,0,0,0,28,227,1,0,0,0,
        30,229,1,0,0,0,32,236,1,0,0,0,34,243,1,0,0,0,36,245,1,0,0,0,38,251,
        1,0,0,0,40,258,1,0,0,0,42,260,1,0,0,0,44,271,1,0,0,0,46,282,1,0,
        0,0,48,293,1,0,0,0,50,304,1,0,0,0,52,318,1,0,0,0,54,320,1,0,0,0,
        56,349,1,0,0,0,58,351,1,0,0,0,60,360,1,0,0,0,62,364,1,0,0,0,64,372,
        1,0,0,0,66,374,1,0,0,0,68,377,1,0,0,0,70,382,1,0,0,0,72,384,1,0,
        0,0,74,400,1,0,0,0,76,407,1,0,0,0,78,414,1,0,0,0,80,418,1,0,0,0,
        82,420,1,0,0,0,84,434,1,0,0,0,86,436,1,0,0,0,88,439,1,0,0,0,90,450,
        1,0,0,0,92,452,1,0,0,0,94,463,1,0,0,0,96,473,1,0,0,0,98,477,1,0,
        0,0,100,481,1,0,0,0,102,486,1,0,0,0,104,502,1,0,0,0,106,506,1,0,
        0,0,108,519,1,0,0,0,110,537,1,0,0,0,112,542,1,0,0,0,114,546,1,0,
        0,0,116,550,1,0,0,0,118,560,1,0,0,0,120,562,1,0,0,0,122,566,1,0,
        0,0,124,574,1,0,0,0,126,583,1,0,0,0,128,586,1,0,0,0,130,589,1,0,
        0,0,132,592,1,0,0,0,134,602,1,0,0,0,136,604,1,0,0,0,138,139,3,2,
        1,0,139,140,5,0,0,1,140,1,1,0,0,0,141,142,3,60,30,0,142,143,3,2,
        1,0,143,146,1,0,0,0,144,146,3,60,30,0,145,141,1,0,0,0,145,144,1,
        0,0,0,146,3,1,0,0,0,147,150,3,6,3,0,148,150,1,0,0,0,149,147,1,0,
        0,0,149,148,1,0,0,0,150,5,1,0,0,0,151,154,3,8,4,0,152,154,3,24,12,
        0,153,151,1,0,0,0,153,152,1,0,0,0,154,7,1,0,0,0,155,156,7,0,0,0,
        156,9,1,0,0,0,157,166,5,53,0,0,158,166,5,54,0,0,159,166,5,55,0,0,
        160,166,5,19,0,0,161,166,5,20,0,0,162,166,3,12,6,0,163,166,3,30,
        15,0,164,166,5,18,0,0,165,157,1,0,0,0,165,158,1,0,0,0,165,159,1,
        0,0,0,165,160,1,0,0,0,165,161,1,0,0,0,165,162,1,0,0,0,165,163,1,
        0,0,0,165,164,1,0,0,0,166,11,1,0,0,0,167,168,3,24,12,0,168,169,5,
        45,0,0,169,170,3,22,11,0,170,171,5,46,0,0,171,13,1,0,0,0,172,181,
        5,53,0,0,173,181,5,54,0,0,174,181,5,52,0,0,175,181,5,55,0,0,176,
        181,5,19,0,0,177,181,5,20,0,0,178,181,3,30,15,0,179,181,5,18,0,0,
        180,172,1,0,0,0,180,173,1,0,0,0,180,174,1,0,0,0,180,175,1,0,0,0,
        180,176,1,0,0,0,180,177,1,0,0,0,180,178,1,0,0,0,180,179,1,0,0,0,
        181,15,1,0,0,0,182,183,3,14,7,0,183,184,5,49,0,0,184,185,3,16,8,
        0,185,188,1,0,0,0,186,188,3,14,7,0,187,182,1,0,0,0,187,186,1,0,0,
        0,188,17,1,0,0,0,189,190,5,45,0,0,190,191,3,18,9,0,191,192,5,46,
        0,0,192,201,1,0,0,0,193,194,5,45,0,0,194,195,3,18,9,0,195,196,5,
        49,0,0,196,197,3,18,9,0,197,198,5,46,0,0,198,201,1,0,0,0,199,201,
        3,16,8,0,200,189,1,0,0,0,200,193,1,0,0,0,200,199,1,0,0,0,201,19,
        1,0,0,0,202,205,3,14,7,0,203,205,3,18,9,0,204,202,1,0,0,0,204,203,
        1,0,0,0,205,21,1,0,0,0,206,207,3,20,10,0,207,208,5,49,0,0,208,209,
        3,22,11,0,209,212,1,0,0,0,210,212,3,20,10,0,211,206,1,0,0,0,211,
        210,1,0,0,0,212,23,1,0,0,0,213,214,3,26,13,0,214,215,3,6,3,0,215,
        25,1,0,0,0,216,217,5,47,0,0,217,218,3,28,14,0,218,219,5,48,0,0,219,
        220,3,26,13,0,220,226,1,0,0,0,221,222,5,47,0,0,222,223,3,28,14,0,
        223,224,5,48,0,0,224,226,1,0,0,0,225,216,1,0,0,0,225,221,1,0,0,0,
        226,27,1,0,0,0,227,228,7,1,0,0,228,29,1,0,0,0,229,230,5,52,0,0,230,
        231,5,45,0,0,231,232,3,32,16,0,232,233,5,46,0,0,233,31,1,0,0,0,234,
        237,3,34,17,0,235,237,1,0,0,0,236,234,1,0,0,0,236,235,1,0,0,0,237,
        33,1,0,0,0,238,239,3,36,18,0,239,240,5,49,0,0,240,241,3,34,17,0,
        241,244,1,0,0,0,242,244,3,36,18,0,243,238,1,0,0,0,243,242,1,0,0,
        0,244,35,1,0,0,0,245,246,5,52,0,0,246,247,5,51,0,0,247,248,3,42,
        21,0,248,37,1,0,0,0,249,252,3,40,20,0,250,252,1,0,0,0,251,249,1,
        0,0,0,251,250,1,0,0,0,252,39,1,0,0,0,253,254,3,42,21,0,254,255,5,
        49,0,0,255,256,3,40,20,0,256,259,1,0,0,0,257,259,3,42,21,0,258,253,
        1,0,0,0,258,257,1,0,0,0,259,41,1,0,0,0,260,261,6,21,-1,0,261,262,
        3,44,22,0,262,268,1,0,0,0,263,264,10,2,0,0,264,265,5,33,0,0,265,
        267,3,44,22,0,266,263,1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,268,
        269,1,0,0,0,269,43,1,0,0,0,270,268,1,0,0,0,271,272,6,22,-1,0,272,
        273,3,46,23,0,273,279,1,0,0,0,274,275,10,2,0,0,275,276,5,32,0,0,
        276,278,3,46,23,0,277,274,1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,
        0,279,280,1,0,0,0,280,45,1,0,0,0,281,279,1,0,0,0,282,283,6,23,-1,
        0,283,284,3,48,24,0,284,290,1,0,0,0,285,286,10,2,0,0,286,287,7,2,
        0,0,287,289,3,48,24,0,288,285,1,0,0,0,289,292,1,0,0,0,290,288,1,
        0,0,0,290,291,1,0,0,0,291,47,1,0,0,0,292,290,1,0,0,0,293,294,6,24,
        -1,0,294,295,3,50,25,0,295,301,1,0,0,0,296,297,10,2,0,0,297,298,
        7,3,0,0,298,300,3,50,25,0,299,296,1,0,0,0,300,303,1,0,0,0,301,299,
        1,0,0,0,301,302,1,0,0,0,302,49,1,0,0,0,303,301,1,0,0,0,304,305,6,
        25,-1,0,305,306,3,52,26,0,306,312,1,0,0,0,307,308,10,2,0,0,308,309,
        7,4,0,0,309,311,3,52,26,0,310,307,1,0,0,0,311,314,1,0,0,0,312,310,
        1,0,0,0,312,313,1,0,0,0,313,51,1,0,0,0,314,312,1,0,0,0,315,316,7,
        5,0,0,316,319,3,52,26,0,317,319,3,54,27,0,318,315,1,0,0,0,318,317,
        1,0,0,0,319,53,1,0,0,0,320,321,6,27,-1,0,321,322,3,56,28,0,322,339,
        1,0,0,0,323,324,10,3,0,0,324,325,5,47,0,0,325,326,3,42,21,0,326,
        327,5,48,0,0,327,338,1,0,0,0,328,329,10,2,0,0,329,330,5,42,0,0,330,
        335,5,52,0,0,331,332,5,43,0,0,332,333,3,38,19,0,333,334,5,44,0,0,
        334,336,1,0,0,0,335,331,1,0,0,0,335,336,1,0,0,0,336,338,1,0,0,0,
        337,323,1,0,0,0,337,328,1,0,0,0,338,341,1,0,0,0,339,337,1,0,0,0,
        339,340,1,0,0,0,340,55,1,0,0,0,341,339,1,0,0,0,342,350,3,10,5,0,
        343,350,5,52,0,0,344,350,3,58,29,0,345,346,5,43,0,0,346,347,3,42,
        21,0,347,348,5,44,0,0,348,350,1,0,0,0,349,342,1,0,0,0,349,343,1,
        0,0,0,349,344,1,0,0,0,349,345,1,0,0,0,350,57,1,0,0,0,351,352,5,52,
        0,0,352,353,5,43,0,0,353,354,3,38,19,0,354,355,5,44,0,0,355,59,1,
        0,0,0,356,361,3,62,31,0,357,361,3,68,34,0,358,361,3,70,35,0,359,
        361,3,80,40,0,360,356,1,0,0,0,360,357,1,0,0,0,360,358,1,0,0,0,360,
        359,1,0,0,0,361,362,1,0,0,0,362,363,5,50,0,0,363,61,1,0,0,0,364,
        365,5,14,0,0,365,366,5,52,0,0,366,367,3,64,32,0,367,63,1,0,0,0,368,
        373,3,6,3,0,369,370,3,4,2,0,370,371,3,66,33,0,371,373,1,0,0,0,372,
        368,1,0,0,0,372,369,1,0,0,0,373,65,1,0,0,0,374,375,5,35,0,0,375,
        376,3,42,21,0,376,67,1,0,0,0,377,378,5,13,0,0,378,379,5,52,0,0,379,
        380,5,35,0,0,380,381,3,42,21,0,381,69,1,0,0,0,382,383,3,72,36,0,
        383,71,1,0,0,0,384,389,5,5,0,0,385,386,5,43,0,0,386,387,5,52,0,0,
        387,388,5,52,0,0,388,390,5,44,0,0,389,385,1,0,0,0,389,390,1,0,0,
        0,390,391,1,0,0,0,391,392,5,52,0,0,392,393,5,43,0,0,393,394,3,74,
        37,0,394,395,5,44,0,0,395,396,3,4,2,0,396,397,3,104,52,0,397,73,
        1,0,0,0,398,401,3,76,38,0,399,401,1,0,0,0,400,398,1,0,0,0,400,399,
        1,0,0,0,401,75,1,0,0,0,402,403,3,78,39,0,403,404,5,49,0,0,404,405,
        3,76,38,0,405,408,1,0,0,0,406,408,3,78,39,0,407,402,1,0,0,0,407,
        406,1,0,0,0,408,77,1,0,0,0,409,410,5,52,0,0,410,411,5,49,0,0,411,
        415,3,78,39,0,412,413,5,52,0,0,413,415,3,6,3,0,414,409,1,0,0,0,414,
        412,1,0,0,0,415,79,1,0,0,0,416,419,3,82,41,0,417,419,3,88,44,0,418,
        416,1,0,0,0,418,417,1,0,0,0,419,81,1,0,0,0,420,421,5,6,0,0,421,422,
        5,52,0,0,422,423,5,7,0,0,423,424,5,45,0,0,424,425,3,84,42,0,425,
        426,5,46,0,0,426,83,1,0,0,0,427,428,3,86,43,0,428,429,5,50,0,0,429,
        430,3,84,42,0,430,435,1,0,0,0,431,432,3,86,43,0,432,433,5,50,0,0,
        433,435,1,0,0,0,434,427,1,0,0,0,434,431,1,0,0,0,435,85,1,0,0,0,436,
        437,5,52,0,0,437,438,3,6,3,0,438,87,1,0,0,0,439,440,5,6,0,0,440,
        441,5,52,0,0,441,442,5,8,0,0,442,443,5,45,0,0,443,444,3,90,45,0,
        444,445,5,46,0,0,445,89,1,0,0,0,446,447,3,92,46,0,447,448,3,90,45,
        0,448,451,1,0,0,0,449,451,3,92,46,0,450,446,1,0,0,0,450,449,1,0,
        0,0,451,91,1,0,0,0,452,453,5,52,0,0,453,454,5,43,0,0,454,455,3,74,
        37,0,455,456,5,44,0,0,456,457,3,4,2,0,457,458,5,50,0,0,458,93,1,
        0,0,0,459,460,3,96,48,0,460,461,3,94,47,0,461,464,1,0,0,0,462,464,
        3,96,48,0,463,459,1,0,0,0,463,462,1,0,0,0,464,95,1,0,0,0,465,474,
        3,98,49,0,466,474,3,100,50,0,467,474,3,106,53,0,468,474,3,112,56,
        0,469,474,3,126,63,0,470,474,3,128,64,0,471,474,3,130,65,0,472,474,
        3,136,68,0,473,465,1,0,0,0,473,466,1,0,0,0,473,467,1,0,0,0,473,468,
        1,0,0,0,473,469,1,0,0,0,473,470,1,0,0,0,473,471,1,0,0,0,473,472,
        1,0,0,0,474,97,1,0,0,0,475,478,3,62,31,0,476,478,3,68,34,0,477,475,
        1,0,0,0,477,476,1,0,0,0,478,479,1,0,0,0,479,480,5,50,0,0,480,99,
        1,0,0,0,481,482,3,102,51,0,482,483,7,6,0,0,483,484,3,42,21,0,484,
        485,5,50,0,0,485,101,1,0,0,0,486,487,6,51,-1,0,487,488,5,52,0,0,
        488,499,1,0,0,0,489,490,10,3,0,0,490,491,5,47,0,0,491,492,3,42,21,
        0,492,493,5,48,0,0,493,498,1,0,0,0,494,495,10,2,0,0,495,496,5,42,
        0,0,496,498,5,52,0,0,497,489,1,0,0,0,497,494,1,0,0,0,498,501,1,0,
        0,0,499,497,1,0,0,0,499,500,1,0,0,0,500,103,1,0,0,0,501,499,1,0,
        0,0,502,503,5,45,0,0,503,504,3,94,47,0,504,505,5,46,0,0,505,105,
        1,0,0,0,506,507,5,1,0,0,507,508,5,43,0,0,508,509,3,42,21,0,509,510,
        5,44,0,0,510,512,3,104,52,0,511,513,3,110,55,0,512,511,1,0,0,0,512,
        513,1,0,0,0,513,515,1,0,0,0,514,516,3,108,54,0,515,514,1,0,0,0,515,
        516,1,0,0,0,516,517,1,0,0,0,517,518,5,50,0,0,518,107,1,0,0,0,519,
        520,5,2,0,0,520,521,3,104,52,0,521,109,1,0,0,0,522,523,5,2,0,0,523,
        524,5,1,0,0,524,525,5,43,0,0,525,526,3,42,21,0,526,527,5,44,0,0,
        527,528,3,104,52,0,528,529,3,110,55,0,529,538,1,0,0,0,530,531,5,
        2,0,0,531,532,5,1,0,0,532,533,5,43,0,0,533,534,3,42,21,0,534,535,
        5,44,0,0,535,536,3,104,52,0,536,538,1,0,0,0,537,522,1,0,0,0,537,
        530,1,0,0,0,538,111,1,0,0,0,539,543,3,114,57,0,540,543,3,116,58,
        0,541,543,3,124,62,0,542,539,1,0,0,0,542,540,1,0,0,0,542,541,1,0,
        0,0,543,544,1,0,0,0,544,545,5,50,0,0,545,113,1,0,0,0,546,547,5,3,
        0,0,547,548,3,42,21,0,548,549,3,104,52,0,549,115,1,0,0,0,550,551,
        5,3,0,0,551,552,3,118,59,0,552,553,5,50,0,0,553,554,3,42,21,0,554,
        555,5,50,0,0,555,556,3,120,60,0,556,557,3,104,52,0,557,117,1,0,0,
        0,558,561,3,120,60,0,559,561,3,122,61,0,560,558,1,0,0,0,560,559,
        1,0,0,0,561,119,1,0,0,0,562,563,5,52,0,0,563,564,7,6,0,0,564,565,
        3,42,21,0,565,121,1,0,0,0,566,567,5,14,0,0,567,569,5,52,0,0,568,
        570,3,6,3,0,569,568,1,0,0,0,569,570,1,0,0,0,570,571,1,0,0,0,571,
        572,5,35,0,0,572,573,3,42,21,0,573,123,1,0,0,0,574,575,5,3,0,0,575,
        576,5,52,0,0,576,577,5,49,0,0,577,578,5,52,0,0,578,579,5,41,0,0,
        579,580,5,17,0,0,580,581,3,42,21,0,581,582,3,104,52,0,582,125,1,
        0,0,0,583,584,5,16,0,0,584,585,5,50,0,0,585,127,1,0,0,0,586,587,
        5,15,0,0,587,588,5,50,0,0,588,129,1,0,0,0,589,590,3,132,66,0,590,
        591,5,50,0,0,591,131,1,0,0,0,592,593,3,134,67,0,593,594,5,52,0,0,
        594,595,5,43,0,0,595,596,3,38,19,0,596,597,5,44,0,0,597,133,1,0,
        0,0,598,599,3,54,27,0,599,600,5,42,0,0,600,603,1,0,0,0,601,603,1,
        0,0,0,602,598,1,0,0,0,602,601,1,0,0,0,603,135,1,0,0,0,604,606,5,
        4,0,0,605,607,3,42,21,0,606,605,1,0,0,0,606,607,1,0,0,0,607,608,
        1,0,0,0,608,609,5,50,0,0,609,137,1,0,0,0,46,145,149,153,165,180,
        187,200,204,211,225,236,243,251,258,268,279,290,301,312,318,335,
        337,339,349,360,372,389,400,407,414,418,434,450,463,473,477,497,
        499,512,515,537,542,560,569,602,606
    ]

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
        self.checkVersion("4.13.1")
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




    def optional_variable_type(self):

        localctx = MiniGoParser.Optional_variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_optional_variable_type)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 47, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.variable_type()
                pass
            elif token in [35, 45, 50]:
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




    def variable_type(self):

        localctx = MiniGoParser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_type)
        try:
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11, 12, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.primitive_type()
                pass
            elif token in [47]:
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




    def primitive_type(self):

        localctx = MiniGoParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4503599627378176) != 0)):
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




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.match(MiniGoParser.INT_LIT)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.match(MiniGoParser.FLOAT_LIT)
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.match(MiniGoParser.STRING_LIT)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 160
                self.match(MiniGoParser.TRUE)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 5)
                self.state = 161
                self.match(MiniGoParser.FALSE)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 6)
                self.state = 162
                self.array_literal()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 7)
                self.state = 163
                self.struct_literal()
                pass
            elif token in [18]:
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




    def dim_literal(self):

        localctx = MiniGoParser.Dim_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dim_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not(_la==52 or _la==53):
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




    def optional_field_values(self):

        localctx = MiniGoParser.Optional_field_valuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_optional_field_values)
        try:
            self.state = 236
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.field_values()
                pass
            elif token in [46]:
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




    def optional_list_expression(self):

        localctx = MiniGoParser.Optional_list_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_optional_list_expression)
        try:
            self.state = 251
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19, 20, 22, 34, 43, 47, 52, 53, 54, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.list_expression()
                pass
            elif token in [44]:
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
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
                    if not(_la==21 or _la==22):
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
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
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




    def expression6(self):

        localctx = MiniGoParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                _la = self._input.LA(1)
                if not(_la==22 or _la==34):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 316
                self.expression6()
                pass
            elif token in [18, 19, 20, 43, 47, 52, 53, 54, 55]:
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




    def declaration(self):

        localctx = MiniGoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 356
                self.variable_declaration()
                pass
            elif token in [13]:
                self.state = 357
                self.constant_declaration()
                pass
            elif token in [5]:
                self.state = 358
                self.func_declaration()
                pass
            elif token in [6]:
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
            if _la==43:
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




    def list_param(self):

        localctx = MiniGoParser.List_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_list_param)
        try:
            self.state = 400
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.no_null_list_param()
                pass
            elif token in [44]:
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




    def declaration_stmt(self):

        localctx = MiniGoParser.Declaration_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_declaration_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 475
                self.variable_declaration()
                pass
            elif token in [13]:
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4329327034368) != 0)):
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
            if _la==2:
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




    def init_statement(self):

        localctx = MiniGoParser.Init_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_init_statement)
        try:
            self.state = 560
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.init_assign()
                pass
            elif token in [14]:
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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4329327034368) != 0)):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4644337115733504) != 0):
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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 67703545177833472) != 0):
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
         




