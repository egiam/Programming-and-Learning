def cronometro():
    s=0
    m=0
    h=0
    d=0
    while s<6000:
        print(d,h,m,s)
        s=s+0.0000078
        while s>=60:
            m=m+s//60
            s=s%60
            while m>=60:
                h=h+m//60
                m=m%60
                while h>=24:
                    d=d+h//24
                    h=h%24

def cronometro_r():                                   #tipo alarma
    s=float(input("coloque cantidad de segundos: "))
    m=s//60
    s=s%60
    while s>0:
        print(m,s)
        s=s-0.0000078
        if s<=1 and m>0:
            m=m-1
            s=s+60
        if s<=0 and m<=0:
            print("alarma")


el=input("elija si quiere cronometro o alarma: ")
if el=="cronometro" or el=="c":
    cronometro()
else:
    if el=="alarma" or el=="a":
        cronometro_r()
    else:
        print("la palabra no conduze a ningun lado")
