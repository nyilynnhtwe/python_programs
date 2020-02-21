while True:
 inputString = input("Enter name : ")
 morseString=""
 if inputString.lower()=='exit':
       break
 for j in inputString:
    i=j.lower()
    if i=="a":
       morseString+=".-"
    elif i=="b":
       morseString+="-..."
    elif i=="c":
       morseString+="-.-."
    elif i=="d":
       morseString+="-.."
    elif i=="e":
       morseString+="."
    elif i=="f":
       morseString+="..-."
    elif i=="g":
       morseString+="--."
    elif i=="h":
       morseString+="...."
    elif i=="i":
       morseString+=".."
    elif i=="j":
       morseString+=".---"
    elif i=="k":
       morseString+="-.-"
    elif i=="l":
       morseString+=".-.."
    elif i=="m":
       morseString+="--"
    elif i=="n":
       morseString+="-."
    elif i=="o":
       morseString+="---"
    elif i=="p":
       morseString+=".--."
    elif i=="q":
       morseString+="--.-"
    elif i=="r":
       morseString+=".-."
    elif i=="s":
       morseString+="..."
    elif i=="t":
       morseString+="-"
    elif i=="u":
       morseString+="..-"
    elif i=="v":
       morseString+="...-"
    elif i=="w":
       morseString+=".--"
    elif i=="x":
       morseString+="-..-"
    elif i=="y":
       morseString+="-.--"
    elif i=="z":
       morseString+="--.."
 print(morseString)

