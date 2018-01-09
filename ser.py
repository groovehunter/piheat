import serial
import json


ser = serial.Serial('/dev/ttyACM1', 9600)

while 1:
    #print("next")
    res = ser.readline()
#   print(res)
    print("next")
    print(res)
    #
    j = json.loads(res.decode('utf-8'))
    #json.prettyprint(j)
    json.dumps(j)

    


