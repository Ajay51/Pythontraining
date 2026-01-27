# calculate_string_length
uname=(input("Enter your username: "))
print("Lenght of username: ",len(uname))
if len(uname)>8:
    print("Username is too long")
elif len(uname)<5:
    print("Username is too short")
else:  
    print("Username length is acceptable")
