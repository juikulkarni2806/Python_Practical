#Write a Program to Read a File and count how many Vowels are present in its content.
with open("jui.txt","r") as f:
    c=f.read()
    count=0
    for char in c:
        if char in "aeiouAEIOU":
            count+=1
    print("Total Vowels in File: ",count) 
    