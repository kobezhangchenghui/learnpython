#!/usr/bin/python
#-*- coding: utf-8 -*-
import paramiko


def login(ip, username, passwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
    except:
        print('%s\tError\n' % ip)


def runCmd(ip, username, passwd, cmd):
    result = []
    sshclient = login(ip, username, passwd)
    channel = sshclient.invoke_shell()
    for m in cmd:
        if m == None:
            continue
        channel.send(m+"\n")
        result.append(channel.recv(4096))
    return result


if __name__ == "__main__":
    cmd = ["su - root", "$passwd", "mkdir -p /zhang"]
    ip = "$ip"
    username = "$user"
    passwd = "$passwd"
    runCmd(ip, username, passwd, cmd)
