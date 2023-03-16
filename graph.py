#Create a graphing function
def half_triangle(row_num):
    for i in range(1, row_num + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()