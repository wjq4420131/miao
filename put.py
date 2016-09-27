# -*- coding:utf8 -*-...
import paramiko
import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="123456",
    db="core",
    charset="utf8"
    )
cur = conn.cursor()


def get_ip():
    sql = "select ipaddr,username,pwd,port_num from waring"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        hostname=row[0]
        username=row[1]
        password = row[2]
        port = row[3]
        put_file(hostname, username, password,port)

def put_file(hostname, username, password,port):
    try:
        t = paramiko.Transport((hostname,port))
        t.connect(username=username,password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put("55.sh","/home/55.sh")
        print "上传成功"
            
    except Exception,e:
        print e 

if __name__=="__main__":
    get_ip()