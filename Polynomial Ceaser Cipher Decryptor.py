numerical_values = []
decrypted_text = ""
text = input("Please enter text>")
encrypted = text.split(',')
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
    password_input = input("Pincode (atleast 4 digits)>")
    password = password_input.split(",")
    if len(password) == 1: 
        password = list(password_input)
    if len(password) != int(password[0]) + 2:
        print("Pincode must be one digit longer then the first number")
        invalid = True
for number in password[1:]:
    coefficients.append(number)
x = password[0]
n = 0
for char in encrypted:
        n += 1
        decrypted_text += chr(int(char) - getIncrease(n))
print(decrypted_text)


