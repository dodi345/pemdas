password = "1234"
i = 1
j = 3

for i in range (i, j+1):
    pswd = input("Masukan Password : ")
    if pswd == password :
        print("Password anda benar !!!")
        break
    else :
        i = i +1
        j = j-1


        print("Password anda salah ",j, "kali lagi")