text = input("Please enter the text to find max block legnth>")
block_legnth = len(text)
coefficients = []
max_x = 0
invalid = True

while(invalid):
    invalid = False
    password_input= input("Pincode (atleast 4 digits)>")
    password = password_input.split(",")
    if len(password) == 1: 
        password = list(password_input)
    if len(password) != int(password[0]) + 2:
        print("Pincode must be two digits longer then the first number")
        invalid = True
    coefficients = password[1:]
def getIncrease(n):
    a = 0
    i = 0
    for coefficient in coefficients:
        a+= (float(coefficient)) * (int(n)**(int(password[0])-int(i)))
        i+=1
    return a

for x in text:
    if ord(x) > max_x: 
        max_x = ord(x)
overflow = True
while overflow:
    if max_x + getIncrease(block_legnth) <= 1114111:
        overflow = False
    else:
        block_legnth -= 1
print("Maximum Block Legnth")
