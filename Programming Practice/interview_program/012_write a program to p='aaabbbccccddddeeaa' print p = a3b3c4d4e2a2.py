mystr = "a,a,a,b,b,c,c,c,c,d,d"
my_list = ''.join(mystr.split(","))
print(my_list)
visited = []
final_list1 = []
final_list2 = []

for char in my_list:
    if char not in visited:
        final_list1.append(f"{char}{my_list.count(char)}")
        final_list2.append(f"{char}:{my_list.count(char)}")
        visited.append(char)

print(final_list1)
print(''.join(final_list1))
print(final_list2)
print(''.join(final_list2))
#---------------------------------------------------

my_list = [1,2,2,2,3,3,4,5,5,5,6,6,7]
new_list = []
for num in my_list:
    if my_list.count(num) == 1:
        new_list.append(num)
print(new_list)

visited = []
count_list = []
for num in my_list:
    if num not in visited:
        count_list.append(f"{num}:{my_list.count(num)}")
        visited.append(num)
print(','.join(count_list))


#--------------------------------------------------
def compress_string(s):
    result = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    result += s[-1] + str(count)
    return result


p = 'aaabbbccccddddeeaa'
compressed_p = compress_string(p)
print(f"p = {compressed_p}")



