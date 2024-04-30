r = int(input())

if r <= 0 :
    print("Jari-jari harus > 0")

else : # r > 0
    luas = 3.1415 * r * r
    print ("%.2f" % luas)