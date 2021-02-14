import math
decrypted_text = ""
text = input("Please enter text>")
invalid = True
coefficients = []

def getIncrease(n):
    a = 0
    i = int(password[0])
    for coefficient in coefficients:
        a+= (float(coefficient)) * (int(n)**(int(password[0])-int(i)))
        i-=1
    return a

def SplitIntoChunks(master_text,chunk_size):
    Chunks =[]
    Chunk = ""
    i = 0
    orignal_chunk_size = chunk_size
    amount_of_chunks = math.ceil(len(master_text)/chunk_size)
    while (len(Chunks)<= amount_of_chunks):
        while i < chunk_size:
            try:
                Chunk += master_text[i]
            except:
                break
            i +=1
        chunk_size = chunk_size + orignal_chunk_size
        Chunks.append(Chunk)
        Chunk = ""
    return Chunks

def returnIncrease(a,max_x):
    while a > max_x:
        a = a - max_x
    return a

def getPassword():
    invalid = True
    Password = [0]
    while invalid:
        password = input("Password")
        for char in password:
            Password.append(ord(char))
        Password[0] = len(password) + 2
        if len(password) < 4:
            invalid = True
            print("Atleast 4 charechters long")
        else:
            invalid = False
    return Password

def getPincode():
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
    return password

while(invalid):
    choice = input("Please enter 1 to use a password or 2 for a pincode")
    password = []
    if choice == "1":
        password = getPassword()
        invalid = False
    if choice == "2":
        print("Please enter your pin in the form xabc... (Where xabc are integers) or in the form x,a,b,c where x is an integer")
        print("x must be 2 smaller then the total legnth of the pin")
        password = getPincode()
        invalid = False
    try:
        block_legnth = int(input("Block legnth"))
        if block_legnth > len(text):
            invalid = True
    except: invalid = True
for number in password[1:]:
    coefficients.append(number)
chunks = SplitIntoChunks(text,block_legnth)
chunks.remove("")
for chunk in chunks:
    n = 0
    for char in chunk:
            n += 1
            decrypted_text += chr(ord(char) -  int(returnIncrease(getIncrease(n),(1056767))))
print(decrypted_text)


