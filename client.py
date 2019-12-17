#!/usr/bin/env python

import socket
import json
import collections
from solution import get_sensor_id, calculate_position, get_team_id

SENSOR_IP = 'nvc2835'
SENSOR_PORT = 9000
BUFFER_SIZE = 1024

START = "<start>"
END = "<end>"

MAP_IP = 'nvc2835'
MAP_PORT = 8000

Beacon = collections.namedtuple('Beacon', ['id', 'x', 'y', 'z'])

BEACON1 = Beacon(id=0, x=2250, y=2000, z=0)
BEACON2 = Beacon(id=11, x=1450, y=1900, z=0)
BEACON3 = Beacon(id=17, x=1400, y=700, z=0)
BEACON4 = Beacon(id=6, x=2500, y=1200, z=0)

beacon_with_rssi = collections.namedtuple('beacon_with_rssi', ['beacon', 'rssi'])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SENSOR_IP, SENSOR_PORT))

m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m.connect((MAP_IP, MAP_PORT))

buffer = "" 
while True:
  #print("Wait for sensor data....")
  data = s.recv(BUFFER_SIZE)
  #print("Sensor data received", data)
  buffer += data.decode("utf-8") 
  index = buffer.index(START)
  if(index >= 0):
    #index += len(START)
    buffer = buffer[index:]
  else:
    buffer = "";
    continue
    
  lines = buffer.split("\n")
  #print(buffer)
  for line in lines:
    buffer = ""
    if(line.endswith(END)):
      line = line.replace(START, "")
      line = line.replace(END, "")
      sensor = json.loads(line)
      sensor_id = sensor["sensorId"]
      beacons = sensor["beacons"]
      #print(line)
      if sensor_id == get_sensor_id():
        beacon_list = []
        for beacon in beacons:
          beacon_list.insert(int(beacon["beaconId"]), beacon["rssi"])
        #print sensor_id + ": ", beacon_list
        #print line

        b1 = beacon_with_rssi(beacon=BEACON1, rssi=beacon_list[BEACON1.id])
        b2 = beacon_with_rssi(beacon=BEACON2, rssi=beacon_list[BEACON2.id])
        b3 = beacon_with_rssi(beacon=BEACON3, rssi=beacon_list[BEACON3.id])
        b4 = beacon_with_rssi(beacon=BEACON4, rssi=beacon_list[BEACON4.id])
        x,y,z = calculate_position(b1, b2, b3, b4)

        x = int(x)
        y = int(y)

        print("Sent position to map: " + str(x) + "," + str(y))
        m.send((get_team_id() + "," + str(x) + "," + str(y) + "\n").encode("utf-8"))
        print("Position sent to map")
        print("Wait for okay from map")
        data = m.recv(BUFFER_SIZE)
        print("Received result from map: " , data.decode("utf-8"))
    else:
      buffer = line;
s.close()
m.close();
