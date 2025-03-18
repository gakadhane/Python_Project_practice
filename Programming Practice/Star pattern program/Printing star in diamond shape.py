h = int(input("enter diamond height: "))

for x in range(h):
    print(" " * (h - x), "*" * (2 * x - 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2 * x - 1))
# O/P:enter diamond height: 5
#
#      *
#     ***
#    *****
#   *******
#    *****
#     ***
#      *