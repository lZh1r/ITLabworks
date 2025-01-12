def describe(name, age=30):
    print(f"{name} {age} лет")

nn = input()
describe(nn)
describe(nn, 1230)

def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

print(is_prime(13))
print(is_prime(234))