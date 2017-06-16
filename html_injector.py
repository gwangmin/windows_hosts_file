#-*- encoding: utf-8 -*-

import time

print """
ㅣ  ㅣ ______ ㅣ\\    /ㅣ ㅣ       ㅣ   ㅡㅡ    ㅣ  ___  ___ _____  ___   __
ㅣㅡㅣ   ㅣ    ㅣ \\  / ㅣ ㅣ       ㅣ ㅣ   ㅣ   ㅣ ㅣ__ ㅣ      ㅣ  ㅣ   ㅣㅣ__ㅣ
ㅣ  ㅣ   ㅣ    ㅣ  \\/  ㅣ ㅣ___    ㅣ ㅣ   ㅣ __ㅣ ㅣ__ ㅣ___   ㅣ  ㅣ___ㅣㅣ  \\
"""
while True:
    print """1. Inject
2. Cancel"""
    n=raw_input("Injector> ")
    if n=="1":
        time.sleep(10)
        hosts=open("C:\Windows\System32\drivers\etc\hosts","a")
        hosts.write("127.0.0.1 www.naver.com\n")
    else:
        hosts=open("C:\Windows\System32\drivers\etc\hosts","w")
        hosts.write("")
    hosts.close()
