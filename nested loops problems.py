#1. Multiplication Table (1 to 10)

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print() 

#2.Count Prime Numbers in a Range (1 to 100)

count = 0
for num in range(2, 101):  # 1 is not prime
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print("Total prime numbers between 1 and 100:", count)

#3. Print All Pairs (i, j) Where Sum is Even

n = int(input("Enter a number (n): "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i + j) % 2 == 0:
            print(f"({i}, {j})")

# 4.Count Total Factors from 1 to n

n = int(input("Enter a number (n): "))
total_factors = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            total_factors += 1

print("Total number of factors from 1 to", n, "is:", total_factors)

# 5.Print All Pythagorean Triplets with Values ≤ n

n = int(input("Enter a number (n): "))
print("Pythagorean Triplets:")

for a in range(1, n + 1):
    for b in range(a, n + 1):  # start from a to avoid duplicate pairs
        for c in range(b, n + 1):
            if a*a + b*b == c*c:
                print(f"({a}, {b}, {c})")


