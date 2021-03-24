from sshtunnel import SSHTunnelForwarder
import redis

server = SSHTunnelForwarder(
    '192.168.0.100', # 服务器域名或IP
    ssh_username="root", # ssh 用户
    ssh_password="password", # ssh 密码
    remote_bind_address=('0.0.0.0', 6379) # 远程绑定的地址及端口
)

server.start()

# 像往常一样使用 redis
print(server.local_bind_port)

r=redis.Redis(
    host='127.0.0.1', # 本地地址
    port=server.local_bind_port, # 穿透后的本地端口
    decode_responses=True
)
k = 'key_name'
r.set(k, '值')
print(r.get(k))
r.delete(k)

server.stop()
