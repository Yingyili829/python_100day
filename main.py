# 🚨 Don't change the code below 👇
row1 = ["11","21","31"]
row2 = ["12","22","32"]
row3 = ["13","23","33"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
#23
#Write your code below this row 👇
horizonal=int(position[0]) #2
vertical=int(position[1])#3

selected_row = map[vertical -1]
selected_row[horizonal-1] = 'x'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")