from matrix import Matrix
import time

def cls(n):
    for i in range(n):
        print()

def menu(**args):
    tab_string = args["num_tabs"] * "\t"
    
    if args.get("right_column") is not None:
        print("NUMBER" + tab_string  + args["right_column"])
    
    for i in range(len(args["list"])):
        print("[" , i+1 , "] " , tab_string , args["list"][i])



print("This is a Demo of Creating Matrices in Python")
time.sleep(3)

print("You'll be able to create  and display only 3 Matrices")
time.sleep(3)

print("Lets GO!")
time.sleep(4)

cls(13)

mat_list = []

for i in range(3):
    print(f"Matrix {i+1}:")

    if i != 2:
        print(" Enter How Many Rows: ", end="")
        nrows  = int(input())

        print(" Enter How Many Columns: " , end="")
        ncols  = int(input())

        cls(2)

        menu(right_column = "Filling Method", list = ["Default Value", "Row-by-Row"], num_tabs = 1)
        print(" \tEnter NUMBER of Your Choice: ", end="")
        fill_method = int(input())

        cls(2)

        if fill_method == 1:
            print(" Enter The Default Value: " , end="")
            default_value = int(input())

            mat = Matrix.create_matrix(nrows= nrows , ncols= ncols , default_value= default_value)

        elif fill_method == 2:
            mat = Matrix.create_matrix(nrows= nrows , ncols= ncols)

    else:
        menu(right_column = "Filling Method" , list = ["Matrix 1 + Matrix 2" , "Matrix 1 - Matrix 2" , "Matrix 1 * Matrix 2" , "Matrix 1 / Matrix 2", "Matrix 1 raise to power of Matrix 2"], num_tabs = 2)
        print(" \tEnter NUMBER of Your Choice: ", end="")
        fill_method = int(input())

        if fill_method == 1:
            mat = mat_list[0] + mat_list[1]

        elif fill_method == 2:
            mat = mat_list[0] - mat_list[1]
        
        elif fill_method == 3:
            mat = mat_list[0] * mat_list[1]

        elif fill_method == 4:
            mat = mat_list[0] / mat_list[1]

        elif fill_method == 5:
            mat = mat_list[0] ** mat_list[1]

    mat_list.append(mat)
    cls(7)


print("Now Let's Print Your Matrices\n")
time.sleep(2)

cls(7)

counter = 0
while counter < 3:

    menu(right_column = "Choice", list = ["Matrix 1" , "Matrix 2", "Matrix 3"], num_tabs = 1)
    print("Enter NUMBER of Matrix to be Displayed: " , end="")
    mat_to_print = int(input())
    mat_to_print -= 1

    cls(2)
    
    print(mat_list[mat_to_print])
    
    cls(3)
    counter += 1