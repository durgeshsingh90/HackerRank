def table(n):
    for i in range(1,11):
        print (str(n) + ' x '+str(i) + ' = ' + str(n*i))


if __name__ == '__main__':
    n = int(input())
    table(n)
