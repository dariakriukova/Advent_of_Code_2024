with open('day_19/test_input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

def can_create_design(design, patterns):
    if not design:
        return True
    for pattern in patterns:
        if design.startswith(pattern):
            if can_create_design(design[len(pattern):], patterns):
                return True
    return False

patterns = lines[0].split(', ')
designs = lines[2:]

possible_designs = sum(can_create_design(design, patterns) for design in designs)

print(f"Number of possible designs: {possible_designs}")
