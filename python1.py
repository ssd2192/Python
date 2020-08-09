print("hello");
x=[1,2,3,4]
print(x)
print(type(x))
print(min(x))
print(max(x))

age= 16
name="Jane"
print(type(name))
print(type(age))


"""for string%s, for integer %d"""
print("Name=%s, Age=%d"%(name,age))

s1='single quotes'
s2="double quotes"
s3='''triple single quote line 1
    triple single quote line 2
    triple single quote line 3'''
print(s1)
print(s2)
print(s3)
print(s1+s2)
print(s1[0])
print(s1[0:6])
print(s1[-2])
print(len(s1))

x='1'
y='2'
print(x+y)
print(int(x)+int(y))
print(x+str(2))

"""tuple examples"""

t=("abc",245,'g')
print(t)

tp1=(1,2,3)
print (tp1[0])
"""tp1[0]=11  this is not possible in tuple"""
print(tp1)

""" list"""
g=[1,2,3,4]
print(g)
g[0]=10
print(g)

print(len(g))

"""dictionary"""

d1={"CANADA":"OTTAWA", "INDIA":" NEW DELHI"}
print(d1["CANADA"])
print(type(d1))
print(d1.keys())
print(d1.values())

"""LOOPS"""
"while loop"
i=0
while(i<=10):
    print(i)
    i+=1;
print("\n")

"for loop"
for j in range(0,11):
    print(j);
    
"dictionary example"
my_name={"Mahsa":29, "Sandy":25, "Anjali":21, "Sukh":20}
name=input("Enter your name")
if(name in my_name.keys()):
    print("Age is:%d" %my_name[name])
else: print("key %s doesn't exist" %name)


























    



