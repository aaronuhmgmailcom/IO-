"""
poll io 多路复用
"""

from socket import *
from select import *
from time import sleep

# 创建三个对象，帮助监控
tcp_sock = socket()
tcp_sock.bind(('0.0.0.0',8888))
tcp_sock.listen(5)

udp_sock = socket(AF_INET,SOCK_DGRAM)
udp_sock.bind(('0.0.0.0',8866))

f = open("my.log",'rb')

# 开始监控这些IO
print("监控IO发生")

p = poll()
# 关注IO事件
p.register(tcp_sock,POLLIN)
p.register(f,POLLOUT)
p.register(udp_sock,POLLOUT|POLLIN)

print("tcp_sock:",tcp_sock.fileno())
print("udp_sock:",udp_sock.fileno())
print("file:",f.fileno())

# 准备工作  {唯一的文件描述符：监控的IO对象}
map = {
       tcp_sock.fileno():tcp_sock,
       udp_sock.fileno():udp_sock,
       f.fileno():f
       }

events = p.poll() # 进行监控
print(events)
print(map)
p.unregister(f) # 取消关注