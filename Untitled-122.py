def print_floyds_triangle(num_rows):
    current_value = 1
    for row in range(1, num_rows + 1):
        for col in range(row):
            print(current_value, end=" ")
            current_value = 1 - current_value
        print()

num_rows = int(input("Number of rows: "))

print_floyds_triangle(num_rows)
