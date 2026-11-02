'''
4. Read from a File
Open the file in read mode and use file.read() to read and display its content.
'''

with open("output.txt", "r") as file:
    content = file.read()
    print(content)      

