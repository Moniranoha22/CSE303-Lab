N = int(input("Enter any positive number: "))
F0 = 0
F1 = 1
for i in range (2, N):
    F = F0 + F1
    F0 = F1
    F1 = F

print("The Nth fibonacci number is: ", F1)