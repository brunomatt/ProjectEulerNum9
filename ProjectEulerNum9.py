#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a^2 + b^2 = c^2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import time
start = time.time()
answer = 1

while answer == 1:
    for c in range(1,500):
        for b in range(1,499):
            for a in range(1,498):
                if a * a + b * b == c * c and a + b + c == 1000 and a < b < c:
                    answer = a * b * c

print(answer)

stop = time.time()
print('Time: ', stop - start)