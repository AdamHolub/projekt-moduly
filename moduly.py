import math
import random

print("Vítejte v programu")
run=True

while run==True:
    print("1. kalkulačka\n2. převody radianu na stupně\n3. sin, cos, tan\n4. random num. generátor\n5. exit\n")
    vyber=int(input("Zvolte možnost\n"))
    if vyber==1:
        while True:
            print("1. plus\n2. minus\n3. krát\n4. děleno\n5. exit\n")
            choice=int(input("Zvolte možnost\n"))
            if choice==1:
                def plus(num1, num2):
                    return num1+num2
                num1=int(input("Zadejte prvni cislo\n"))
                num2=int(input("Zadejte druhe cislo\n"))
                print(plus(num1,num2))
            if choice==2:
                def minus(num1, num2):
                    return num1-num2
                num1=int(input("Zadejte prvni cislo\n"))
                num2=int(input("Zadejte druhe cislo\n"))
                print(minus(num1,num2))
            if choice==3:
                def krat(num1, num2):
                    return num1*num2
                num1=int(input("Zadejte prvni cislo\n"))
                num2=int(input("Zadejte druhe cislo\n"))
                print(krat(num1,num2))
            if choice==4:
                def deleno(num1, num2):
                    return num1/num2
                num1=int(input("Zadejte prvni cislo\n"))
                num2=int(input("Zadejte druhe cislo\n"))
                print(deleno(num1,num2))
            if choice==5:
                break
    if vyber==2:
        while True:
            print("1. radiany na stupně\n2. stupně na radiany\n3. exit\n")
            choice=int(input("zvolte možnost\n"))
            if choice==1:
                radian=int(input("Zadejte počet radiánů\n"))
                print(math.degrees(radian))
            if choice==2:
                degrees=int(input("Zadejte počet stupňů\n"))
                print(math.radians(degrees))
            if choice==3:
                break
    if vyber==3:
        while True:
            print(  "1. sin\n2. cos\n3. tan\n4. exit\n")
            choice=int(input("zvolte možnost\n"))
            if choice==1:
                sin=int(input("Zadejte sin\n"))
                print(math.degrees(math.sin(sin)))
            if choice==2:
                cos=int(input("Zadejte cos\n"))
                print(math.degrees(math.cos(cos)))
            if choice==3:
                tan=int(input("Zadejte tan\n"))
                print(math.degrees(math.tan(tan)))
            if choice==4:
                break
    if vyber==4:
        while True:
            print("1. random generator\n2. exit\n")
            choice=int(input("Zvolte možnost\n"))
            if choice==1:
                num1=int(input("Zadejte min. cislo do random generatoru\n"))
                num2=int(input("Zadejte max. cislo do random generatoru\n"))
                print(random.randrange(num1,num2))
            if choice==2:
                break
    if vyber==5:
        print("konec programu")
        run=False