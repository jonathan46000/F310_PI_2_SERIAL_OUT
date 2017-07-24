#!/usr/bin/python

import serial

ser = serial.Serial('/dev/ttyAMA0',9600,timeout=1)

serial_data = [0,0]

def send_serial_data() :
	ser.write(str(serial_data[0]))
	ser.write("888")
	ser.write(str(serial_data[1]))
	ser.write("999")
	return;

def print_serial_data():
	print(serial_data[0])
	print(serial_data[1])
	return;

def fill_serial_data(code,value):
	if code < 288 :
		if code == 17 :
			if value == 0 :
				serial_data[1] = 0
			elif value == 1 :
				serial_data[0] = 14
				serial_data[1] = 1
			else :
				serial_data[0] = 13
				serial_data[1] = 1
		if code == 16 :
			if value == 0 :
				serial_data[1] = 0
			elif value == 1 :
				serial_data[0] = 16
				serial_data[1] = 1
			else :
				serial_data[0] = 15
				serial_data[1] = 1
		if code < 16 :
			if code == 2 :
				serial_data[0] = 17
			if code == 5 :
				serial_data[0] = 18
			if code == 0 :
				serial_data[0] = 19
			if code == 1 : 
				serial_data[0] = 20
			serial_data[1] = value
	else :
		serial_data[0] = code - 288
		serial_data[1] = value
	return;

from evdev import InputDevice, categorize, ecodes, KeyEvent
gamepad = InputDevice('/dev/input/event3')
print (gamepad)
for event in gamepad.read_loop() :
	if event.code != 4:
		keyevent = categorize(event)
		if keyevent.event.code == 0 :
			if keyevent.event.value != 0 :
				fill_serial_data(keyevent.event.code,keyevent.event.value)
				print_serial_data()
				send_serial_data()			
		else :
			fill_serial_data(keyevent.event.code,keyevent.event.value)
			print_serial_data()
			send_serial_data()
