import math
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
def SplitIntoChunks(master_text,chunk_size):
    Chunks =[]
    Chunk = ""
    i = 0
    amount_of_chunks = math.ceil(len(master_text)/chunk_size)
    while (len(Chunks)<= amount_of_chunks):
        while i < chunk_size:
            try:
                Chunk += master_text[i]
            except:
                break
            i +=1
        chunk_size += chunk_size
        Chunks.append(Chunk)
        Chunk = ""
    return Chunks
while(invalid):
    invalid = False
    password_input= input("Pincode (atleast 4 digits)>")
    password = password_input.split(",")
    if len(password) == 1: 
        password = list(password_input)
    if len(password) != int(password[0]) + 2:
        print("Pincode must be two digits longer then the first number")
        invalid = True
    try:
        block_legnth = int(input("Block legnth"))
        if block_legnth > len(text):
            invalid = True
    except: invalid = True
#First letter = order,2nd letter = b,3rd letter = c and so on.. where f(n) = an^x + bn^(x-1) + c^(x-2) .... [letter]^(x-x)
for number in password[1:]:
    coefficients.append(number)
chunks = SplitIntoChunks(text,block_legnth)
chunks.remove("")
for chunk in chunks:
    n = 0
    for char in chunk:
            n += 1
            encrypted_text += chr(ord(char) + int(getIncrease(n)))
       
    
print(encrypted_text)
