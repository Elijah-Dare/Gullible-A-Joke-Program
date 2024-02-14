"""Gullible Program - A joke program by AI Sweigart modified by Agbolade Elijah
How to keep a gullible person busy for hours. This is a joke program
Tags: tiny, begineer, humor"""



print("Gullible by AI Sweigart modified by Agbolade Elijah")

while True:
    print("Do you want to know how to keep a gullible person busy for hours? Y/N")
    response = input("> ")
    
    if response.lower() == 'no' or response.lower() == 'n':
        break # if "no" break out of this loop.
    
    elif response.lower() == 'yes' or response == 'no':
        continue # if yes continue to the start of this loop
    
    else:   
        print("{} is not a valid yes/no response".format(response))
    
print("Thank you. Have a nice day!")
    