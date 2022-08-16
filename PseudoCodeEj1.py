h=int(input("Ingresa la hora\n"))
m=int(input("Ingresa los minutos\n"))
s=int(input("Ingresa los segundos\n"))

if(h >= 0 and h <= 23 and m >= 0 and m <= 59 and s >= 0 and s <= 59):
    if(h==23):
        if(m==59):
            if(s==59):
                print("La hora dos segundos es: "+" 00:00:01")
            elif(s==58):
                print("La hora dos segundos es: "+" 00:00:00")
            else:
                s = s+2
                print("La hora dos segundo tarde es: "+str(h)+":"+str(m)+":"+str(s))
        elif(m==58):
            if(s==59):
                m = 59
                print("La hora dos segundos es: "+str(h)+":"+str(m)+": 01")
            elif(s==58):
                m=59
                print("La hora dos segundos es: "+str(h)+":"+str(m)+":00")
            else:
                s = s+2
                print("La hora dos segundo tarde es: "+str(h)+":"+str(m)+":"+str(s))
        else:
            if(s==59):
                m = m+1
                print("La hora dos segundos es: "+str(h)+":"+str(m)+":01")
            elif(s==58):
                m = m+1
                print("La hora dos segundos es: "+str(h)+":"+str(m)+":00")
            else:
                s = s+2
                print("La hora dos segundo tarde es: "+str(h)+":"+str(m)+":"+str(s))
    else:
        if(m==59):
            if(s==59):
                print("La hora dos segundos es: "+str(h+1)+":00:01")
            elif(s==58):
                print("La hora dos segundos es: "+str(h+1)+":00:00")
            else:
                s = s+2
                print("La hora dos segundo tarde es: "+str(h)+":"+str(m)+":"+str(s))
        elif(m==58):
            if(s==59):
                m = 59
                print("La hora dos segundos es: "+str(h)+":"+str(m)+": 01")
            elif(s==58):
                m=59
                print("La hora dos segundos es: "+str(h)+":"+str(m)+":00")
            else:
                s = s+2
                print("La hora dos segundo tarde es: "+str(h)+":"+str(m)+":"+str(s))
        else:
            if(s==59):
                m = m+1
                print("La hora dos segundos es: "+str(h)+":"+str(m)+":01")
            elif(s==58):
                m = m+1
                print("La hora dos segundos es: "+str(h)+":"+str(m)+":00")
            else:
                s = s+2
                print("La hora dos segundo tarde es: "+str(h)+":"+str(m)+":"+str(s))
else:
    print("Hora incorrecta")