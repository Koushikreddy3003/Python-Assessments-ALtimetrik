#User defined function to read the file

def write_to_file(filename,text):
    with open(filename, 'w') as file:
        file.write(text)
    print(f"data writen to {filename}")