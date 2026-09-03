"""จำนวนเฉพาะ"""
num1, num2 = map(int, input().split())
prime = []
for i in range(num1, num2+1):
    if i == 2:
        prime.append(i)
    elif i == 1:
        pass
    elif i == 3:
        prime.append(i)
    elif i == 5:
        prime.append(i)
    elif i == 7:
        prime.append(i)
    elif not i % 2 :
        pass
    elif not i % 3:
        pass
    elif not i % 5:
        pass
    elif not i % 7:
        pass
    elif not i%i and not i%1 :
        prime.append(i)
if not prime:
    print(f"Total primes: {len(prime)}")
else:
    print(*prime)
    print(f"Total primes: {len(prime)}")
