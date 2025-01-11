# Write a program to take a user age and let him know if he can go the club.  21


age = int(input('Please enter a persons age.'))     # ask user to input age

if age >= 18 :                                      # Allow 18 and above to club
    print ("welcome to our club!")
else:
    print("We are sorry you are not allowed!")