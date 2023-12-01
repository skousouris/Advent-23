# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os

home_directory = os.path.expanduser("~")
print("Home Directory:", home_directory)


with open("day1a.txt") as trebuchet:
    lines = trebuchet.readlines()

with open("temp1.txt" , "w") as temp1:
    temp1.write("")


for line in lines[:]:
    a = ''.join(char for char in line if char.isdigit())
    with open("temp1.txt", "a") as temp1:
        temp1.write(a+"\n")

with open("temp1.txt") as temp1:
    lines = temp1.readlines()

sum = 0
num = 0
for line in lines:
    first = int(line[0])
    last = int(line[-2])
    sum += first*10 + last
    num += 1
    print(num,first,last,sum)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
