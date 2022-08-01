from pathlib import Path
import codecs


print("")
print(" ██████   ██████ ███████████   ████████      █████████   █████                                         ")
print("░░██████ ██████ ░░███░░░░░███ ███░░░░███    ███░░░░░███ ░░███                                          ")
print(" ░███░█████░███  ░███    ░███░░░    ░███   ░███    ░░░  ███████    ██████   ███████ ████████    ██████ ")
print(" ░███░░███ ░███  ░██████████    ██████░    ░░█████████ ░░░███░    ███░░███ ███░░███░░███░░███  ███░░███")
print(" ░███ ░░░  ░███  ░███░░░░░░    ░░░░░░███    ░░░░░░░░███  ░███    ░███████ ░███ ░███ ░███ ░███ ░███ ░███")
print(" ░███      ░███  ░███         ███   ░███    ███    ░███  ░███ ███░███░░░  ░███ ░███ ░███ ░███ ░███ ░███")
print(" █████     █████ █████       ░░████████    ░░█████████   ░░█████ ░░██████ ░░███████ ████ █████░░██████ ")
print("░░░░░     ░░░░░ ░░░░░         ░░░░░░░░      ░░░░░░░░░     ░░░░░   ░░░░░░   ░░░░░███░░░░ ░░░░░  ░░░░░░  ")
print("                                                                           ███ ░███                    ")
print("                                                                          ░░██████                     ")
print("                                                                           ░░░░░░                      ")
print("")

def writer():
    #ecnoding the hidden text
    text = input()
    text = "Hidden here " + text
    text = codecs.encode(text,'rot_13')

    #making the new file with the hidden text
    soundFile = open(inputFileName, 'rb')
    open(("new " + inputFileName), 'wb').write(soundFile.read()+bytes(text, encoding='utf8'))


def reader():
    #Open file and find location of my anchor
    wholefile=open(inputFileName, 'rb').read()
    anchor="Uvqqra urer "
    location = wholefile.rfind(bytes(anchor,encoding='utf8'))
    #check if it doesn't exist
    if location == -1:
        print("No secret data was found")
    else:
        #Prints and decodes the rot13
        print(codecs.decode((wholefile[location+12:]).decode("utf8"),'rot_13'))


#Input file and and check if it exists
try:
    print("Input file you want to read or write:")
    inputFileName = str(input())
    open(inputFileName)
except Exception as e:
    print("File does not exist")
    quit()

#Check if file size is not too large, with a large buffer to allow a large secret message
if Path(inputFileName).stat().st_size >= 62000000000:
    print("File too large")
    quit()

print("Would you like to (r)ead or (w)rite a secret")
#choice validation
flag = False
while flag == False:
    choice = input()
    flag = True

    if choice == "r":
        reader()
    elif choice == "w":
        print("What text do you want to hide")
        writer()
    else:
        print("Not valid input, try again")
        flag = False
