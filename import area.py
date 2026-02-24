import area

print("1. Area of Circle")
print("2. Area of Rectangle")

choice = int(input("Enter your choice (1 to 3): "))

if choice == 1:
    r = float(input("Enter radius: "))
    print("Area of Circle =", area.area_circle(r))

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    print("Area of Rectangle =", area.area_rectangle(l, w))
elif choice == 3:
    b = float(input("Enter the base length: "))
    h = float(input("Enter height: "))
    print ("Area of traingle is ", area.area_triangle(b, h))

else:
    print("Invalid choice!")