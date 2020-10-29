"""
select io 多路复用
"""

from socket import *
from select import select
from time import sleep

# 创建三个对象，帮助监控
tcp_sock = socket()
tcp_sock.bind(('0.0.0.0',8888))
tcp_sock.listen(5)
print(tcp_sock)

udp_sock = socket(AF_INET,SOCK_DGRAM)
udp_sock.bind(('0.0.0.0',8866))

f = open("my.log",'rb')

# 开始监控这些IO
print("监控IO发生")
sleep(5)
# tcp_sock:监听套接字（只负责连接）　只有读事件    udp_sock:连接套接字
rs,ws,xs = select([tcp_sock],[f,udp_sock],[])
print("rs :",rs)
print("ws :",ws)
print("xs :",xs)