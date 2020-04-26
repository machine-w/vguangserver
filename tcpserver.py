# 导入socket库:
import socket,time,threading
import uuid

# 创建一个socket: 
# AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
vguangs={}
# 监听端口:
s.bind(('0.0.0.0', 1984))
s.listen(5)
print('#################等待链接#####################')

#发送函数
def sendCmd(devId,cmd):
    # cmd = bytes.fromhex('55AA29010000D7')
    vguangs[devId][0].send(cmd)

#处理函数
def recvData(devId,sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    # sock.send(b'Welcome!')
    
    while True:
        data = sock.recv(1024)
        # print(data[:6],data[6:-1])
        content = data[6:-1].decode('utf-8')
        print(content)

        if len(content) !=0:
            cmd = bytes.fromhex('55AA0405000F03505000F2')
            sendCmd(devId,cmd)
        # sock.send(data)
        # time.sleep(1)
        # if not data or data.decode('utf-8') == 'exit':
        #     break
        # sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
try:
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        devId = str(uuid.uuid4())
        vguangs[devId]=(sock, addr)
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=recvData, args=(devId,sock, addr))
        t.start()
finally:
    print('#################结束任务#####################')
    s.close()
    for devId in vguangs:
        vguangs[devId][0].close()
    
