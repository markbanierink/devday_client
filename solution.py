#!/usr/bin/env python

import random

#Return tag id ex '999-0000-00238068'
def get_sensor_id():
  return '999-0000-00249705'

#Return the team name
def get_team_id():
  return "Team1: " + get_sensor_id()

#b.beacon
#b.rssi
#beacon.id
#beacon.x
#beacon.y
#beacon.z
#Return x,y,z
def calculate_position(b1, b2, b3, b4):
  #What is b1, b2, b3, b4?
  rssiOfB1 = b1.rssi
  beacon_info_of_b2 = b2.beacon
  xOfB2 = beacon_info_of_b2.x
  #or
  xOfB2 = b2.beacon.x
  
  #Difficult math...
  #max screen size 2000cm
  x = random.random() * 2000
  y = 1000
  #z is not used anyway, but a nice to have
  z = 0
  
  return x,y,z
  
