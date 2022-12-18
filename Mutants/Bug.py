Type = "Thing"
Name = "Bug"
Info = {
  'hit points': "400",
  'reaction time': "8",
  'pain chance': "128",
  'speed': "8",
  'width': "2031616",
  'height': "3670016",
  'mass': "400",
  'attack sound': "55",
}
Frames = (
  {'sprite number':"40",'sprite subnumber': "0",'duration':"15",'action pointer':      "Look",'next frame': 1},
  {'sprite number':"40",'sprite subnumber': "1",'duration':"15",'action pointer':      "Look",'next frame': 0},
  {'sprite number':"40",'sprite subnumber': "0",'duration': "3",'action pointer':     "Chase",'next frame': 3},
  {'sprite number':"40",'sprite subnumber': "0",'duration': "3",'action pointer':     "Chase",'next frame': 4},
  {'sprite number':"40",'sprite subnumber': "1",'duration': "3",'action pointer':     "Chase",'next frame': 5},
  {'sprite number':"40",'sprite subnumber': "1",'duration': "3",'action pointer':     "Chase",'next frame': 6},
  {'sprite number':"40",'sprite subnumber': "2",'duration': "3",'action pointer':     "Chase",'next frame': 7},
  {'sprite number':"40",'sprite subnumber': "2",'duration': "3",'action pointer':     "Chase",'next frame': 8},
  {'sprite number':"40",'sprite subnumber': "3",'duration': "3",'action pointer':     "Chase",'next frame': 9},
  {'sprite number':"40",'sprite subnumber': "3",'duration': "3",'action pointer':     "Chase",'next frame': 2},
  {'sprite number':"40",'sprite subnumber': "4",'duration': "5",'action pointer':"FaceTarget",'next frame':11},
  {'sprite number':"40",'sprite subnumber': "5",'duration': "5",'action pointer':"FaceTarget",'next frame':12},
  {'sprite number':"40",'sprite subnumber': "6",'duration': "5",'action pointer':'HeadAttack','next frame': 2},
  {'sprite number':"40",'sprite subnumber': "7",'duration': "5",'action pointer':"FaceTarget",'next frame':14},
  {'sprite number':"40",'sprite subnumber': "8",'duration': "5",'action pointer':"FaceTarget",'next frame':15},
  {'sprite number':"40",'sprite subnumber': "9",'duration': "5",'action pointer':'HeadAttack','next frame': 2},
  {'sprite number':"40",'sprite subnumber':"10",'duration': "3",                              'next frame':17},
  {'sprite number':"40",'sprite subnumber':"10",'duration': "3",'action pointer':      "Pain",'next frame':18},
  {'sprite number':"40",'sprite subnumber':"10",'duration': "6",                              'next frame': 2},
  {'sprite number':"40",'sprite subnumber':"11",'duration': "8",                              'next frame':20},
  {'sprite number':"40",'sprite subnumber':"12",'duration': "8",'action pointer':    "Scream",'next frame':21},
  {'sprite number':"40",'sprite subnumber':"13",'duration': "8",                              'next frame':22},
  {'sprite number':"40",'sprite subnumber':"14",'duration': "8",                              'next frame':23},
  {'sprite number':"40",'sprite subnumber':"15",'duration': "8",                              'next frame':24},
  {'sprite number':"40",'sprite subnumber':"16",'duration': "8",                              'next frame':25},
  {'sprite number':"40",'sprite subnumber':"17",'duration': "8",                              'next frame':26},
  {'sprite number':"40",'sprite subnumber':"18",'duration': "8",'action pointer':      "Fall",'next frame':27},
  {'sprite number':"40",'sprite subnumber':"19",'duration':"-1",                              'next frame':""}
)
States = {
  'initial frame': 0,
  'first moving frame': 3,
  'far attack frame': 11,
  'close attack frame': 14,
  'injury frame': 17,
  'death frame': 20
}
Flags = {
  "SOLID",
  "SHOOTABLE",
  "FLOAT",
  "NOGRAVITY",
  "COUNTKILL"
}
