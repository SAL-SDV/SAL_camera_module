import paramiko
import scp as scp

#ここでは自前のラズパイでテスト
hostname = '192.168.11.17'
port = 22
username = 'pi'
#keyfile = '.ssh/id_rsa'
password = 'raspberry'
rsa_key = paramiko.RSAKey.from_private_key_file(keyfile)

#動画の転送
def send(path):
    #sshを用いて親機へファイルを転送
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,password)　#パス認証方式
        #ssh.connect(hostname,port,username,pkey=rsa_key) #秘密鍵方式
        with scp.SCPClient(ssh.get_transport()) as scp2:
            scp2.put(path,'/home/pi/SAL_Web_master/media/movie')
    print("rest")

if __name__ == '__main__':
  print("import only")
