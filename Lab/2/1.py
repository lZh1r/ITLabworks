def greet(name):
    print(f"Привет, {name}!")

def square(num):
    return num**2

def max_of_two(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return -1

greet(input())

print(square(int(input())))

a,b = int(input()), int(input())
print(max_of_two(a,b))