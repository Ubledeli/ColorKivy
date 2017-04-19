import socket
import json, time
from machine import Pin, PWM, ADC
# B, R, G, 12v, B, R, G, 12v W, 12v W, 12v
pwm = [14,12,13,15,2,4,5]
pins = [PWM(Pin(i)) for i in pwm]
#adc = ADC(0)

def setup_server(address):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(address)
	return s

def run_server(s):
	while True:
		data, address= s.recvfrom(1024)
		try:
			data = json.loads(data.decode())
			for i,p in enumerate(pins):
				p.duty(data[i])
		except:
			s.sendto(data,address)

def test():
	s = setup_server(('',25000))
	run_server(s)

if __name__ == '__main__':
	test()
