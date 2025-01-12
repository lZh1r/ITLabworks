#Task 1
def f(file, type):
    a = open(file)
    #whole
    if type == 0:
        print(a.read())
    #line-by-line
    elif type == 1:
        for i in a:
            print(a.readline())
    else:
        return

f("example.txt", 0)

#Task 2
def editFile(fileName, userInput):
    a = open(fileName, "a")
    a.write(userInput)
    a.close()

print("Enter file name")
abc = input()
print("Enter text")
cba = input()

editFile(abc, cba)

#Task 3
def ff(file, type):
    try:
        a = open(file)
    except FileNotFoundError:
        print("No such file exists!")
        return
    #whole
    if type == 0:
        print(a.read())
    #line-by-line
    elif type == 1:
        for i in a:
            print(i)
    else:
        return
