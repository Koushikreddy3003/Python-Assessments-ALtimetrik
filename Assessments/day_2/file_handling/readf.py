# user defined function to read the file

def read_file(filename):
    try:
        with open(filename,'r') as file:
            text= file.read()
        print(text)

    except FileNotFoundError:
        print("File not found")