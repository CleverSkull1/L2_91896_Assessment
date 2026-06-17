import math
import pandas
from tabulate import tabulate as tabulate

# functions
def statement_generator(statement, decoration, amount=3):
    """Emphasises headings by adding decoration at the start and end"""
    return f"{decoration * amount} {statement} {decoration * amount}\n"

def string_checker(question, valid_ans=("yes", "no"), num_letters=1):
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

def remove_trails(value):
    """Removes trailing zeroes from full numbers while still rounding decimal numbers to 2 decimal points"""
    if int(value) == float(value):
        return f"{int(value)}"
    else:
        return f"{value:.2f}"

def cuboid():
    """Calculates the volume and surface area of a cuboid using the formula with what the user inputted"""
    volume = length * width * height
    surface_area = 2 * (length * width + width * height + length * height)
    print(f"\nCuboid volume: {remove_trails(volume)}{unit}³\nCuboid surface area: {remove_trails(surface_area)}{unit}²")
    volumes.append(f"{remove_trails(volume)}{unit}³")
    surface_areas.append(f"{remove_trails(surface_area)}{unit}²")

def cylinder():
    """Calculates the volume and surface area of a cylinder using the formula with what the user inputted"""
    volume = (π * radius ** 2) * height
    surface_area = 2 * (π * radius * height) + 2 * (π * radius ** 2)
    print(f"Cylinder volume: {remove_trails(volume)}{unit}³\nCylinder surface area: {remove_trails(surface_area)}{unit}²")
    volumes.append(f"{remove_trails(volume)}{unit}³")
    surface_areas.append(f"{remove_trails(surface_area)}{unit}²")

def triangular_prism():
    """Calculates the volume and surface area of a triangular prism using the formula with what the user inputted"""
    volume = (1 / 2) * side_a * side_b * length
    surface_area = (side_a * length) + (side_b * length) + (side_c * length) + (side_b * side_a)
    print(f"Triangular prism volume: {remove_trails(volume)}{unit}³\nTriangular prism surface area: {remove_trails(surface_area)}{unit}²")
    volumes.append(f"{remove_trails(volume)}{unit}³")
    surface_areas.append(f"{remove_trails(surface_area)}{unit}²")

def cone():
    """Calculates the volume and surface area of a cone using the formula with what the user inputted"""
    volume = (1 / 3) * π * radius ** 2 * height
    surface_area = π * radius * (radius + math.sqrt(height ** 2 + radius ** 2))
    print(f"Cone volume: {remove_trails(volume)}{unit}³\nCone surface area: {remove_trails(surface_area)}{unit}²")
    volumes.append(f"{remove_trails(volume)}{unit}³")
    surface_areas.append(f"{remove_trails(surface_area)}{unit}²")

def sphere():
    """Calculates the volume and surface area of a sphere using the formula with what the user inputted"""
    volume = (4 / 3) * π * radius ** 3
    surface_area = 4 * π * radius ** 2
    print(f"Sphere volume: {remove_trails(volume)}{unit}³\nSphere surface area: {remove_trails(surface_area)}{unit}²")
    volumes.append(f"{remove_trails(volume)}{unit}³")
    surface_areas.append(f"{remove_trails(surface_area)}{unit}²")

def square_pyramid():
    """Calculates the volume and surface area of a square based pyramid using the formula with what the user inputted"""
    volume = (width ** 2) * (height / 3)
    surface_area = width ** 2 + 2 * width * math.sqrt(((width ** 2) / 4) + height ** 2)
    print(f"Square based pyramid volume: {remove_trails(volume)}{unit}³\nSquare based pyramid surface area: {remove_trails(surface_area)}{unit}²")
    volumes.append(f"{remove_trails(volume)}{unit}³")
    surface_areas.append(f"{remove_trails(surface_area)}{unit}²")

def triangle_pyramid():
    """Calculates the volume and surface area of a triangle based pyramid using the formula with what the user inputted"""
    volume = (1/3) * area * height
    surface_area = area + (1/2) * (perimeter * height)
    print(f"Triangle based pyramid volume: {remove_trails(volume)}{unit}³\nTriangle based pyramid surface area: {remove_trails(surface_area)}{unit}²")
    volumes.append(f"{remove_trails(volume)}{unit}³")
    surface_areas.append(f"{remove_trails(surface_area)}{unit}²")

# variables & lists
π = math.pi
height_shapes = ["cuboid", "cylinder", "cone", "square_pyramid", "triangle_pyramid"]
length_shapes = ["cuboid", "triangular_prism"]
width_shapes = ["cuboid", "square_pyramid", "triangle_pyramid"]
radius_shapes = ["cylinder", "cone", "sphere"]
shapes = []
volumes = []
surface_areas = []

# main routine
while True:

    # asks the user which shape they would like to calculate and replaces the spaces with underscores because functions can't have spaces
    shape = string_checker("Which shape? ", ("cuboid", "cylinder", "triangular prism", "cone", "sphere",
                                              "square pyramid", "triangle pyramid", "xxx"), None)
    if shape == "xxx":
        break
    shape = shape.replace(" ", "_")

    # asks the user which unit they would like to use
    unit = string_checker("Which unit? ", ("cm", "m", "mm", "km"), None)
    print()

    # decides what parameters to ask the user based on the shape they selected
    if shape in height_shapes:
        height = num_checker("Height: ")
    if shape in length_shapes:
        length = num_checker("Length: ")
    if shape in width_shapes:
        width = num_checker("Width: ")
    if shape in radius_shapes:
        radius = num_checker("Radius: ")
    if shape == "triangle_pyramid":
        area = num_checker("Base area: ")
        perimeter = num_checker("Base perimeter: ")
    if shape == "triangular_prism":
        side_a = num_checker("Side A: ")
        side_b = num_checker("Side B: ")
        side_c = num_checker("Side C: ")

    # runs the calculation function based on the shape the user selected
    exec(f"{shape}()")

    # puts the shape and units into a list to call later
    shapes.append(shape)
    print()

print()
calculations_panda = {
    "Shape": shapes,
    "Volume": volumes,
    "Surface Area": surface_areas
}

panda = tabulate(pandas.DataFrame(calculations_panda), headers='keys', tablefmt='psql', showindex=False)
print(panda)