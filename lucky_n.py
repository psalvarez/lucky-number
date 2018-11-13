import math

inLimit = input("Write a high search limit (power of 10): ")

while int(inLimit) <= 0:
    inLimit = input("Not valid input. Please, write a high search limit (power of 10): ")

lo = 0
hi = int(inLimit) #ATM, constrained to be a power of ten

t = math.ceil(math.log(hi, 10))

#print(t)

luckyNumbers = 0

for i in range(int(t)) :
    #print("Before iteration " + str(i) + " the amount of lucky numbers is " + str(luckyNumbers))
    x = 8 * luckyNumbers
    luckyNumbers = x + 2 * (9 ** i)

print("The total amount of lucky numbers is " + str(luckyNumbers))
