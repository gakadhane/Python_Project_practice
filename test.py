def outer_fun():
    x = 10
    def inner_fun():
        nonlocal x
        x = 20
        print(x)
    inner_fun()
    print(x)
outer_fun()


x = 10
def inner_fun():
    x = 20
    print(x)
inner_fun()
print(x)


text = "   Hello   welcome  gaurav   "

text1 = text.strip()
text2 = text.split()
text3 = text.replace("welcome", "star")
text4 = text.lstrip()
text5 = text.rstrip()
text6 = text.rsplit()
text7 = " ".join(text.split())
print(text1)
print(text2)
print(text3)
print(text4)
print(text5)
print(text6)
print(text7)



class parent():

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a-b

print(f"addition of a and b is: {parent.add(10,5)}")





