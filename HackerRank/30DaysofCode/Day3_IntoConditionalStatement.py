def check(value):
    if n%2!=0:
        return ('Weird')
    elif n%2==0 and (2<=n<=5):
        return ('Not Weird')
    elif n%2==0 and (6<=n<=20):
        return ('Weird')
    elif n%2==0 and (n>20):
        return ('Not Weird')


if __name__ == '__main__':
    n = int(input())
    a=check(n)
    print (a)
