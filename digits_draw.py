string = input()
arr = []
counter = 0
for i in range(len(string)) :
    arr.append(int(string[i]))
    counter += 1

arr0 = ["----", " -- ", "|  |", "|  |", "    ", "|  |", "|  |", " -- ", "----"]
arr1 = ["----", "    ", "   |", "   |", "    ", "   |", "   |", "    ", "----"]
arr2 = ["----", " -- ", "   |", "   |", " -- ", "|   ", "|   ", " -- ", "----"]
arr3 = ["----", " -- ", "   |", "   |", " -- ", "   |", "   |", " -- ", "----"]
arr4 = ["----", "    ", "|  |", "|  |", " -- ", "   |", "   |", "    ", "----"]
arr5 = ["----", " -- ", "|   ", "|   ", " -- ", "   |", "   |", " -- ", "----"]
arr6 = ["----", " -- ", "|   ", "|   ", " -- ", "|  |", "|  |", " -- ", "----"]
arr7 = ["----", " -- ", "   |", "   |", "    ", "   |", "   |", "    ", "----"]
arr8 = ["----", " -- ", "|  |", "|  |", " -- ", "|  |", "|  |", " -- ", "----"]
arr9 = ["----", " -- ", "|  |", "|  |", " -- ", "   |", "   |", " -- ", "----"]

nums = [arr0, arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9]

if counter > 1 :
    for j in range(9) :
        for i in range(counter):
            if i == 0 : 
                if j == 0 or j == 8:
                    print("x", nums[arr[i]][j], "-", sep = "", end = "")
                else :
                    print("|", nums[arr[i]][j], " ", sep = "", end = "") 
            elif i == counter - 1 :
                if j == 0 or j == 8:
                    print(nums[arr[i]][j], "x", sep = "", end = "")
                    print("")
                else : 
                    print(nums[arr[i]][j], "|", sep = "", end = "")
                    print("")
            else : 
                if j == 0 or j == 8:
                    print(nums[arr[i]][j], "-", sep = "", end = "")
                else :
                    print(nums[arr[i]][j], " ", sep = "", end = "")
elif counter == 1 :
    for j in range(9) :
        if j == 0 :
            print("x", nums[arr[0]][j], "x", sep = "", end = "")
            print("")
        elif j == 8 :
            print("x", nums[arr[0]][j], "x", sep = "", end = "")
            print("")
        else :
            print("|", nums[arr[0]][j], "|", sep = "", end = "") 
            print("")

print("")