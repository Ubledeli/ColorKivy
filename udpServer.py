import socket, json
port = 25000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", port))
print("waiting on port:", port)
while 1:
	binary, addr = s.recvfrom(1024)
	try:
		json_lst = json.loads(binary.decode())
		print(json_lst,type(json_lst))
		for i,j in enumerate(json_lst):
			print(i,json_lst[i])
	except:
		print('puko json')
