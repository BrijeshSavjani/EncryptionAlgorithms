# EncryptionAlgorithms
A bunch of Encryption algorithms built for school coursework
<h2>Simple Caeser</h2>
This is a simple ceaser made in python that uses the UNICODE charchterset. To use simpily encrypt using the Simple Caser Cipher file and decrypt using the simple decryptor.
<h3>How it works?</h3>
The Ceaser cipher was first invented by Julius Ceaser to encrypt his commaunds and journals. It works by creating an indexed list of all of the possible charechters. To encrpt just increase every charechters index by a set offset and llop around when you reach the end. Decrypting is just the inverse. This is a rather trivial process. 
<h3>Some detail on my alogorithm</h3>
To make mine I used the UNICODE charechter set as this is the default in Python. I used the Chr() and Ord() functions. I didn't include any code to loop back to the first index since I expect standard charechters as a input and not control codes or Private Use Areas from the user. And as those are at the edges of the Charechter set I don't have to worry about overflows.
<h2>Polynomial Ceaser Cipher</h2>
The polynomial ceaser cipher is an idea that I had to make the ceaser ciphers offset be set by a polynomial equation. This means that the same letter will be encrypted differently based on where it is in the string.This makes it a lot hardeer to crack. If one coefficient is off by 0.01 a completely differert string will still be decoded. If you consider all integerial keycodes up to the order of 9 you would have an incredible 11111111000(over 11 bilion discrete combinations). Each iteration run has a time complexity of O(l^2).Where l is the amount of charechters in the string to decrypt. This means the worse case total decyprion is 11111111000 X l^2. That also fails to consider non-itegerial values or orders greater then 9.
<h3>Using the program</h3>
<h4>Setting the polynomial</h4>
The polynomial is set using a 'keycode'. This can be entered in the form "nabcd..." (where a,b,c,d.. are all single digit integers). Or in the form n,a,b,c,d.... (where a,b,c,d... can be any naturual number). n allways has to be a positive integers. n is the order of the polynomial this means n also has to be two larger then the legnth of the key so that there are enough coefficients. Below is how the 'keycode' is used to create the offset.</br>
<img src = "https://render.githubusercontent.com/render/math?math=Offset%20=%20LetterIndex%20%2b%20(a^n%20%2b%20%20b^{n%20-1}%20%2b%20c%20^{n%20-2}%20....%20%2b%20FinalNumber^{n-n})"/>
<h4>Block Legnth</h1>
