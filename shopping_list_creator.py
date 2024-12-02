#Shopping-list creator program

def space():
    print("")

print("Welcome to this Shopping-list program!")
space()
n = input("Please, enter your name here: ")
space()
d = input("Please, enter the date here: ")
space()
print("Enter an element or press 'q'!")

l = []

while True:
    i = input()
    if i == 'q':
        break
    l.append(i)

with open('list.txt', 'w') as file:
    file.write("Name: " + n + "\n")
    file.write("Date: " + d + "\n")
    file.write("\n")
    file.write("I need: \n")
    for e in l:
        file.write(e + "\n")

print("The list is successfully done!")
print("You can check the list.txt in the folder of the program!")
