#prompt user for file name
#take name of file as input
#read text from file
#print spellchecked text to console
#provide task to run from build

#file_name = input("Enter file name:\n")


if __name__ == "__main__":

    with open("sample.txt") as file: 
        text=file.read()
    print(text)

    