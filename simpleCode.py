# Python program to convert decimal to binary

# Function to convert Decimal number
# to Binary number
def decimalToBinary(n):
	return bin(n).replace("0b", "")

# Driver code
if __name__ == '__main__':
	print(decimalToBinary(22))
	print(decimalToBinary(18))
	print(decimalToBinary(7))

#nasıl bir upgrade olabilir ?
#en büyük sayıya göre diğer sayılara sıfır eklnemesi (0.upgrade)
#bunun için tek satırda inputlar alınarak formatlanmış bir formda bastırılmalı ordered bir şekilde (1.upgrade)
