numerical_values = []
encrypted_text = ""
text = input("Please enter text>")
invalid = True
increase = 0
while(invalid):
    invalid = False
    password = input("Pincode (atleast 4 digits)>")
    if len(password) != int(password[0]) + 2:
        print("Pincode must be one digit longer then the first number")
        invalid = True
#First letter = order,2nd letter = b,3rd letter = c and so on..
for charechter in text:
    numerical_values.append(ord(charechter))
for x in range (0,len(password) -1):
    num = numerical_values[x]
    for coefficient in password[1:]:
        increase += int(coefficient) * (x ^ (int(password[0]) -x))
        encrypted_text += (chr(num + increase))
print(encrypted_text)
