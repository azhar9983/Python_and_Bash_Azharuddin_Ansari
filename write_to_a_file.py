'''
3. Write to a File
Write a program to create a text file and write some content to it, using file functions like open() and write().

'''

with open("output.txt", "w") as file:
    file.write("This is a sample text written to the file.\n")
    file.write("You can add more content as needed.\n")
    file.write("File writing in Python is straightforward!\n")  

