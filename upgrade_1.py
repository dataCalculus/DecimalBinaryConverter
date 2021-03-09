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
        decToBinary.bin_list.append(orderedBin) # append each element to bin_list
        decToBinary.counter = decToBinary.counter + 1
        return (bin(orderedBin).replace("0b", ""))
    @staticmethod
    def getElements():
        cacheBinList = decToBinary.bin_list.copy()
        cacheBinList.sort()
        return (cacheBinList)
    @staticmethod
    def getSituation():
        print(decToBinary.counter,"tane input alındı ... Sayılar : ",decToBinary.bin_list,"...")

    def __str__(self):
        return "decToBinary classı decimali binarye çeviren bir static method bulundurur." \
               "bu method her çağırıldığında sayma işlemi yapar ."
# Driver code
if __name__ == '__main__':
    print(decToBinary.decimalToBinary())
    print(decToBinary.decimalToBinary())
    #print(decToBinary.getElements())
    decToBinary.getSituation()


#anticipated upgrade1 -> dönüştürülen sayıların kaydedilmesi
# completed


#anticipated upgrade2 -> konsoldan alınan inputlara göre programda karar mekanizması oluşturulması örn :
#işlem sonlandırma , sonlandıktan sonra yeniden başlatma counter 0lama işlemi

#...