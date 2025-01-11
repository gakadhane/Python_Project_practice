import os

file_name = "Gaurav.txt"
content = "This is a Gaurav's File of testdata"

with open(file_name, "w") as file:
    file.write(content)

with open(file_name, "r") as file:
    content2 = file.read()
    print(content2)

# os.chdir("Desktop")  # change the director to desktop