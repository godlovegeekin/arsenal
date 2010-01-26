#!/usr/bin/env python
# Hankaku_V.py
IS_VERTICAL = True
CODE2CID = {32: 231, 33: 232, 34: 233, 35: 234, 36: 235, 37: 236, 38: 237, 39: 238, 40: 239, 41: 240, 42: 241, 43: 242, 44: 243, 45: 244, 46: 245, 47: 246, 48: 247, 49: 248, 50: 249, 51: 250, 52: 251, 53: 252, 54: 253, 55: 254, 56: 255, 57: 256, 58: 257, 59: 258, 60: 259, 61: 260, 62: 261, 63: 262, 64: 263, 65: 264, 66: 265, 67: 266, 68: 267, 69: 268, 70: 269, 71: 270, 72: 271, 73: 272, 74: 273, 75: 274, 76: 275, 77: 276, 78: 277, 79: 278, 80: 279, 81: 280, 82: 281, 83: 282, 84: 283, 85: 284, 86: 285, 87: 286, 88: 287, 89: 288, 90: 289, 91: 290, 92: 291, 93: 292, 94: 293, 95: 294, 96: 231, 97: 296, 98: 297, 99: 298, 100: 299, 101: 300, 102: 301, 103: 302, 104: 303, 105: 304, 106: 305, 107: 306, 108: 307, 109: 308, 110: 309, 111: 310, 112: 311, 113: 312, 114: 313, 115: 314, 116: 315, 117: 316, 118: 317, 119: 318, 120: 319, 121: 320, 122: 321, 123: 322, 124: 323, 125: 324, 126: 325, 129: 327, 130: 328, 131: 329, 132: 330, 133: 331, 134: 516, 135: 517, 136: 518, 137: 519, 138: 520, 139: 521, 140: 522, 141: 523, 142: 524, 143: 525, 144: 342, 145: 526, 146: 527, 147: 528, 148: 529, 149: 530, 150: 531, 151: 532, 152: 533, 153: 534, 154: 535, 155: 536, 156: 537, 157: 538, 158: 539, 159: 540, 161: 327, 162: 328, 163: 329, 164: 330, 165: 331, 166: 332, 167: 333, 168: 334, 169: 335, 170: 336, 171: 337, 172: 338, 173: 339, 174: 340, 175: 341, 176: 342, 177: 343, 178: 344, 179: 345, 180: 346, 181: 347, 182: 348, 183: 349, 184: 350, 185: 351, 186: 352, 187: 353, 188: 354, 189: 355, 190: 356, 191: 357, 192: 358, 193: 359, 194: 360, 195: 361, 196: 362, 197: 363, 198: 364, 199: 365, 200: 366, 201: 367, 202: 368, 203: 369, 204: 370, 205: 371, 206: 372, 207: 373, 208: 374, 209: 375, 210: 376, 211: 377, 212: 378, 213: 379, 214: 380, 215: 381, 216: 382, 217: 383, 218: 384, 219: 385, 220: 386, 221: 387, 222: 388, 223: 389, 224: 541, 225: 542, 226: 543, 227: 544, 228: 545, 229: 546, 230: 547, 231: 548, 232: 549, 233: 550, 234: 551, 235: 552, 236: 553, 237: 554, 238: 555, 239: 556, 240: 557, 241: 558, 242: 559, 243: 560, 244: 561, 245: 562, 246: 563, 247: 564, 248: 565, 249: 566, 250: 567, 251: 568, 252: 569, 253: 570, 254: 388, 255: 389}
