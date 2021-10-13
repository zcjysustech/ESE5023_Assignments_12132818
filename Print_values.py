def Print_values(a,b,c):
    if(a>b):
        if(b>c):
            print(a,b,c)
            return
        else:
            if(a>c):
                print(a,c,b)
                return
            else:
                print(c,a,b)
                return
    else:
        if(b>c):
            if (a > c):
                print(b, a, c)
                return
            else:
                print(b, c, a)
                return
        else:
            print(c,b,a)
            return

if __name__=="__main__":
    a=int(input())
    b=int(input())
    c=int(input())
    Print_values(a,b,c)
