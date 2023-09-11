#!/usr/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("IP:")
host = str(input())

print("PORT:")
port = int(input())



def porthawk(port):
    if s.connect_ex((host, port)):
        print(port)
        print("closed")
    else:
        print(port)
        print("opened")
        

print("PORT HAWK| | |Made by superkar Bedr")

porthawk(port)

