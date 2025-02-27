# Writing sample data to a file for demonstration
with open('example.txt', 'w') as file:
    file.write("Hello, World!\nWelcome to Python.\nEnjoy coding!")

# Reading the entire content of the file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Content of the file:")
    print(content)


# Reading the file line by line
with open('example.txt', 'r') as file:
    print("Reading lines one by one:")
    line1 = file.readline()
    print(line1.strip())  # Output: Hello, World!

    line2 = file.readline()
    print(line2.strip())  # Output: Welcome to Python.

    line3 = file.readline()
    print(line3.strip())  # Output: Enjoy coding!