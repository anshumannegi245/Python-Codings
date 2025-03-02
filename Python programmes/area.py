def display_menu():
    print("\nMenu:")
    print("1. Calculate Area of a Circle")
    print("2. Calculate Area of a Rectangle")
    print("3. Calculate Area of a Triangle")
    print("4. Exit")

def calculate_circle_area(radius):
    import math
    return math.pi * radius**2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        try:
            choice = int(choice)  # Convert input to integer

            if choice == 1:
                radius = float(input("Enter the radius of the circle: "))
                area = calculate_circle_area(radius)
                print("Area of the circle:", area)

            elif choice == 2:
                length = float(input("Enter the length of the rectangle: "))
                width = float(input("Enter the width of the rectangle: "))
                area = calculate_rectangle_area(length, width)
                print("Area of the rectangle:", area)

            elif choice == 3:
                base = float(input("Enter the base of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                area = calculate_triangle_area(base, height)
                print("Area of the triangle:", area)

            elif choice == 4:
                print("Exiting program.")
                break  # Exit the loop

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
