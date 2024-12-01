# Open and read the file
with open("test_input.txt") as file:
    lines = file.readlines()

# Parse into two lists
list_1 = []
list_2 = []
for line in lines:
    pair = line.strip().split()
    list_1.append(int(pair[0]))
    list_2.append(int(pair[1]))

# Sort
list_1.sort()
list_2.sort()

# Calculate differences
differences = [abs(a - b) for a, b in zip(list_1, list_2)]

# Sum up
total_distance = sum(differences)

print(f"The total distance between the lists is: {total_distance}")