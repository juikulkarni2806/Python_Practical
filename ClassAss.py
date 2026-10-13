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
with open("jui.txt", "r") as file:
    lines = file.readlines()

# Print the total number of lines
print("Total lines:", len(lines))

# Display the 2nd and 4th lines (Index 1 and 3)
print("2nd line:", lines[1].strip())
print("4th line:", lines[3].strip())
