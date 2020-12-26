import socket as s
host=input()
print(f"IP of {host} is {s.gethostbyname(host)}")