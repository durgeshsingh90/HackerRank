n=int(input())

def name():
    o=[]
    e=[]
    for i in range(len(a)):
        if i%2==0:
            e.append(a[i])
            
        else:
            o.append(a[i])
    print (''.join(e) +' '+ ''.join(o))

for i in range(n):
    a=input()
    name()
