# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure #(1 to 3)?  ")
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

horizontal = int(position[0])  
vertical = int(position[1])

first_number_selected = map[vertical - 1]
first_number_selected[horizontal - 1] = "X"

#### or using one line ####

# map[vertical - 1][horizontal - 1] = "X"

#Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# map = [[0"⬜️", 1"⬜️", 2"⬜️"], [0"⬜️", 1"⬜️", 2"⬜️"], [0"⬜️", 1"⬜️", 2"⬜️"]]

             #1     2     3
# row1 =  1 ["⬜️", "⬜️", "⬜️"]
# row2 =  2 ["⬜️", "⬜️", "⬜️"]
# row3 =  3 ["⬜️", "⬜️", "⬜️"]

###INDEX### WHY WE NEED TO USE -1 === INPUT = 3 WONT WORK BUT 3-1 = 2 WHICH WILL SELECT THE SQUARE 3
        #     0     1     2
# row1 =  0 ["⬜️", "⬜️", "⬜️"]
# row2 =  1 ["⬜️", "⬜️", "⬜️"]
# row3 =  2 ["⬜️", "⬜️", "⬜️"]

# test = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]

# print(test[0])
# print(test[0][2])

# print(test[0])
# print(test[0][1])

# print(test[1])
# print(test[1][2])

# print(test[1])
# print(test[1][1])

# print(test[2])
# print(test[2][0])

# print(test[2])
# print(test[2][3 - 1])