import socket, json, random


class UdpClient:
    server_address = ('192.168.0.16',25000)
    data1 = [round(random.random()*1023) for i in range(7)]
    data1 = [1023-i for i in data1]
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    nodes = set()

    def __init__(self, s_addr=server_address):
        self.s_addr = s_addr
        UdpClient.nodes.add(s_addr)

    def jsend(self, data):
        b = json.dumps(data).encode()
        UdpClient.s.sendto(b, self.s_addr)

    def test(self):
        #s = self.setup_connection(self.s_addr)
        #self.jsend(s,self.data1)
        pass

if __name__ == '__main__':
	UdpClient().test()
