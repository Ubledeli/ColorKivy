import socket
import json
#pins=[2,14,4,5,12,13,15]
try:
	from machine import Pin, PWM, ADC
	pwm2 = PWM(Pin(2))
	pwm1r = PWM(Pin(14))
	pwm1g = PWM(Pin(4))
	pwm1b = PWM(Pin(5))
	pwm2r = PWM(Pin(12))
	pwm2g = PWM(Pin(13))
	pwm2b = PWM(Pin(15))
	adc = ADC(0)
	
except:
	print('no module named machine')
def light(pin,value,inverted=False):
		if value < 0:
			value = 0
		if value > 1023:
			value = 1023
		if not inverted:
			pin.duty(value)
		else:
			pin.duty(1023-value)

def blink(pin):
	for i in range(3):
		pin.duty(0)
		time.sleep(0.5)
		pin.duty(1023)
		time.sleep(0.5)

def setup_server(address):
	#host = ''
	#port = 25000
	#backlog = 5
	#size = 1024

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	#ai = usocket.getaddrinfo("0.0.0.0", port)
	#addr = ai[0][4]

	s.bind(address)
	#s.listen(5) #samo za tcp
	return s

def run_server(s):
	while True:
		data, address= s.recvfrom(1024)
		print('addr',address)
		print('data', data)
		#s.sendto(data,address)
		data = data.decode()
		try:
			d = json.loads(data)
			#print(d['1r'],d['1g'],d['1b'])
			pwm2.duty(1023-d['led'])
			pwm1r.duty(1023-d['1r'])
			pwm1g.duty(1023-d['1g'])
			pwm1b.duty(1023-d['1b'])
			pwm2r.duty(1023-d['2r'])
			pwm2g.duty(1023-d['2g'])
			pwm2b.duty(1023-d['2b'])
			#print('json uspeo')
		except:
			#print('puko json', data)
			pass

def test():
	s = setup_server(('',25000))
	run_server(s)

if __name__ == '__main__':
	test()
