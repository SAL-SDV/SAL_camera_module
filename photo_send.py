# coding:utf-8
import paramiko
import scp as scp

#ホームモジュールの情報
hostname = '192.168.90.29'
port = 22
username = 'pi'
password = 'raspberry'
#keyfile = '.ssh/id_rsa'

#rsa_key = paramiko.RSAKey.from_private_key_file(keyfile)

#画像の転送
def send(path):
    #sshを用いて親機へファイルを転送
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,password)
        with scp.SCPClient(ssh.get_transport()) as scp2:
            scp2.put(path,'/home/pi/SAL_Web-master/media/movie')
    print("rest")

if __name__ == '__main__':
  print("import only")
