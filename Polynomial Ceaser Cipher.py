numerical_values = []
encrypted_text = ""
text = input("Please enter text>")
unecncrypted = list(text)
invalid = True
x = 0
coefficients = []

def getIncrease(n):
    a = 0
    i = 0
    for coefficient in coefficients:
        a+= (int(coefficient)) * (int(n)**(int(x)-int(i)))
        i+=1
    return a

while(invalid):
    invalid = False
    password = input("Pincode (atleast 4 digits)>")
    if len(password) != int(password[0]) + 2:
        print("Pincode must be one digit longer then the first number")
        invalid = True
#First letter = order,2nd letter = b,3rd letter = c and so on.. where f(n) = an^x + bn^(x-1) + c^(x-2) .... [letter]^(x-x)

for number in password[1:]:
    coefficients.append(number)
x = password[0]
n = 0
for char in unecncrypted:
        n += 1
        encrypted_text += chr((ord(char) + getIncrease(n)))
print(encrypted_text)
