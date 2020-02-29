string=input("Enter the text you want to change:")
i=len(string)-1
code=""
while i>=0:
    code+=string[i]   
    i-=1
print("Reversed cipher:"+code)