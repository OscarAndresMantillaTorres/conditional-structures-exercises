def triangle_type(a, b, c):
    # Check if the triangle is valid
    if a + b > c and a + c > b and b + c > a:
        # Determine the type of triangle
        if a == b == c:
            return "The triangle is equilateral."
        elif a == b or a == c or b == c:
            return "The triangle is isosceles."
        else:
            return "The triangle is scalene."
    else:
        return "It is not a valid triangle."

# Loop to receive user input
while True:
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        # Check the type of triangle and display the result
        result = triangle_type(a, b, c)
        print(result)

        # Ask if the user wants to continue
        continue_input = input("Do you want to enter another set of sides? (yes/no): ")
        if continue_input.lower() != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
