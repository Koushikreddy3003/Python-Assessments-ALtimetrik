
#importing the user defined functions
import readf, appendf, writef

# displaying options for file operations
print("Assignment Day 2")
print("1. write a file")
print("2. Read a file")
print("3. Append a file")
print("4. Exit")

try:
    while True:
        choice=int(input("Enter the choice:"))

        if choice==1:
            #Writing block
            try:
                filename=input("enter the file name")
                text=input("Enter the text to write in the file")
                writef.write_to_file(filename,text)
                
            except FileNotFoundError:
                print("File Error: check the file you entered")
        

        elif choice == 2:
            #Reading block
            try: 
                filename=input("Enter the File name to read")
                readf.read_file(filename)
            except FileNotFoundError:
                print("File Not Found: Check the file name entered")

        elif choice==3:
            #Append Block
            try:
                filename=input("Enter the File name to Append")
                text=input("Enter the text to append")
                appendf.append_to_file(filename,text)
            except FileNotFoundError:
                print("file not found: check the file you entered")

        elif  choice==4:
            #exit block
            print("*************exiting the program*************")
            break
        else:
            '''error block - invalid input'''
            print("***********invalid input**************")
#exception block
except ValueError:
    print("Enter Proper Numeric Values")