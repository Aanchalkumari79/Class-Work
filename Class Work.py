f=open('text1.txt','a')
f.writelines(["suman\n","smuit\n"])
f.close()
g=open('text1.txt','r')
print(g.read())

print(g.read(5))
print(g.read(10))

print(g.read(5))
g.seek(0)
print(g.read(10))