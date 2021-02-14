# EncryptionAlgorithms
A bunch of Encryption algorithms built for school coursework
<h2>Simple Caeser</h2>
This is a simple ceaser made in python that uses the UNICODE charchterset. To use simpily encrypt using the Simple Caser Cipher file and decrypt using the simple decryptor.
<h3>How it works?</h3>
The Ceaser cipher was first invented by Julius Ceaser to encrypt his commaunds and journals. It works by creating an indexed list of all of the possible charechters. To encrpt just increase every charechters index by a set offset and llop around when you reach the end. Decrypting is just the inverse. This is a rather trivial process. 
<h3>Some details on my alogorithm</h3>
To make mine I used the UNICODE charechter set as this is the default in Python. I used the Chr() and Ord() functions. I didn't include any code to loop back to the first index since I expect standard charechters as a input and not control codes or Private Use Areas from the user. And as those are at the edges of the Charechter set I don't have to worry about overflows.
<h2>Polynomial Ceaser Cipher</h2>
The polynomial ceaser cipher is an idea that I had to make the ceaser ciphers offset be set by a polynomial equation. This means that the same letter will be encrypted differently based on where it is in the string.This makes it a lot hardeer to crack. If one coefficient is off by 0.1 a completely differert string will still be decoded. If you consider all integerial keycodes up to the order of 9 you would have an incredible 11111111000(over 11 bilion discrete combinations). Each iteration run has a time complexity of O(l^2).Where l is the amount of charechters in the string to decrypt. This means the worse case total decyprion is 11111111000 X l^2. That also fails to consider non-itegerial values or orders greater then 9. The varying block legnth also adds more time complexity and possibilities.
<h3>Using the program</h3>
<h4>Setting the polynomial</h4>
The polynomial is set using a 'pincode'. This can be entered in the form "xabcd..." (where a,b,c,d.. are all single digit integers). Or in the form x,a,b,c,d.... (where a,b,c,d... can be any naturual number). x allways has to be a positive integers. x is the order of the polynomial this means x also has to be two larger then the legnth of the key so that there are enough coefficients. Below is how the 'keycode' is used to create the offset.</br>
<img src = "https://render.githubusercontent.com/render/math?math=Offset%20=%20LetterIndex%20%2b%20(an^x%20%2b%20%20bn^{x%20-1}%20%2b%20cn%20^{x%20-2}%20....%20%2b%20FinalNumber*n^{x-x})"/>
Where x is the order of the polynomial and n is it's index in the string
<h4>Block Legnth</h1>
Text gets split into blocks when it is inputted. Each block is encrypted seperately and then combined. This is done so that n(the index in the block) does not get too large and return too many huge numbers. Whilst this does not break the algorithm now it does take longer to compute. I have allowed the user to set a custom blocklegnth to help the user choose betwwen time and security. Smaller blocklegnth = lower security but faster encryption.
<h3>Why I made it?</h3>
The simple caeser cipher has multiple problems which make it easy to crack. For example once you know 1 value it's easy to work out the rest of the values. You can also crack it using the distribution of letters. I.E Some letters are more common then then others so if you map the ciphered letters on a frequency distribution and compared this to a frequency distrinution from a plain english text you could work out the orignal string. This was the next logical step to take to increase security.


