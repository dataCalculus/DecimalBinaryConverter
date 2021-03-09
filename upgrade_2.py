# Python program to convert decimal to binary

# Function to convert Decimal number
# to Binary number
class decToBinary:
    counter = 0
    bin_list = []

    @staticmethod
    def decimalToBinary():
        print("Enter the {0} th number that will be converted binary number ...".format(decToBinary.counter))
        orderedBin = int(input(""))
        decToBinary.bin_list.append(orderedBin)  # append each element to bin_list
        decToBinary.counter = decToBinary.counter + 1
        return (bin(orderedBin).replace("0b", ""))

    @staticmethod
    def getElements():
        cacheBinList = decToBinary.bin_list.copy()
        cacheBinList.sort()
        return (cacheBinList)

    @staticmethod
    def listToBinaryCounter(liste=[]):
        for i in liste:
            print (bin(i).replace("0b", ""))


    @staticmethod
    def getSituation():
        print(decToBinary.counter, "tane input alındı ... Sayılar : ", decToBinary.bin_list, "...")
        decToBinary.listToBinaryCounter(decToBinary.bin_list)

    def __str__(self):
        return "decToBinary classı decimali binarye çeviren bir static method bulundurur." \
               "bu method her çağırıldığında sayma işlemi yapar ."


# Driver code
if __name__ == '__main__':
    while(True):
        # 0 sayı oku , 1 elemanları döndür , 2 durum bilgisi , 3 obje hakkında bilgi , 4 menüyü tekrar göster , 5 çık
        print("0 sayı oku , 1 elemanları döndür , 2 durum bilgisi , 3 obje hakkında bilgi ,"
              " 4 menüyü tekrar göster , 5 çık")
        selection = int(input())
        if selection == 0:
            decToBinary.decimalToBinary()
            continue
        elif selection == 1:
            print(decToBinary.getElements())
            continue
        elif selection == 2:
            print(decToBinary.getSituation())
            continue
        elif selection == 3:
            print(decToBinary())
        elif selection == 4:
            print("0 sayı oku , 1 elemanları döndür , 2 durum bilgisi , 3 obje hakkında bilgi ,"
                  " 4 menüyü tekrar göster , 5 çık")
        elif selection == 5: #exit
            break
        else :
            print("Geçersiz komut... Lütfen tekrar deneyiniz...")

