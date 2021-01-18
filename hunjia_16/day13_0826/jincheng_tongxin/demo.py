import multiprocessing as mp


def send(conn, data):
    conn.send(["百度网址", "www.baidu.com", data])


def receive(conn):
    print("接收数据：", conn.recv() )


if __name__ == '__main__':
    conn_rec, conn_send = mp.Pipe()  # 管道分为接收和发送
    # 创建俩子进程
    pro_send = mp.Process(target=send, args=(conn_send, "www.baidu.com"))
    pro_rec = mp.Process(target=receive, args=(conn_rec,))
    pro_rec.start()
    pro_send.start()
