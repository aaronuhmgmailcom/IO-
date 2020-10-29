"""
基于select 的IO多路复用并发模型
重点代码 ！
"""
from socket import *
from select import select

# 全局变量
HOST = "0.0.0.0"
PORT = 8889
ADDR = (HOST,PORT)

# 创建tcp套接字
tcp_socket = socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)

# 设置为非阻塞
tcp_socket.setblocking(False)

# IO对象监控列表
rlist = [tcp_socket] # 初始监听对象  没有客户端连接
wlist = []
xlist = []

# 循环监听
while True:
    # 对关注的IO进行监控
    rs,ws,xs = select(rlist,wlist,xlist)
    # 对返回值rs 分情况讨论 监听套接字   客户端连接套接字
    for r in rs:
        if r is tcp_socket:
            # 处理客户端连接
            connfd, addr = r.accept()
            print("Connect from", addr)
            connfd.setblocking(False) # 设置非阻塞
            rlist.append(connfd) # 添加到监控列表
        else:
            # 收消息
            data = r.recv(1024)
            if not data:
                # 客户端退出
                rlist.remove(r) # 移除关注
                r.close()
                continue
            print(data.decode())
            # r.send(b'OK')
            wlist.append(r) # 放入写列表　　主动处理

    for w in ws:
        w.send(b"OK") # 发送消息　　写时间
        wlist.remove(w) # 如果不移除会不断的写






