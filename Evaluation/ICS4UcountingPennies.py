def is_point_in_circle(x, y, R):
    # Check if the point (x, y) is inside the circle with radius R centered at the origin
    return x**2 + y**2 <= R**2

def count_pennies_recursive(x, y, R, count):
    # Base case: if x exceeds the radius, return the count
    if x > R:
        return count
    # If y exceeds the radius, reset y to -R and move to the next x-coordinate
    if y > R:
        return count_pennies_recursive(x + 1, -R, R, count)
    # Check if the current point (x, y) is inside the circle
    if is_point_in_circle(x, y, R):
        count += 1
    # Recursive call for the next point (x, y + 1)
    return count_pennies_recursive(x, y + 1, R, count)

def count_pennies(R):
    # Start recursion from point (-R, -R)
    return count_pennies_recursive(-R, -R, R, 0)

# Input radius
radius = int(input("Enter the radius of the circle: "))
result = count_pennies(radius)
print("Number of pennies that fit inside the circle: ", result)


#The code checks if \( x^2 + y^2 \leq R^2 \) for each point `(x, y)` in the grid. 
# If true, the point is inside the circle and the count is incremented. 
# The recursion moves through the grid by adjusting `x` and `y`.