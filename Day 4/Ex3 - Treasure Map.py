row1 = ["😄","😄","😄"]
row2 = ["😄","😄","😄"]
row3 = ["😄","😄","😄"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure?\n")

if position[1] == "1":
    if position[0] == "1":
        row1[0] = "X"
    if position[0] == "2":
        row1[1] = "X"
    if position[0] =="3":
        row1[2] = "X"

if position[1] == "2":
    if position[0] == "1":
        row2[0] = "X"
    if position[0] == "2":
        row2[1] = "X"
    if position[0] == "3":
        row2[2] = "X"

if position[1] == "3":
    if position[0] == "1":
        row3[0] = "X"
    if position[0] == "2":
        row3[1] = "X"
    if position[0] == "3":
        row3[2] = "X"

print(f"{row1}\n{row2}\n{row3}")

# Alternate Way:
#
# row1 = ["😄","😄","😄"]
# row2 = ["😄","😄","😄"]
# row3 = ["😄","😄","😄"]
#
# map = [row1, row2, row3]
#
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Where do you want to put the treasure?\n")
#
# horizonal = int(position[0])
# vertical = int(position[1])
#
# map[vertical-1][horizonal-1] = "X"