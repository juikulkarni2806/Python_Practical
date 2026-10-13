#Write a Program to Read a File and count how many Vowels are present in its content.
# with open("jui.txt","r") as f:
#     c=f.read()
#     count=0
#     for char in c:
#         if char in "aeiouAEIOU":
#             count+=1
#     print("Total Vowels in File: ",count) 
#Read All Lines From A file into a list.print the total number of lines and display the 2nd and 4th line.
# Open the file and read all lines into a list
# with open("jui.txt", "r") as file:
#     lines = file.readlines()

# # Print the total number of lines
# print("Total lines:", len(lines))

# # Display the 2nd and 4th lines (Index 1 and 3)
# print("2nd line:", lines[1].strip())
# print("4th line:", lines[3].strip())
#Take a Sentence from user, spilt it into words, and store them in a list.print the longest word.
# 1. Take a sentence from the user
#sentence = input("Enter a sentence: ")

# 2. Split it into words and store them in a list
#words = sentence.split()

# 3. Find and print the longest word
#longest_word = max(words, key=len)

#print("The longest word is:", longest_word)
#Read a file spilt its content into words,and store them in a list.
#i.print the Total Number of words
#ii.Print all unique Words.
# Open and read the file
with open('jui.txt', 'r') as file:
    words = file.read().split()

# i. Print total number of words
print("Total words:", len(words))

# ii. Print all unique words
print("Unique words:", set(words))
