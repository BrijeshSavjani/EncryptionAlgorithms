numerical_values = []
decrypted_text = ""
print("Please enter text")
text = input(">")
for charechter in text:
    numerical_values.append(ord(charechter))
for num in numerical_values:
    decrypted_text += (chr(num - 2))
print(decrypted_text)
