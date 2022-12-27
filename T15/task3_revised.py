# displays countdown from 20 to 0
print("Numbers from 20 down to 0:")
i = 21
while i > 0:
    i -= 1
    print(i)


# displays all the even numbers between 1 and 20
print("\nAll the even numbers between 1 and 20: ")
for i in range(1, 20):
    if i % 2 == 0:
        print(i)


# creates a star pattern
# 5 lines; each line contains number of starts same as the line number
print("\nThe star pattern: ")
n = 5
i = 0
for i in range(n):
    for j in range(i+1):
        print("*", end='')
    print()


# find the greatest common divisor of two given numbers
print("\nGreatest common divisor or Highest common factor (HFC)")
# was not too sure how to solve the problem, so checked YouT ube videos to solve
# links: https://www.youtube.com/watch?v=DePWIOK1STg , https://www.youtube.com/watch?v=cahuG1cEQdY&t=95s

n1 = 80
n2 = 30

if n1 < n2:
    lower_n = n1
else:
    lower_n = n2

# maximum value that can divide both numbers is the smallest number
# minimum value is always at least 1
gcd = 0   # initiated
for i in range(1, lower_n + 1):
    # i = gcd if both n1 & n2 are divisible by i
    if (n1 % i == 0) and (n2 % i == 0):
        gcd = i

print(gcd)


