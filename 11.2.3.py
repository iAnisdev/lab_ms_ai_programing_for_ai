side_a = int(input("Enter the length of side a: "))
side_b = int(input("Enter the length of side b: "))
side_c = int(input("Enter the length of side c: "))

# Check if the sides form a valid triangle by checking if the sum of the lengths of any two sides is greater than the length of the third side
is_valid_triangle = side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a

if not is_valid_triangle:
    print("This is not a valid triangle")
    exit()

# Check if the triangle is equilateral (all sides are equal), isosceles (two sides are equal), or scalene (no sides are equal)
is_equilateral = side_a == side_b == side_c
is_isosceles = side_a == side_b or side_a == side_c or side_b == side_c
is_scalene = side_a != side_b != side_c

if is_equilateral:
    print("This is an equilateral triangle")
elif is_isosceles:
    print("This is an isosceles triangle")
elif is_scalene:
    print("This is a scalene triangle")