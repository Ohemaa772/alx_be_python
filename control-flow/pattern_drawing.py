
# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop: iterate through each row using a while loop
while row < size:
    # Inner loop: print '*' in each column of the row
    for col in range(size):
        print("*", end="")
    # Move to the next line after finishing the row
    print()
    # Increment row counter
    row += 1

