import turtle
import math


def userinput():
    # number of elements as input
    n = int(input("Enter number of elements : "))

    if n > 2:
        # iterating till the range
        for i in range(0, n):
            print('Enter element X')
            ix = int(input())

            print('Enter element Y')
            iy = int(input())

            y.append(iy)
            x.append(ix)

    else:
        print("Select Atleast 3 points")

    A = [x[0], y[0]]
    B = [x[1], y[1]]
    C = [x[2], y[2]]
    Dd = []
    for i in range(2, n):
        Dd = [x[i], y[i]]

    def line_intersection(line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(p, q):
            return p[0] * q[1] - p[1] * q[0]

        div = det(xdiff, ydiff)
        if div == 0:
            print('Line do not intersect')


        else:
            r = (det(*line1), det(*line2))
            v = det(r, xdiff) / div
            w = det(r, ydiff) / div
            raise Exception("line intersects at:", v, ",", w)

    line_intersection((A, B), (C, Dd))


def input_from_file():
    global mode
    a_file = open("newt.txt")
    list_of_lists = [(line.strip()).split() for line in a_file]
    list_of_lists = [[int(xx) for xx in single_list] for single_list in list_of_lists]
    print(list_of_lists)
    polygon_number = input("Whilch polygon do you want:1, 2 or 3?")
    x = []
    y = []
    if polygon_number == "1":
        x = list_of_lists[0]
        y = list_of_lists[1]

    elif polygon_number == "2":
        x = list_of_lists[2]
        y = list_of_lists[3]

    elif polygon_number == "3":
        x = list_of_lists[4]
        y = list_of_lists[5]
    return x, y


def draw():
    # tim=turtle.Turtle()
    tut.color(outline_color)
    tut.fillcolor(interior_color)
    tut.begin_fill()
    tut.pensize(3)
    tut.ht()
    tut.penup()
    print(x, y)
    tut.goto(x[0], y[0])
    tut.pendown()
    for i in range(1, len(x)):
        tut.goto(x[i], y[i])

    tut.goto(x[0], y[0])
    tut.end_fill()


# Analytical functions
def boundry(x, y):
    a = int(input("Enter X:"))
    b = int(input("Enter Y:"))
    check = (b - y[0]) * (x[1] - x[0]) - (a - x[0]) * (y[1] - y[0])
    if check > 0:
        print("Point lies outside the Polygon")
    elif check < 0:
        print("Point lies inside the Polygon")
    else:
        print("Point lies on the Polygon")


def area(x, y):
    ar = 0
    for i in range(0, len(x) - 1):
        a = x[i] * y[i + 1] - y[i] * x[i + 1]
        ar = ar + a
    print(ar / 2)


def perimeter(x, y):
    pr = 0
    for i in range(0, len(x)-1):
        p = (x[i + 1] - x[i])**2 + (y[i + 1] - y[i])**2 
        p = math.fabs(p)
        pr = pr + p
        pr = math.fabs(pr)
    print(math.sqrt(pr))


# Transformations

def scale():
    s = int(input("Enter the scale you want:"))

    tut.penup()
    tut.goto(x[0], y[0])
    tut.pendown()
    tut.clear()

    for i in range(1, len(x)):
        tim.goto(x[i] * s, y[i] * s)

    tut.goto(x[0], y[0])


def color_choice():
    print("What you want to color:")
    print('1. Outline')
    print('2. Interior')
    print('3. Both')
    choice = int(input('Choice: '))
    outline_color = 'black'
    interior_color = 'white'
    if choice == 1:
        outline_color = input('Outline color: ')
    elif choice == 2:
        interior_color = input('Interior color: ')
    elif choice == 3:
        outline_color = input('Outline color: ')
        interior_color = input('Interior color: ')
    return outline_color, interior_color

def line(x, y):
    t.goto(x, y)
    t.pd()
    t.write(str(x) + "," + str(y))


# manipulation:
def panning():
    delx = int(input('x coordinates by which you would like to move the polygon:'))
    dely = int(input('y coordinates by which you would like to move the polygon:'))
    tut.penup()
    tut.goto(x[0] + delx, y[0] + dely)
    tut.pendown()
    for i in range(0, len(x)):
        tim.goto(delx + x[i], dely + y[i])
    tut.goto(x[0] + delx, y[0] + dely)
def edit():
    edit_what=input("Do you want to 1. remove\n2. add")
    if edit_what=="1":
        deleted_x_vertex=int(input("Enter the x coordinate to be deleted"))
        index=x.index(deleted_x_vertex)
        x.pop(index)
        y.pop(index)
    if edit_what=="2":
        added_x_vertex=float(input("Enter the x coordinate to be added"))
        added_y_vertex=float(input("Enter the y coordinate to be added"))
        x.append(added_x_vertex)
        y.append(added_y_vertex)
        A = [x[0], y[0]]
        B = [x[1], y[1]]
        C = [x[2], y[2]]
        Dd = []
        for i in range(2, len(x)):
            Dd = [x[i], y[i]]

        def line_intersection(line1, line2):
            xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
            ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

            def det(p, q):
                return p[0] * q[1] - p[1] * q[0]

            div = det(xdiff, ydiff)
            if div == 0:
                print('Line do not intersect')


            else:
                r = (det(*line1), det(*line2))
                v = det(r, xdiff) / div
                w = det(r, ydiff) / div
                raise Exception("line intersects at:", v, ",", w)

        line_intersection((A, B), (C, Dd))


        
                            

tut = turtle.Turtle()
turtle.Screen().bgcolor("pink")
tut.ht()

p = []

x = []

y = []
t = turtle
t.ht()
s = turtle.Screen()
p0 = [[100, 0], [100, 100], [0, 100], [0, 0]]
outline_color = 'black'
interior_color = 'white'
while True:
    print("Welcome")
    print("Please Select From listed options:")
    print("1. Enter Polygon COORDS")
    print("2. Select Polygon from file")
    menu = int(input("What Would You Like to do?"))
    if menu == 1:
        userinput()
        outline_color, interior_color = color_choice()
        draw()
        break
    elif menu == 2:
        x, y = input_from_file()
        outline_color, interior_color = color_choice()
        draw()
        break
    else:
        print("Invalid Input")
while True:
    print("")
    print(" Welcome! What would you like your polygon to try?   ")
    print("\n")
    print("| Statistics | Transformation | Output    | Manipulation ")
    print("| P:Area     | S: Scale       | V: Export |              ")
    print("| Q:Perimeter| T: Rotate      | W: Exit   | Z: Panning   ")
    print("| R:Boundry  | U: Color       | X: Input  | Y: Edit      ")
    print("")
    menu = input("Your choice?")
    if menu == "P":
        area(x, y)
    elif menu == "Q":
        perimeter(x, y)
    elif menu == "R":
        boundry(x, y)
    elif menu == "S":
        tut.clear()
        scale()
    elif menu == "T":
        break
    elif menu == "Z":
        panning()
    elif menu == "U":
        outline_color, interior_color = color_choice()
        tut.penup()
        tut.goto(x[0], y[0])
        tut.pendown()
        tut.clear()
        draw()
    elif menu=="Y":
        edit()
        tut.clear()
        draw()
    else:
        print("Invalid Input")
