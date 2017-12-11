#import json

ys = {}

ys["honoka"] = {"B": 78, "W": 58, "H": 82}
ys["eri"]    = {"B": 88, "W": 60, "H": 84}
ys["kotori"] = {"B": 80, "W": 58, "H": 80}
ys["umi"]    = {"B": 76, "W": 58, "H": 80}
ys["rin"]    = {"B": 75, "W": 59, "H": 80}
ys["maki"]   = {"B": 78, "W": 56, "H": 83}
ys["nozomi"] = {"B": 90, "W": 60, "H": 82}
ys["hanayo"] = {"B": 82, "W": 60, "H": 83}
ys["niko"]   = {"B": 74, "W": 57, "H": 79}

print(ys)
#出力：{'nozomi': {'H': 82, 'B': 90, 'W': 60}, 'umi': {'H': 80, 'B': 76, 'W': 58}, 'niko': {'H': 79, 'B': 74, 'W': 57}, 'kotori': {'H': 80, 'B': 80, 'W': 58}, 'maki': {'H': 83, 'B': 78, 'W': 56}, 'eri': {'H': 84, 'B': 88, 'W': 60}, 'hanayo': {'H': 83, 'B': 82, 'W': 60}, 'rin': {'H': 80, 'B': 75, 'W': 59}, 'honoka': {'H': 82, 'B': 78, 'W': 58}}

print(ys["rin"]["W"])
#出力：59