import datetime

Kazu = int(input("Enter..."))

Ans = 0
Flag = False

stime = datetime.datetime.now().time()

if Kazu == 1:
    Ans = 1
        
else:
    while Kazu > 1:
        
        if Flag == False:
            Ans = Kazu * (Kazu-1)
            Flag = True
        else:
            Ans = Ans * (Kazu-1)
        Kazu = Kazu -1
        #print(Kazu)
        #try:
            #Keika = open("Keika.txt", "a")
            #File.write(str(Ans))
            #Keika.write(f"{Ans:,}" + "\n")
            #Keika.close()
        #except exception as e:
            #print("ERROR")

etime = datetime.datetime.now().time()

try:
    File = open("Ans.txt", "w")
    File.write(str(stime) + "\n")
    File.write(str(etime) + "\n")
    File.write(str(Ans))
    #File.write(f"{Ans:,}")

    File.close()
    print("OK!")

except exception as e:

    print("ERROR")
