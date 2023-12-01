# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Read the file
with open("day1a.txt") as trebuchet:
    content = trebuchet.read()

#Perform replacement
content = content.replace("eight","e8t")
content = content.replace("one","o1e")
content = content.replace("two","t2o")
content = content.replace("three","t3e")
content = content.replace("four","f4r")
content = content.replace("five","f5e")
content = content.replace("six","s6x")
content = content.replace("seven","s7n")
content = content.replace("nine","n9e")

#Write content with replaced strings
with open("temp1.txt" , "w") as temp1:
    temp1.write(content)

with open("temp2.txt" , "w") as temp2:
    temp2.write("")

with open("temp1.txt","r") as trebuchet:
    lines = trebuchet.readlines()

#write only numbers
for line in lines:
    a = ''.join(char for char in line if char.isdigit())
    with open("temp2.txt", "a") as temp2:
        temp2.write(a+"\n")

with open("temp2.txt") as temp2:
    lines = temp2.readlines()

summ = sum(int(line[0])*10 + int(line[-2]) for line in lines)

print(summ)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
