import math

# functions
def statement_generator(statement, decoration, amount=3):
    """Emphasises headings by adding decoration at the start and end"""
    return f"{decoration * amount} {statement} {decoration * amount}\n"

def string_checker(question, valid_ans=("yes", "no"), num_letters = 1):
    """Checks that users enter a full word
     or the 'n' letters of a word from a list of valid responses"""

    while True:
        response = input(question).lower()

        for item in valid_ans:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans}")

def num_checker(question, num_type="float", exit_code=None):
    """Checks that response is a float / integer more than zero"""

    if num_type == "float":
        error = "Please enter a number greater than 0."
    else:
        error = "Please enter an integer greater than 0."

    while True:
        response = input(question)

        if response == exit_code:
            return response
        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def cuboid():
    """Calculates the volume and surface area of a cuboid using the formula with what the user inputted"""
    cuboid_volume = length * width * height
    cuboid_surface_area = 2 * (length * width + width * height + length * height)
    print(f"Cuboid volume: {cuboid_volume:.2f}\nCuboid surface area: {cuboid_surface_area:.2f}")

def cylinder():
    """Calculates the volume and surface area of a cylinder using the formula with what the user inputted"""
    cylinder_volume = π * radius ** 2 * height
    cylinder_surface_area = 2 * (π * radius * height) + 2 * (π * radius ** 2)
    print(f"Cylinder volume: {cylinder_volume:.2f}\nCylinder surface area: {cylinder_surface_area:.2f}")

def triangularprism():
    """Calculates the volume and surface area of a triangular prism using the formula with what the user inputted"""
    triangular_prism_volume = (1/2) * width * height * length
    triangular_prism_surface_area = "yet to be coded"
    print(f"Triangular prism volume: {triangular_prism_volume:.2f}\nTriangular prism surface area: {triangular_prism_surface_area:.2f}")

def cone():
    """Calculates the volume and surface area of a cone using the formula with what the user inputted"""
    cone_volume = (1/3) * π * radius ** 2 * height
    cone_surface_area = π * radius * (radius + math.sqrt(height ** 2 + radius ** 2))
    print(f"Cone volume: {cone_volume:.2f}\nCone surface area: {cone_surface_area:.2f}")

def sphere():
    """Calculates the volume and surface area of a sphere using the formula with what the user inputted"""
    sphere_volume = (4 / 3) * π * radius ** 3
    sphere_surface_area = 4 * π * radius ** 2
    print(f"Sphere volume: {sphere_volume:.2f}\nSphere surface area: {sphere_surface_area:.2f}")

def squarepyramid():
    """Calculates the volume and surface area of a square based pyramid using the formula with what the user inputted"""
    square_pyramid_volume = (width ** 2) * (height / 3)
    square_pyramid_surface_area = width ** 2 + 2 * width * math.sqrt(((width ** 2) / 4) + height ** 2)
    print(f"Square based pyramid volume: {square_pyramid_volume:.2f}\nSquare based pyramid surface area: {square_pyramid_surface_area:.2f}")

def trianglepyramid():
    """Calculates the volume and surface area of a triangle based pyramid using the formula with what the user inputted"""
    triangle_pyramid_volume = (1/3) * area * height
    triangle_pyramid_surface_area = area + (1/2) * (perimeter * height)
    print(f"Triangle based pyramid volume: {triangle_pyramid_volume:.2f}\nTriangle based pyramid surface area: {triangle_pyramid_surface_area:.2f}")

# variables & lists
π = math.pi
height_shapes = ["cuboid", "cylinder", "triangularprism", "cone", "squarepyramid", "trianglepyramid"]
length_shapes = ["cuboid", "triangularprism"]
width_shapes = ["cuboid", "squarepyramid", "trianglepyramid", "squarepyramid", "trianglepyramid"]
radius_shapes = ["cylinder", "cone", "sphere"]

# main routine
shape = string_checker(f"Which shape? ", ("cuboid", "cylinder", "triangularprism", "cone", "sphere", "squarepyramid", "trianglepyramid"), None)


if shape in height_shapes:
    height = num_checker(f"Height: ")
if shape in length_shapes:
    length = num_checker(f"Length: ")
if shape in width_shapes:
    width = num_checker(f"Width: ")
if shape in radius_shapes:
    radius = num_checker(f"Radius: ")
if shape == "trianglepyramid":
    area = num_checker("Base area: ")
    perimeter = num_checker(f"Base perimeter: ")

exec(f"{shape}()")



