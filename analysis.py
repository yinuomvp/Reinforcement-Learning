import matplotlib.pyplot as plt

Iterations_10=[i for i in range(1,11)]
Iterations_100=[i for i in range(1,101)]
Iterations_150=[i for i in range(1,151)]
Iterations_500=[i for i in range(1,501)]

Value_Iteration_Easy_10=[667,360,59,16,13,10,15,13,10,9]
Policy_Iteration_Easy_10=[293,181,229,14,9,10,11,13,15,9]
Q_Learning_Easy_10=[42,66,20,42,20,13,27,17,126,13]
Value_Iteration_Easy_100=[460,115,86,10,10,12,9,19,14,14,11,12,11,17,11,10,12,10,13,11,10,11,12,13,11,11,9,13,9,11,15,9,14,13,9,15,12,11,12,10,10,13,11,12,11,11,14,12,9,11,13,11,12,19,12,9,9,12,12,10,16,11,16,9,12,12,12,15,12,16,13,14,14,9,10,10,10,12,10,9,10,12,15,10,15,12,11,11,14,10,12,14,14,13,17,11,9,12,10,17]
Policy_Iteration_Easy_100=[427,907,429,16,14,15,12,9,12,9,10,10,13,10,11,11,16,11,13,11,10,13,9,11,12,9,12,9,12,14,11,20,12,11,11,22,11,9,12,12,20,12,15,11,14,11,10,15,10,9,10,12,14,10,12,10,11,11,9,11,12,9,12,16,9,17,10,13,9,9,11,12,10,12,9,11,12,14,16,16,11,12,14,12,10,13,10,12,10,15,12,10,14,12,10,12,14,9,9,14]
Q_Learning_Easy_100=[80,192,11,40,24,22,29,51,26,18,12,29,10,12,13,11,14,47,23,16,10,10,10,15,17,19,9,13,12,21,11,17,13,13,14,9,33,11,32,11,12,13,28,15,49,9,16,10,33,11,11,13,13,29,66,17,13,50,10,17,12,12,10,23,15,14,9,10,13,11,23,24,14,11,15,15,10,12,27,12,12,14,20,9,56,19,21,11,14,12,19,12,11,18,24,17,16,17,12,28]

Value_Iteration_Hard_150=[1011047,21445,2062,1090,2115,1246,1314,1954,576,648,927,776,764,863,910,519,232,179,60,52,48,48,44,45,52,44,49,44,44,37,43,38,52,46,46,46,50,39,41,41,51,51,40,41,38,40,49,47,42,52,51,48,48,38,53,52,42,46,44,43,39,47,47,46,49,41,39,46,46,48,40,42,44,43,44,42,45,45,50,50,40,38,44,49,49,53,50,43,42,39,51,39,50,43,41,54,41,42,54,45,40,51,51,47,52,44,48,41,44,48,49,45,35,42,44,46,41,41,41,39,38,53,53,43,48,34,53,42,47,44,43,49,47,46,39,46,41,47,47,48,44,55,53,43,39,50,43,37,45,40]
Policy_Iteration_Hard_150=[143141,20822,3571,847,3654,856,737,672,779,250,1239,11116,550,387,404,820,307,182270,295,76,50,39,50,45,45,44,42,50,51,50,55,52,46,45,43,47,45,53,37,44,42,50,35,37,36,48,45,44,42,49,46,55,43,52,48,39,52,48,50,44,45,39,45,43,44,46,47,41,40,49,55,42,48,39,41,40,49,39,47,39,37,40,41,44,49,37,37,37,52,46,48,40,39,44,39,55,50,49,42,54,51,44,43,46,50,48,44,48,48,44,39,45,42,47,47,51,60,48,45,51,44,56,44,46,46,40,36,42,40,50,37,44,45,50,48,45,46,43,39,42,43,46,46,47,43,56,45,48,47,43]
Q_Learning_Hard_150=[550,1899,1194,297,270,433,739,532,572,896,326,185,210,189,86,746,821,325,88,192,144,441,50,310,97,76,276,73,126,187,118,63,520,70,45,64,278,413,47,60,61,51,792,83,66,114,48,55,50,67,79,98,81,66,70,83,65,49,99,90,70,108,72,104,59,65,218,69,68,46,61,104,140,83,43,74,166,71,65,97,54,86,74,84,123,126,77,47,95,98,85,91,89,89,96,190,76,61,144,137,131,45,55,59,48,70,136,69,55,88,67,66,67,50,90,87,89,58,80,62,66,110,53,102,63,65,82,60,109,95,50,67,70,84,95,80,73,94,61,131,63,85,92,78,85,88,87,118,57,83]
Value_Iteration_Hard_500=[256507,30433,5124,1224,691,1852,809,1645,860,379,1667,653,163,1263,625,119,167,197,83,64,44,54,44,41,41,54,61,52,43,37,45,44,47,45,46,51,40,58,42,41,37,36,38,36,56,51,42,40,40,49,44,45,53,52,43,44,56,47,41,38,37,54,36,40,41,48,54,45,39,48,45,51,40,47,40,38,43,43,45,48,43,44,40,44,40,47,44,45,47,41,45,44,51,42,35,49,44,51,42,55,46,39,43,40,44,40,47,41,45,50,47,41,47,40,50,37,47,45,51,43,47,47,45,51,37,57,40,40,56,46,49,40,39,49,47,43,51,41,44,49,47,41,42,44,63,50,41,46,53,38,37,42,39,47,41,43,48,53,41,62,51,41,48,51,41,52,43,44,42,44,44,59,47,49,45,42,51,54,44,42,37,42,39,48,47,47,47,44,44,45,49,49,43,58,45,52,42,45,43,42,45,37,53,41,46,51,41,37,48,46,48,52,53,42,44,51,40,45,54,39,44,44,40,38,51,41,46,41,45,50,43,35,41,44,42,47,45,46,46,55,47,47,50,45,46,46,40,50,43,48,54,53,43,40,42,40,47,46,52,47,44,53,50,45,40,44,38,43,44,54,55,53,43,54,39,47,45,38,41,42,50,45,46,42,42,40,48,51,45,40,56,48,49,51,44,41,44,41,38,51,42,48,51,53,51,41,44,47,49,46,47,47,42,43,49,52,42,40,43,42,41,54,44,38,47,43,61,45,47,47,45,43,46,40,54,51,53,46,53,43,47,41,45,51,54,38,44,50,41,48,41,43,42,39,58,43,43,64,43,48,43,48,46,42,37,47,43,52,44,47,51,69,40,45,49,58,40,36,47,46,65,57,38,39,42,48,52,43,50,41,38,41,45,38,41,46,44,49,39,40,44,45,41,47,40,53,47,47,38,44,47,42,49,54,45,41,50,41,43,40,47,45,39,38,49,41,38,38,39,53,51,42,55,52,42,45,42,45,43,46,45,54,36,44,53,43,40,50,41,44,47,42,44,40,47,40,57,52,39,43,45,53,54,41,44,54,42,54,39,52,51,39,39,40,41,40,45,46,45,43,44,41,41,54,47,40,40,46,47,44,45,40,52,44,56,40,43,46,41,43]
Policy_Iteration_Hard_500=[161645,85737,6801,912,859,761,1247,1504,1384,909,1325,398,436,635,616,71,363,190,162,65,90,53,50,58,38,49,45,47,46,37,48,39,57,41,49,55,44,40,46,44,49,42,52,42,52,36,43,48,40,46,46,51,45,37,44,45,47,47,40,44,43,40,51,47,54,47,50,47,42,47,38,45,47,49,46,44,52,59,42,47,42,55,39,44,51,53,46,47,44,44,40,48,43,43,39,46,48,49,47,38,42,51,39,39,55,47,53,49,45,49,41,45,41,51,39,46,52,41,50,41,52,45,49,49,43,45,48,48,44,52,40,47,38,36,38,51,48,39,43,47,45,46,42,46,42,46,45,44,45,41,38,44,54,44,36,52,51,38,46,46,49,39,39,45,53,45,56,35,51,44,39,47,43,41,51,53,51,45,43,45,47,39,46,41,43,51,43,40,52,47,46,49,43,37,42,46,41,38,46,41,47,58,37,51,42,44,42,51,52,40,44,48,42,41,50,40,40,48,48,44,44,46,49,53,43,41,39,41,47,52,42,47,42,46,40,48,43,46,42,43,40,40,46,37,43,39,41,46,41,51,42,51,40,38,38,38,46,50,40,45,57,49,42,49,42,55,39,56,50,41,51,37,41,42,51,44,39,35,39,42,44,55,45,46,47,53,43,42,39,45,55,39,48,39,41,47,38,38,46,49,54,45,39,50,43,41,53,50,45,46,51,47,47,48,42,38,47,43,38,43,44,38,44,36,43,43,41,48,45,39,41,40,63,53,51,42,40,44,40,41,43,43,49,43,39,41,46,41,50,38,48,52,42,39,46,52,38,43,41,51,39,62,53,45,48,39,39,47,44,46,51,37,48,37,44,41,42,52,34,40,42,52,37,41,46,40,47,41,46,40,47,56,43,44,44,41,46,40,49,39,54,49,43,50,51,43,43,43,48,54,48,41,53,46,41,39,42,41,43,49,50,44,36,54,45,53,41,40,37,46,46,54,38,54,39,49,37,39,41,51,50,41,53,42,42,55,50,53,54,40,53,41,40,43,40,42,40,42,44,52,47,47,39,50,47,47,41,43,44,50,53,50,49,45,41,39,38,43,38,58,41,53,46,41,43,43,47,45,40,38,40,47,51,40,49,39,42,41,37,49]
Q_Learning_Hard_500=[369,2001,850,1702,138,509,378,585,283,217,152,208,225,390,390,680,496,169,76,190,255,161,100,167,324,126,112,129,264,110,361,104,354,134,157,169,103,74,77,94,66,116,114,63,98,48,52,83,55,260,57,51,119,92,83,67,49,57,76,63,58,71,49,77,85,339,77,63,97,241,66,78,95,63,139,115,154,102,85,56,98,117,61,45,149,61,70,53,69,125,53,69,68,51,86,60,100,65,86,230,49,67,90,65,85,89,103,89,99,90,172,141,94,57,178,83,119,56,83,81,50,89,66,65,63,80,457,137,117,67,119,89,54,59,125,56,56,84,102,66,175,137,80,45,46,124,78,61,67,51,52,112,118,74,90,58,70,142,79,44,128,115,97,93,68,81,64,69,65,170,73,75,111,86,65,73,111,100,94,62,185,65,48,189,55,112,67,77,77,95,56,67,83,112,136,111,159,83,60,90,98,127,125,49,314,83,94,112,46,57,120,107,69,85,117,56,175,59,68,55,62,82,106,67,100,62,72,116,147,54,93,47,140,66,72,76,109,112,80,152,62,130,114,66,73,83,91,48,69,150,91,81,157,62,109,147,102,87,65,55,38,151,85,207,113,137,69,46,82,255,80,55,130,160,107,58,94,138,184,68,58,128,46,68,72,77,52,46,49,72,107,62,116,57,54,115,96,110,73,272,134,53,86,86,89,156,78,93,105,90,128,253,69,98,118,77,74,79,42,88,56,76,69,67,120,47,72,110,72,71,82,78,63,46,59,116,50,71,102,80,77,63,63,76,72,57,100,77,60,53,73,125,114,76,103,125,79,83,63,55,56,117,61,90,83,50,61,58,72,162,67,60,68,107,119,50,67,80,65,60,378,75,60,57,55,147,82,150,85,95,126,50,65,93,79,96,91,102,59,97,97,89,95,158,189,76,63,74,80,136,69,91,124,72,60,103,88,85,67,117,88,73,67,65,53,56,145,55,72,205,308,190,61,94,88,103,83,84,71,64,76,131,116,90,51,66,80,57,95,84,53,117,89,63,104,64,85,145,239,87,64,70,177,96,105,50,104,54,108,288,88,92,57,49,105,47,61,61,71,109,66,78,95,71,93,55,82,94,190,79,125,85,69,124,87,46,69,426,112,58]

Value_Iteration_Time_Easy_10=[54,8,4,3,7,4,4,6,7,9]
Policy_Iteration_Time_Easy_10=[38,6,11,15,9,8,22,18,21,15]
Q_Learning_Time_Easy_10=[135,29,5,8,27,31,4,4,8,11]
Value_Iteration_Time_Easy_100=[36,10,7,5,4,5,6,11,22,8,7,10,15,11,14,9,8,10,23,23,15,21,37,19,47,22,29,22,26,9,9,17,11,15,18,9,16,31,19,32,20,30,17,36,25,22,9,14,21,16,17,24,12,18,20,16,41,33,42,17,21,10,13,9,10,12,13,9,19,27,35,30,16,18,12,12,20,17,22,17,19,14,21,19,16,12,25,26,14,101,29,22,17,14,22,54,39,37,15,52]
Policy_Iteration_Time_Easy_100=[42,5,3,3,10,4,18,10,5,8,11,20,23,37,19,19,31,23,25,31,20,14,12,12,12,8,8,8,12,15,19,15,23,25,20,13,11,13,11,13,11,12,15,21,21,23,22,17,15,15,16,15,26,26,28,24,26,18,17,20,16,23,30,30,28,22,18,20,19,19,39,35,32,23,23,20,21,31,31,34,29,23,23,24,32,39,45,26,24,28,33,36,38,31,27,27,34,39,41,32]
Q_Learning_Time_Easy_100=[17,5,4,7,7,7,6,8,3,4,3,6,5,3,5,4,4,9,6,2,11,2,3,3,4,4,2,3,4,3,3,2,2,3,2,2,3,3,3,2,3,2,3,3,5,2,3,3,6,3,6,4,3,4,3,4,7,9,4,4,7,4,4,5,7,7,7,7,7,7,7,5,8,9,5,7,6,4,5,5,4,8,7,9,11,12,9,5,4,6,9,10,7,12,6,10,8,7,10,7]

Value_Iteration_Time_Hard_150=[153,13,5,5,7,8,9,10,11,12,13,46,38,16,16,17,18,27,30,40,46,34,62,60,41,124,87,89,78,47,31,34,33,32,45,100,134,100,44,39,77,84,59,68,73,81,59,77,54,50,90,63,52,64,80,81,54,55,84,72,60,60,101,73,87,74,96,73,92,84,67,79,99,73,117,81,74,91,100,119,447,345,144,144,147,101,100,84,122,95,104,119,94,106,91,158,125,99,118,117,118,115,116,112,125,116,165,139,114,123,140,124,125,127,122,119,159,293,171,173,143,205,185,200,124,136,163,182,139,149,133,158,150,165,149,288,423,233,336,165,204,288,150,189,141,165,146,213,331,564]
Policy_Iteration_Time_Hard_150=[16,7,8,10,15,15,23,20,57,36,25,28,34,40,44,42,41,39,82,51,55,79,63,88,77,56,66,83,86,106,76,105,86,133,82,139,116,148,132,88,142,133,217,134,120,169,132,151,170,107,143,152,121,162,152,162,149,185,144,186,168,170,211,154,178,175,169,204,174,164,186,221,173,177,188,202,223,199,198,203,328,203,207,202,213,369,223,218,213,273,269,224,225,237,221,283,267,233,319,255,252,253,283,262,252,301,269,255,471,848,345,273,296,289,297,279,295,315,272,325,817,335,369,461,324,356,865,506,307,343,599,350,331,339,1250,412,352,546,361,368,340,357,357,344,339,361,374,361,354,433]
Q_Learning_Time_Hard_150=[88,154,23,42,17,24,27,25,33,31,30,27,65,39,40,34,40,30,37,38,33,36,63,70,49,44,35,41,38,40,36,40,43,43,42,39,49,55,42,50,47,43,52,47,50,49,60,50,49,50,51,52,48,47,50,45,48,51,52,47,48,49,50,53,48,59,49,52,57,61,48,54,53,53,57,53,54,58,67,61,53,61,60,60,53,59,126,58,232,78,72,73,78,74,64,66,57,74,64,71,68,61,64,198,83,64,74,65,52,64,72,69,74,66,67,107,78,90,81,85,84,85,77,74,71,67,77,66,64,69,71,73,77,68,72,85,66,72,68,76,67,71,79,80,84,72,74,76,74,77]
Value_Iteration_Time_Hard_500=[172,8,11,15,31,18,22,39,38,36,47,43,58,93,62,75,58,168,82,87,116,87,84,77,55,44,66,118,64,53,45,64,81,67,127,108,99,116,131,132,170,292,189,300,489,363,201,142,173,192,211,260,77,64,116,132,60,152,120,100,116,93,99,221,196,255,258,311,265,250,267,198,118,117,121,108,106,89,133,77,79,109,109,82,139,84,85,116,101,96,144,99,99,98,150,113,100,97,151,97,158,139,117,116,112,124,119,122,136,120,129,124,126,131,147,126,135,123,133,137,144,137,143,129,148,131,154,134,147,130,158,132,172,131,154,142,168,134,164,135,174,137,170,147,168,146,173,142,174,148,178,153,180,157,184,151,198,151,185,155,192,158,201,159,186,167,207,159,267,167,194,175,200,168,202,170,202,172,202,185,203,174,213,182,213,180,216,193,216,183,215,191,219,192,227,198,229,193,219,193,228,199,247,200,215,202,219,200,233,219,203,231,204,237,219,229,222,243,248,224,225,244,223,234,225,228,232,234,237,239,228,232,235,238,236,244,236,242,248,241,248,237,245,246,250,246,253,246,252,257,258,248,251,254,259,258,255,270,261,312,257,267,270,262,270,278,266,268,271,276,270,272,276,275,279,280,285,279,281,280,278,286,281,285,286,287,291,286,296,295,294,288,294,303,308,343,298,300,295,306,298,301,299,305,302,300,311,306,319,310,307,311,302,312,318,318,320,316,322,322,324,317,317,321,327,340,316,354,360,326,328,330,328,346,343,349,350,630,352,352,373,377,353,353,511,368,392,382,345,411,423,369,389,365,406,383,400,417,383,372,408,382,406,372,378,375,572,390,405,390,427,510,417,412,394,418,452,447,431,463,393,394,418,406,387,428,411,394,389,400,399,391,393,400,410,400,385,404,398,413,393,412,399,414,454,403,399,395,407,413,415,414,407,423,406,410,424,419,399,418,431,414,425,423,424,411,423,420,433,480,425,433,421,446,438,437,441,442,435,417,433,439,426,455,442,456,443,446,469,431,448,458,499,466,455,446,453,452,454,455,455,458,446,455,462,453,463,470,461,468,460,479,468,466,519,464,480,484,466,475,481,459,478,474,462,480,481,468,485,489,489,496,498,476,486,547,484,492,495,495]
Policy_Iteration_Time_Hard_500=[14, 7, 19, 34, 13, 22, 26, 60, 31, 46, 40, 32, 40, 127, 140, 40, 40, 67, 58, 49, 72, 71, 222, 87, 265, 73, 264, 170, 100, 91, 163, 119, 114, 109, 98, 108, 90, 98, 93, 96, 101, 99, 115, 111, 103, 123, 96, 131, 111, 136, 155, 123, 144, 154, 178, 173, 181, 193, 208, 176, 161, 182, 170, 177, 152, 171, 164, 182, 183, 167, 175, 169, 169, 171, 187, 183, 185, 189, 193, 192, 201, 200, 337, 391, 280, 379, 1074, 254, 247, 385, 372, 294, 519, 460, 292, 239, 268, 230, 200, 226, 290, 316, 272, 260, 268, 238, 365, 310, 279, 252, 249, 284, 292, 254, 401, 312, 302, 438, 288, 377, 328, 372, 334, 465, 330, 568, 420, 307, 376, 308, 271, 270, 277, 285, 321, 280, 357, 316, 313, 295, 301, 316, 286, 285, 287, 309, 296, 305, 306, 321, 351, 339, 337, 335, 321, 312, 314, 317, 341, 335, 355, 324, 324, 327, 333, 364, 353, 369, 364, 341, 357, 497, 508, 572, 436, 393, 566, 623, 421, 388, 369, 373, 365, 362, 371, 372, 375, 378, 394, 384, 380, 411, 397, 398, 417, 391, 394, 463, 422, 423, 406, 490, 488, 462, 439, 427, 416, 413, 412, 425, 420, 419, 423, 428, 427, 450, 430, 434, 443, 442, 452, 459, 480, 566, 584, 679, 472, 461, 485, 520, 491, 518, 882, 738, 578, 531, 541, 502, 495, 572, 694, 597, 556, 632, 723, 596, 499, 496, 510, 519, 518, 524, 510, 501, 520, 531, 518, 537, 540, 530, 532, 525, 559, 533, 559, 598, 536, 532, 536, 559, 542, 554, 557, 560, 539, 560, 567, 574, 572, 596, 650, 666, 634, 734, 705, 711, 776, 662, 673, 780, 682, 605, 990, 642, 885, 982, 728, 620, 643, 782, 711, 627, 631, 626, 668, 676, 662, 637, 727, 805, 647, 703, 656, 670, 800, 731, 636, 639, 776, 729, 724, 669, 1199, 362, 1532, 1662, 1843, 1375, 1760, 962, 988, 1923, 1300, 2045, 1241, 885, 1028, 848, 845, 829, 827, 860, 910, 1000, 1221, 1037, 1166, 1529, 934, 910, 897, 938, 992, 923, 1087, 922, 953, 885, 860, 885, 1399, 1389, 1118, 1440, 966, 992, 924, 970, 1156, 1033, 1249, 1151, 1147, 1080, 975, 1018, 1590, 1374, 1225, 1258, 1022, 914, 936, 925, 950, 906, 973, 983, 959, 963, 955, 1391, 2070, 359, 1243, 1772, 1550, 351, 1233, 1078, 1097, 1092, 1052, 1075, 1050, 1064, 1104, 1087, 1131, 1109, 1074, 1154, 1088, 1119, 1113, 1128, 1088, 1139, 1108, 1117, 1197, 1078, 1131, 1096, 1187, 1249, 1261, 1164, 1157, 1215, 1156, 1106, 1178, 1125, 1150, 1162, 1096, 1145, 1215, 1178, 1160, 1154, 1182, 1190, 1182, 1151, 1235, 1258, 1243, 1256, 1196, 1216, 1223, 1219, 1227, 1256, 1328, 1409, 826, 160, 1994, 1340, 1418, 1700, 1261, 1250, 1221, 1241, 1210, 1205, 1217, 1224, 1280, 1278, 1216, 1189, 1276, 1257, 1317, 1457, 1224, 1291, 1297, 1299, 1303, 1277, 1400, 1256, 1266, 1291, 925, 1465, 2000, 1754, 1661, 2066, 1749, 1369, 1639, 1339]
Q_Learning_Time_Hard_500=[94,35,18,56,30,21,28,59,33,42,36,39,26,37,24,83,72,45,44,50,50,32,33,43,37,38,41,42,39,35,32,34,34,36,35,35,38,41,36,34,36,34,37,37,43,36,40,38,36,42,45,44,41,41,39,34,40,44,36,43,51,44,47,40,48,43,45,60,40,46,45,50,44,51,49,45,53,45,45,49,51,49,53,54,54,57,52,50,44,52,48,53,51,54,56,54,56,56,57,77,61,61,51,62,58,56,53,54,59,62,62,53,54,58,62,70,61,55,73,58,69,72,67,67,66,70,62,63,63,66,57,64,68,72,72,68,65,60,64,61,69,64,81,68,64,68,65,72,79,72,79,85,72,73,78,69,70,66,66,77,83,90,74,65,73,67,89,78,70,79,73,78,92,68,75,78,72,77,77,68,82,80,83,84,83,82,73,88,79,80,102,117,221,401,234,102,80,87,83,177,111,94,103,92,82,82,80,80,84,103,99,109,91,87,83,78,92,87,92,104,87,85,78,89,97,103,80,85,84,114,89,93,91,94,87,86,95,90,98,126,111,90,89,93,105,103,124,93,112,89,99,116,99,113,114,96,102,97,124,89,86,100,96,105,100,89,103,86,109,111,92,104,99,90,136,129,123,126,104,98,104,114,98,102,106,100,96,95,92,98,105,104,104,102,117,103,105,104,103,106,109,101,105,124,136,125,104,109,106,135,105,113,106,103,153,104,107,107,127,123,110,106,123,120,107,115,113,116,123,121,132,120,112,150,118,113,115,105,118,129,111,120,122,113,120,116,118,123,119,107,115,116,115,117,126,135,118,121,115,138,117,120,121,113,115,130,130,121,118,118,142,131,123,139,118,145,126,118,115,126,127,119,121,144,119,144,134,158,132,131,135,136,124,119,130,159,122,128,141,138,128,130,127,129,147,135,134,133,136,139,138,149,151,214,165,148,131,141,147,163,180,135,142,174,142,144,147,136,143,143,131,127,140,136,140,142,141,145,152,148,153,129,140,146,134,149,149,147,136,161,139,139,139,140,154,136,151,159,143,133,142,149,141,133,172,143,145,150,147,144,166,146,150,139,143,149,157,160,158,167,183,157,236,169,170,155,158,192,164,149,166,166,155,198,143,160,181,160,167,154]

Value_Iteration_Rewards_Easy_10=[-565.0,-258.0,43.0,86.0,89.0,92.0,87.0,89.0,92.0,93.0]
Policy_Iteration_Rewards_Easy_10=[-191.0,-79.0,-127.0,88.0,93.0,92.0,91.0,89.0,87.0,93.0]
Q_Learning_Rewards_Easy_10=[60.0,36.0,82.0,60.0,82.0,89.0,75.0,85.0,-24.0,89.0]
Value_Iteration_Rewards_Easy_100=[-358.0,-13.0,16.0,92.0,92.0,90.0,93.0,83.0,88.0,88.0,91.0,90.0,91.0,85.0,91.0,92.0,90.0,92.0,89.0,91.0,92.0,91.0,90.0,89.0,91.0,91.0,93.0,89.0,93.0,91.0,87.0,93.0,88.0,89.0,93.0,87.0,90.0,91.0,90.0,92.0,92.0,89.0,91.0,90.0,91.0,91.0,88.0,90.0,93.0,91.0,89.0,91.0,90.0,83.0,90.0,93.0,93.0,90.0,90.0,92.0,86.0,91.0,86.0,93.0,90.0,90.0,90.0,87.0,90.0,86.0,89.0,88.0,88.0,93.0,92.0,92.0,92.0,90.0,92.0,93.0,92.0,90.0,87.0,92.0,87.0,90.0,91.0,91.0,88.0,92.0,90.0,88.0,88.0,89.0,85.0,91.0,93.0,90.0,92.0,85.0]
Policy_Iteration_Rewards_Easy_100=[-325.0,-805.0,-327.0,86.0,88.0,87.0,90.0,93.0,90.0,93.0,92.0,92.0,89.0,92.0,91.0,91.0,86.0,91.0,89.0,91.0,92.0,89.0,93.0,91.0,90.0,93.0,90.0,93.0,90.0,88.0,91.0,82.0,90.0,91.0,91.0,80.0,91.0,93.0,90.0,90.0,82.0,90.0,87.0,91.0,88.0,91.0,92.0,87.0,92.0,93.0,92.0,90.0,88.0,92.0,90.0,92.0,91.0,91.0,93.0,91.0,90.0,93.0,90.0,86.0,93.0,85.0,92.0,89.0,93.0,93.0,91.0,90.0,92.0,90.0,93.0,91.0,90.0,88.0,86.0,86.0,91.0,90.0,88.0,90.0,92.0,89.0,92.0,90.0,92.0,87.0,90.0,92.0,88.0,90.0,92.0,90.0,88.0,93.0,93.0,88.0]
Q_Learning_Rewards_Easy_100=[22.0,-90.0,91.0,62.0,78.0,80.0,73.0,51.0,76.0,84.0,90.0,73.0,92.0,90.0,89.0,91.0,88.0,55.0,79.0,86.0,92.0,92.0,92.0,87.0,85.0,83.0,93.0,89.0,90.0,81.0,91.0,85.0,89.0,89.0,88.0,93.0,69.0,91.0,70.0,91.0,90.0,89.0,74.0,87.0,53.0,93.0,86.0,92.0,69.0,91.0,91.0,89.0,89.0,73.0,36.0,85.0,89.0,52.0,92.0,85.0,90.0,90.0,92.0,79.0,87.0,88.0,93.0,92.0,89.0,91.0,79.0,78.0,88.0,91.0,87.0,87.0,92.0,90.0,75.0,90.0,90.0,88.0,82.0,93.0,46.0,83.0,81.0,91.0,88.0,90.0,83.0,90.0,91.0,84.0,78.0,85.0,86.0,85.0,90.0,74.0]

Value_Iteration_Rewards_Hard_150=[-1010945.0,-21343.0,-1960.0,-988.0,-2013.0,-1144.0,-1212.0,-1852.0,-474.0,-546.0,-825.0,-674.0,-662.0,-761.0,-808.0,-417.0,-130.0,-77.0,42.0,50.0,54.0,54.0,58.0,57.0,50.0,58.0,53.0,58.0,58.0,65.0,59.0,64.0,50.0,56.0,56.0,56.0,52.0,63.0,61.0,61.0,51.0,51.0,62.0,61.0,64.0,62.0,53.0,55.0,60.0,50.0,51.0,54.0,54.0,64.0,49.0,50.0,60.0,56.0,58.0,59.0,63.0,55.0,55.0,56.0,53.0,61.0,63.0,56.0,56.0,54.0,62.0,60.0,58.0,59.0,58.0,60.0,57.0,57.0,52.0,52.0,62.0,64.0,58.0,53.0,53.0,49.0,52.0,59.0,60.0,63.0,51.0,63.0,52.0,59.0,61.0,48.0,61.0,60.0,48.0,57.0,62.0,51.0,51.0,55.0,50.0,58.0,54.0,61.0,58.0,54.0,53.0,57.0,67.0,60.0,58.0,56.0,61.0,61.0,61.0,63.0,64.0,49.0,49.0,59.0,54.0,68.0,49.0,60.0,55.0,58.0,59.0,53.0,55.0,56.0,63.0,56.0,61.0,55.0,55.0,54.0,58.0,47.0,49.0,59.0,63.0,52.0,59.0,65.0,57.0,62.0]
Policy_Iteration_Rewards_Hard_150=[-143039.0,-20720.0,-3469.0,-745.0,-3552.0,-754.0,-635.0,-570.0,-677.0,-148.0,-1137.0,-11014.0,-448.0,-285.0,-302.0,-718.0,-205.0,-182168.0,-193.0,26.0,52.0,63.0,52.0,57.0,57.0,58.0,60.0,52.0,51.0,52.0,47.0,50.0,56.0,57.0,59.0,55.0,57.0,49.0,65.0,58.0,60.0,52.0,67.0,65.0,66.0,54.0,57.0,58.0,60.0,53.0,56.0,47.0,59.0,50.0,54.0,63.0,50.0,54.0,52.0,58.0,57.0,63.0,57.0,59.0,58.0,56.0,55.0,61.0,62.0,53.0,47.0,60.0,54.0,63.0,61.0,62.0,53.0,63.0,55.0,63.0,65.0,62.0,61.0,58.0,53.0,65.0,65.0,65.0,50.0,56.0,54.0,62.0,63.0,58.0,63.0,47.0,52.0,53.0,60.0,48.0,51.0,58.0,59.0,56.0,52.0,54.0,58.0,54.0,54.0,58.0,63.0,57.0,60.0,55.0,55.0,51.0,42.0,54.0,57.0,51.0,58.0,46.0,58.0,56.0,56.0,62.0,66.0,60.0,62.0,52.0,65.0,58.0,57.0,52.0,54.0,57.0,56.0,59.0,63.0,60.0,59.0,56.0,56.0,55.0,59.0,46.0,57.0,54.0,55.0,59.0]
Q_Learning_Rewards_Hard_150=[-448.0,-1797.0,-1092.0,-195.0,-168.0,-331.0,-637.0,-430.0,-470.0,-794.0,-224.0,-83.0,-108.0,-87.0,16.0,-644.0,-719.0,-223.0,14.0,-90.0,-42.0,-339.0,52.0,-208.0,5.0,26.0,-174.0,29.0,-24.0,-85.0,-16.0,39.0,-418.0,32.0,57.0,38.0,-176.0,-311.0,55.0,42.0,41.0,51.0,-690.0,19.0,36.0,-12.0,54.0,47.0,52.0,35.0,23.0,4.0,21.0,36.0,32.0,19.0,37.0,53.0,3.0,12.0,32.0,-6.0,30.0,-2.0,43.0,37.0,-116.0,33.0,34.0,56.0,41.0,-2.0,-38.0,19.0,59.0,28.0,-64.0,31.0,37.0,5.0,48.0,16.0,28.0,18.0,-21.0,-24.0,25.0,55.0,7.0,4.0,17.0,11.0,13.0,13.0,6.0,-88.0,26.0,41.0,-42.0,-35.0,-29.0,57.0,47.0,43.0,54.0,32.0,-34.0,33.0,47.0,14.0,35.0,36.0,35.0,52.0,12.0,15.0,13.0,44.0,22.0,40.0,36.0,-8.0,49.0,0.0,39.0,37.0,20.0,42.0,-7.0,7.0,52.0,35.0,32.0,18.0,7.0,22.0,29.0,8.0,41.0,-29.0,39.0,17.0,10.0,24.0,17.0,14.0,15.0,-16.0,45.0,19.0]
Value_Iteration_Rewards_Hard_500=[-256405.0,-30331.0,-5022.0,-1122.0,-589.0,-1750.0,-707.0,-1543.0,-758.0,-277.0,-1565.0,-551.0,-61.0,-1161.0,-523.0,-17.0,-65.0,-95.0,19.0,38.0,58.0,48.0,58.0,61.0,61.0,48.0,41.0,50.0,59.0,65.0,57.0,58.0,55.0,57.0,56.0,51.0,62.0,44.0,60.0,61.0,65.0,66.0,64.0,66.0,46.0,51.0,60.0,62.0,62.0,53.0,58.0,57.0,49.0,50.0,59.0,58.0,46.0,55.0,61.0,64.0,65.0,48.0,66.0,62.0,61.0,54.0,48.0,57.0,63.0,54.0,57.0,51.0,62.0,55.0,62.0,64.0,59.0,59.0,57.0,54.0,59.0,58.0,62.0,58.0,62.0,55.0,58.0,57.0,55.0,61.0,57.0,58.0,51.0,60.0,67.0,53.0,58.0,51.0,60.0,47.0,56.0,63.0,59.0,62.0,58.0,62.0,55.0,61.0,57.0,52.0,55.0,61.0,55.0,62.0,52.0,65.0,55.0,57.0,51.0,59.0,55.0,55.0,57.0,51.0,65.0,45.0,62.0,62.0,46.0,56.0,53.0,62.0,63.0,53.0,55.0,59.0,51.0,61.0,58.0,53.0,55.0,61.0,60.0,58.0,39.0,52.0,61.0,56.0,49.0,64.0,65.0,60.0,63.0,55.0,61.0,59.0,54.0,49.0,61.0,40.0,51.0,61.0,54.0,51.0,61.0,50.0,59.0,58.0,60.0,58.0,58.0,43.0,55.0,53.0,57.0,60.0,51.0,48.0,58.0,60.0,65.0,60.0,63.0,54.0,55.0,55.0,55.0,58.0,58.0,57.0,53.0,53.0,59.0,44.0,57.0,50.0,60.0,57.0,59.0,60.0,57.0,65.0,49.0,61.0,56.0,51.0,61.0,65.0,54.0,56.0,54.0,50.0,49.0,60.0,58.0,51.0,62.0,57.0,48.0,63.0,58.0,58.0,62.0,64.0,51.0,61.0,56.0,61.0,57.0,52.0,59.0,67.0,61.0,58.0,60.0,55.0,57.0,56.0,56.0,47.0,55.0,55.0,52.0,57.0,56.0,56.0,62.0,52.0,59.0,54.0,48.0,49.0,59.0,62.0,60.0,62.0,55.0,56.0,50.0,55.0,58.0,49.0,52.0,57.0,62.0,58.0,64.0,59.0,58.0,48.0,47.0,49.0,59.0,48.0,63.0,55.0,57.0,64.0,61.0,60.0,52.0,57.0,56.0,60.0,60.0,62.0,54.0,51.0,57.0,62.0,46.0,54.0,53.0,51.0,58.0,61.0,58.0,61.0,64.0,51.0,60.0,54.0,51.0,49.0,51.0,61.0,58.0,55.0,53.0,56.0,55.0,55.0,60.0,59.0,53.0,50.0,60.0,62.0,59.0,60.0,61.0,48.0,58.0,64.0,55.0,59.0,41.0,57.0,55.0,55.0,57.0,59.0,56.0,62.0,48.0,51.0,49.0,56.0,49.0,59.0,55.0,61.0,57.0,51.0,48.0,64.0,58.0,52.0,61.0,54.0,61.0,59.0,60.0,63.0,44.0,59.0,59.0,38.0,59.0,54.0,59.0,54.0,56.0,60.0,65.0,55.0,59.0,50.0,58.0,55.0,51.0,33.0,62.0,57.0,53.0,44.0,62.0,66.0,55.0,56.0,37.0,45.0,64.0,63.0,60.0,54.0,50.0,59.0,52.0,61.0,64.0,61.0,57.0,64.0,61.0,56.0,58.0,53.0,63.0,62.0,58.0,57.0,61.0,55.0,62.0,49.0,55.0,55.0,64.0,58.0,55.0,60.0,53.0,48.0,57.0,61.0,52.0,61.0,59.0,62.0,55.0,57.0,63.0,64.0,53.0,61.0,64.0,64.0,63.0,49.0,51.0,60.0,47.0,50.0,60.0,57.0,60.0,57.0,59.0,56.0,57.0,48.0,66.0,58.0,49.0,59.0,62.0,52.0,61.0,58.0,55.0,60.0,58.0,62.0,55.0,62.0,45.0,50.0,63.0,59.0,57.0,49.0,48.0,61.0,58.0,48.0,60.0,48.0,63.0,50.0,51.0,63.0,63.0,62.0,61.0,62.0,57.0,56.0,57.0,59.0,58.0,61.0,61.0,48.0,55.0,62.0,62.0,56.0,55.0,58.0,57.0,62.0,50.0,58.0,46.0,62.0,59.0,56.0,61.0,59.0]
Policy_Iteration_Rewards_Hard_500=[-161543.0,-85635.0,-6699.0,-810.0,-757.0,-659.0,-1145.0,-1402.0,-1282.0,-807.0,-1223.0,-296.0,-334.0,-533.0,-514.0,31.0,-261.0,-88.0,-60.0,37.0,12.0,49.0,52.0,44.0,64.0,53.0,57.0,55.0,56.0,65.0,54.0,63.0,45.0,61.0,53.0,47.0,58.0,62.0,56.0,58.0,53.0,60.0,50.0,60.0,50.0,66.0,59.0,54.0,62.0,56.0,56.0,51.0,57.0,65.0,58.0,57.0,55.0,55.0,62.0,58.0,59.0,62.0,51.0,55.0,48.0,55.0,52.0,55.0,60.0,55.0,64.0,57.0,55.0,53.0,56.0,58.0,50.0,43.0,60.0,55.0,60.0,47.0,63.0,58.0,51.0,49.0,56.0,55.0,58.0,58.0,62.0,54.0,59.0,59.0,63.0,56.0,54.0,53.0,55.0,64.0,60.0,51.0,63.0,63.0,47.0,55.0,49.0,53.0,57.0,53.0,61.0,57.0,61.0,51.0,63.0,56.0,50.0,61.0,52.0,61.0,50.0,57.0,53.0,53.0,59.0,57.0,54.0,54.0,58.0,50.0,62.0,55.0,64.0,66.0,64.0,51.0,54.0,63.0,59.0,55.0,57.0,56.0,60.0,56.0,60.0,56.0,57.0,58.0,57.0,61.0,64.0,58.0,48.0,58.0,66.0,50.0,51.0,64.0,56.0,56.0,53.0,63.0,63.0,57.0,49.0,57.0,46.0,67.0,51.0,58.0,63.0,55.0,59.0,61.0,51.0,49.0,51.0,57.0,59.0,57.0,55.0,63.0,56.0,61.0,59.0,51.0,59.0,62.0,50.0,55.0,56.0,53.0,59.0,65.0,60.0,56.0,61.0,64.0,56.0,61.0,55.0,44.0,65.0,51.0,60.0,58.0,60.0,51.0,50.0,62.0,58.0,54.0,60.0,61.0,52.0,62.0,62.0,54.0,54.0,58.0,58.0,56.0,53.0,49.0,59.0,61.0,63.0,61.0,55.0,50.0,60.0,55.0,60.0,56.0,62.0,54.0,59.0,56.0,60.0,59.0,62.0,62.0,56.0,65.0,59.0,63.0,61.0,56.0,61.0,51.0,60.0,51.0,62.0,64.0,64.0,64.0,56.0,52.0,62.0,57.0,45.0,53.0,60.0,53.0,60.0,47.0,63.0,46.0,52.0,61.0,51.0,65.0,61.0,60.0,51.0,58.0,63.0,67.0,63.0,60.0,58.0,47.0,57.0,56.0,55.0,49.0,59.0,60.0,63.0,57.0,47.0,63.0,54.0,63.0,61.0,55.0,64.0,64.0,56.0,53.0,48.0,57.0,63.0,52.0,59.0,61.0,49.0,52.0,57.0,56.0,51.0,55.0,55.0,54.0,60.0,64.0,55.0,59.0,64.0,59.0,58.0,64.0,58.0,66.0,59.0,59.0,61.0,54.0,57.0,63.0,61.0,62.0,39.0,49.0,51.0,60.0,62.0,58.0,62.0,61.0,59.0,59.0,53.0,59.0,63.0,61.0,56.0,61.0,52.0,64.0,54.0,50.0,60.0,63.0,56.0,50.0,64.0,59.0,61.0,51.0,63.0,40.0,49.0,57.0,54.0,63.0,63.0,55.0,58.0,56.0,51.0,65.0,54.0,65.0,58.0,61.0,60.0,50.0,68.0,62.0,60.0,50.0,65.0,61.0,56.0,62.0,55.0,61.0,56.0,62.0,55.0,46.0,59.0,58.0,58.0,61.0,56.0,62.0,53.0,63.0,48.0,53.0,59.0,52.0,51.0,59.0,59.0,59.0,54.0,48.0,54.0,61.0,49.0,56.0,61.0,63.0,60.0,61.0,59.0,53.0,52.0,58.0,66.0,48.0,57.0,49.0,61.0,62.0,65.0,56.0,56.0,48.0,64.0,48.0,63.0,53.0,65.0,63.0,61.0,51.0,52.0,61.0,49.0,60.0,60.0,47.0,52.0,49.0,48.0,62.0,49.0,61.0,62.0,59.0,62.0,60.0,62.0,60.0,58.0,50.0,55.0,55.0,63.0,52.0,55.0,55.0,61.0,59.0,58.0,52.0,49.0,52.0,53.0,57.0,61.0,63.0,64.0,59.0,64.0,44.0,61.0,49.0,56.0,61.0,59.0,59.0,55.0,57.0,62.0,64.0,62.0,55.0,51.0,62.0,53.0,63.0,60.0,61.0,65.0,53.0]
Q_Learning_Rewards_Hard_500=[-267.0,-1899.0,-748.0,-1600.0,-36.0,-407.0,-276.0,-483.0,-181.0,-115.0,-50.0,-106.0,-123.0,-288.0,-288.0,-578.0,-394.0,-67.0,26.0,-88.0,-153.0,-59.0,2.0,-65.0,-222.0,-24.0,-10.0,-27.0,-162.0,-8.0,-259.0,-2.0,-252.0,-32.0,-55.0,-67.0,-1.0,28.0,25.0,8.0,36.0,-14.0,-12.0,39.0,4.0,54.0,50.0,19.0,47.0,-158.0,45.0,51.0,-17.0,10.0,19.0,35.0,53.0,45.0,26.0,39.0,44.0,31.0,53.0,25.0,17.0,-237.0,25.0,39.0,5.0,-139.0,36.0,24.0,7.0,39.0,-37.0,-13.0,-52.0,0.0,17.0,46.0,4.0,-15.0,41.0,57.0,-47.0,41.0,32.0,49.0,33.0,-23.0,49.0,33.0,34.0,51.0,16.0,42.0,2.0,37.0,16.0,-128.0,53.0,35.0,12.0,37.0,17.0,13.0,-1.0,13.0,3.0,12.0,-70.0,-39.0,8.0,45.0,-76.0,19.0,-17.0,46.0,19.0,21.0,52.0,13.0,36.0,37.0,39.0,22.0,-355.0,-35.0,-15.0,35.0,-17.0,13.0,48.0,43.0,-23.0,46.0,46.0,18.0,0.0,36.0,-73.0,-35.0,22.0,57.0,56.0,-22.0,24.0,41.0,35.0,51.0,50.0,-10.0,-16.0,28.0,12.0,44.0,32.0,-40.0,23.0,58.0,-26.0,-13.0,5.0,9.0,34.0,21.0,38.0,33.0,37.0,-68.0,29.0,27.0,-9.0,16.0,37.0,29.0,-9.0,2.0,8.0,40.0,-83.0,37.0,54.0,-87.0,47.0,-10.0,35.0,25.0,25.0,7.0,46.0,35.0,19.0,-10.0,-34.0,-9.0,-57.0,19.0,42.0,12.0,4.0,-25.0,-23.0,53.0,-212.0,19.0,8.0,-10.0,56.0,45.0,-18.0,-5.0,33.0,17.0,-15.0,46.0,-73.0,43.0,34.0,47.0,40.0,20.0,-4.0,35.0,2.0,40.0,30.0,-14.0,-45.0,48.0,9.0,55.0,-38.0,36.0,30.0,26.0,-7.0,-10.0,22.0,-50.0,40.0,-28.0,-12.0,36.0,29.0,19.0,11.0,54.0,33.0,-48.0,11.0,21.0,-55.0,40.0,-7.0,-45.0,0.0,15.0,37.0,47.0,64.0,-49.0,17.0,-105.0,-11.0,-35.0,33.0,56.0,20.0,-153.0,22.0,47.0,-28.0,-58.0,-5.0,44.0,8.0,-36.0,-82.0,34.0,44.0,-26.0,56.0,34.0,30.0,25.0,50.0,56.0,53.0,30.0,-5.0,40.0,-14.0,45.0,48.0,-13.0,6.0,-8.0,29.0,-170.0,-32.0,49.0,16.0,16.0,13.0,-54.0,24.0,9.0,-3.0,12.0,-26.0,-151.0,33.0,4.0,-16.0,25.0,28.0,23.0,60.0,14.0,46.0,26.0,33.0,35.0,-18.0,55.0,30.0,-8.0,30.0,31.0,20.0,24.0,39.0,56.0,43.0,-14.0,52.0,31.0,0.0,22.0,25.0,39.0,39.0,26.0,30.0,45.0,2.0,25.0,42.0,49.0,29.0,-23.0,-12.0,26.0,-1.0,-23.0,23.0,19.0,39.0,47.0,46.0,-15.0,41.0,12.0,19.0,52.0,41.0,44.0,30.0,-60.0,35.0,42.0,34.0,-5.0,-17.0,52.0,35.0,22.0,37.0,42.0,-276.0,27.0,42.0,45.0,47.0,-45.0,20.0,-48.0,17.0,7.0,-24.0,52.0,37.0,9.0,23.0,6.0,11.0,0.0,43.0,5.0,5.0,13.0,7.0,-56.0,-87.0,26.0,39.0,28.0,22.0,-34.0,33.0,11.0,-22.0,30.0,42.0,-1.0,14.0,17.0,35.0,-15.0,14.0,29.0,35.0,37.0,49.0,46.0,-43.0,47.0,30.0,-103.0,-206.0,-88.0,41.0,8.0,14.0,-1.0,19.0,18.0,31.0,38.0,26.0,-29.0,-14.0,12.0,51.0,36.0,22.0,45.0,7.0,18.0,49.0,-15.0,13.0,39.0,-2.0,38.0,17.0,-43.0,-137.0,15.0,38.0,32.0,-75.0,6.0,-3.0,52.0,-2.0,48.0,-6.0,-186.0,14.0,10.0,45.0,53.0,-3.0,55.0,41.0,41.0,31.0,-7.0,36.0,24.0,7.0,31.0,9.0,47.0,20.0,8.0,-88.0,23.0,-23.0,17.0,33.0,-22.0,15.0,56.0,33.0,-324.0,-10.0,44.0]

print(max(Value_Iteration_Rewards_Easy_100))
print(max(Policy_Iteration_Rewards_Easy_100))
print(max(Q_Learning_Rewards_Easy_100))
print(max(Value_Iteration_Rewards_Hard_500)-100)
print(max(Policy_Iteration_Rewards_Hard_500)-100)
print(max(Q_Learning_Rewards_Hard_500)-100)

plt.plot(Iterations_150, Value_Iteration_Hard_150, label="Value Iteration")
plt.plot(Iterations_150, Policy_Iteration_Hard_150, label="Policy Iteration")
plt.plot(Iterations_150, Q_Learning_Hard_150, label="Q_Learning")
plt.xlabel('Iterations')
plt.ylabel('Steps/Actions')
plt.title('Hard Grid Actions vs. Iterations')
plt.ylim(top=500,bottom=0)
plt.legend()
plt.show()

plt.plot(Iterations_150, Value_Iteration_Time_Hard_150, label="Value Iteration")
plt.plot(Iterations_150, Policy_Iteration_Time_Hard_150, label="Policy Iteration")
plt.plot(Iterations_150, Q_Learning_Time_Hard_150, label="Q_Learning")
plt.xlabel('Iterations')
plt.ylabel('Time in Milliseconds')
plt.title('Hard Grid Time vs. Iterations')
plt.legend()
plt.show()

plt.plot(Iterations_150, Value_Iteration_Rewards_Hard_150, label="Value Iteration")
plt.plot(Iterations_150, Policy_Iteration_Rewards_Hard_150, label="Policy Iteration")
plt.plot(Iterations_150, Q_Learning_Rewards_Hard_150, label="Q_Learning")
plt.xlabel('Iterations')
plt.ylabel('Total Reward Gained')
plt.title('Hard Grid Total Reward Gained vs. Iterations')
plt.ylim(top=100,bottom=-300)
plt.legend()
plt.show()