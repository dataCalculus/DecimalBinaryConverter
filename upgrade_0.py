# Python program to convert decimal to binary

# Function to convert Decimal number
# to Binary number
class decToBinary:
    counter = 0
    @staticmethod
    def decimalToBinary():
        print("Enter the {0} th number that will be converted binary number ...".format(decToBinary.counter))
        orderedBin = int(input(""))
        decToBinary.counter = decToBinary.counter + 1
        return (bin(orderedBin).replace("0b", ""))
    def __str__(self):
        return "decToBinary classı decimali binarye çeviren bir static method bulundurur." \
               "bu method her çağırıldığında sayma işlemi yapar ve hafızalıdır."
# Driver code
if __name__ == '__main__':
    print(decToBinary.decimalToBinary())
    print(decToBinary.decimalToBinary())

#anticipated upgrade1 -> dönüştürülen sayıların kaydedilmesi

#anticipated upgrade2 -> konsoldan alınan inputlara göre programda karar mekanizması oluşturulması örn :
#işlem sonlandırma , sonlandıktan sonra yeniden başlatma counter 0lama işlemi

#...