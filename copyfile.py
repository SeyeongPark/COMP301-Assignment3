'''
File Name : COMP301-Assignment3
Author's Name : Seyeong Park
Student Number : 301088175
File Description : This is 'copyfile.py' file.
                  It will copy the contents of one file into another file.
'''

# Prompt the user for two file names
Source = input("Enter your file name for Source :\t")
Destination = input("Enter your file name for Destination :\t")

# Open Source file
with open(Source) as SoCont:
    # Write or Add Destination file
    with open(Destination,'w') as DeCont:
        # Copy the contents of the Source file into the Destination file
        for Contents in SoCont:
            DeCont.write(Contents)

# Open Source file for reading
SoCont = open(Source,'r')
firCn = SoCont.read()

# Print the contents of Source file 
print("\nIn file of Source: \n"+firCn+"\n")

print("* Successfully Destination file is copied by Source file\n")

# Print the contents of Sestinationsssss file 
DeCont = open(Source,'r')
secCn = DeCont.read()
print("In file of Destination:\n",secCn+"\n")