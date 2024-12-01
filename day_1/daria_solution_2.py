from collections import Counter

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

# Find unique values in list_1 and count occurrences in list_2
unique_list_1 = set(list_1)
print(unique_list_1)
count_list_2 = Counter(list_2)
print(count_list_2)

# Calculate similarity score
similarity_score = sum(i * count_list_2[i] for i in unique_list_1)

print(f"The similarity score is: {similarity_score}")