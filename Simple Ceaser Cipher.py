numerical_values = []
encrypted_text = ""
print("Please enter text")
text = input(">")
for charechter in text:
    numerical_values.append(ord(charechter))
for num in numerical_values:
    encrypted_text += (chr(num +2))
print(encrypted_text)
