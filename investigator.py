print("BINARY CLUE INVESTIGATOR")
print("------------------------")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nNumber 1:", a)
print("Binary 1:", bin(a)[2:])

print("\nNumber 2:", b)
print("Binary 2:", bin(b)[2:])

clue = a ^ b

print("\nXOR Clue:", clue)
print("Binary Clue:", bin(clue)[2:])

if clue == 0:
    print("Both numbers have the same bits!")
else:
    print("Different bits have been detected!")