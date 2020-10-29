"""
基于多线程的 tcp 网络并发模型
重点代码！！
"""
from socket import *
from threading import Thread

# 全局变量
HOST = '0.0.0.0'
PORT = 8888
ADDR =  (HOST,PORT) #  服务器地址

# 处理客户端请求
class MyThread(Thread):
    def __init__(self,connfd):
        super().__init__()
        self.connfd = connfd

    def run(self):
        while True:
            data = self.connfd.recv(1024)
            # 另外一端不存在了，recv会返回空字节
            if not data:
                break
            print("Recv:",data.decode())
            self.connfd.send(b"Thanks")
        self.connfd.close()

def main():
    # tcp套接字创建
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)
    print("Listen the port %s"%PORT)

    # 循环连接客户端
    while True:
        try:
            connfd,addr = sock.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sock.close()
            return
        # 为连接进来的客户端创建单独的线程
        t = MyThread(connfd) # 使用自定义线程类创建线程
        t.setDaemon(True) # 主线程退出，分之线程终止服务
        t.start()

if __name__ == '__main__':
    main()







