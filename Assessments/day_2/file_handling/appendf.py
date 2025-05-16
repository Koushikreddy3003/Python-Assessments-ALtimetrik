# user defined function to append
def append_to_file(filename, text):
    with open(filename,'a') as file:
        file.write('\n'+text)
    print(f"Data appended to {filename}")