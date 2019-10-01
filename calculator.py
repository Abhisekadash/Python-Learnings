def add(a):
    t=True
    while t:
        b=a.split()
        if len(b)>1:
            c=1
            for x in range(len(b)):
                if int(b[x])!=0 and int(b[x])>0:
                    c=c*int(b[x])
                else:
                    print("Don't enter 0 or negative value")
                    break
            print(c)
        else:
            print("Please enter more then 1 no.")
        n=input("If you Want to Add again Press y:")
        if n=="y":
            t=True
            a=input("Enter another values")
        else:
            t=False
def multiply(a):
    t=True
    while t:
        b=a.split()
        if len(b)>1:
            c=1
            for x in range(len(b)):
                if int(b[x])!=0 and int(b[x])>0:
                    c=c+int(b[x])
                else:
                    print("Don't enter 0 or negative value")
                    break
            print(c)
        else:
            print("Please enter more then 1 no.")
        n=input("If you Want to mulitiply again Press y:")
        if n=="y":
            t=True
            a=input("Enter another values")
        else:
            t=False
def subst(a):
    t=True
    while t:
        b=a.split()
        if len(b)==2:
            c=0
            for x in range(len(b)-1):
                if int(b[x])!=0 and int(b[x])>0:
                    c=int(b[x])/int(b[x+1])
                    
                else:
                    print("Don't enter 0 or negative value")
            print(c)
        else:
            print("Please enter more then 1 no.")
        n=input("If you Want to substract again Press y:")
        if n=="y":
            t=True
            a=input("Enter another values")
        else:
            t=False
def div(a):
    t=True
    while t:
        b=a.split()
        if len(b)==2:
            c=0 
            for x in range(len(b)-1):
                if int(b[x])!=0 and int(b[x])>0:
                    c=int(b[x])-int(b[x+1])
                else:
                    print("Don't enter 0 or negative value")
            print(c)
        else:
            print("Please enter more then 1 no.")
        n=input("If you Want to devide again Press y:")
        if n=="y":
            t=True
            a=input("Enter another values")
        else:
            t=False
c=int(input("1:add\n2:multiply\n3:substract\n4:division\nchoose:"))
def choice(c):
    if c==1:
        add(input("Add values:"))
    elif c==2:
        multiply(input("Multiply values:"))
    elif c==4:
        div(input("Div values:"))
    elif c==3:
        subst(input("Substract value:"))
    else:
        print("Choose 1 to 4 only")
choice(c)