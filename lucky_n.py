import math

lo = 0
hi = 10 #ATM, constrained to be a power of ten

t = math.log(hi, 10)

luckyNumbers = 0

for i in range(int(t)) :
    #print("Before iteration " + str(i) + " the amount of lucky numbers is " + str(luckyNumbers))
    x = 8 * luckyNumbers
    luckyNumbers = x + 2 * (9 ** i)

print("The total amount of lucky numbers is " + str(luckyNumbers))
