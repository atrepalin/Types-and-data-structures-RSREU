from math import fabs

MAX_SECTIONS = 1000000
EPSILON = 1e-7

section_stack = [0 for _ in range(MAX_SECTIONS)]

def get_top_section_height():
    global stack_start, stack_end, heights
    assert stack_start < stack_end
    return heights[section_stack[stack_start]]

def pop_from_stack():
    global stack_start
    assert stack_start < stack_end
    stack_start += 1
    return section_stack[stack_start - 1]

def push_to_stack(section_index):
    global stack_end, stack_start, heights
    while (
        stack_start < stack_end
        and heights[section_stack[stack_end - 1]] < heights[section_index]
    ):
        stack_end -= 1
    section_stack[stack_end] = section_index
    stack_end += 1

def redistribute_water(num_sections, initial_water_volume):
    global stack_start, stack_end, heights, water_levels
    water_levels = [0 for _ in range(num_sections)]
    stack_start = 0
    stack_end = 0
    current_section = 0
    next_section = 1
    remaining_water = initial_water_volume
    transferred_water = 0
    push_to_stack(0)
    while (
        next_section < num_sections
        and current_section < next_section
        and remaining_water > (heights[next_section - 1] + EPSILON)
    ):
        water_transfer_1 = (
            (remaining_water - transferred_water)
            * (next_section - current_section)
            / (next_section - current_section + 1)
        )
        if stack_start < stack_end:
            water_transfer_2 = (remaining_water - get_top_section_height()) * (
                next_section - current_section
            )
            water_transfer = min(water_transfer_2, water_transfer_1)
        else:
            water_transfer = water_transfer_1
        remaining_water -= water_transfer / (next_section - current_section)
        transferred_water += water_transfer
        if fabs(remaining_water - transferred_water) < EPSILON:
            push_to_stack(next_section)
            next_section += 1
            transferred_water = 0
        if fabs(remaining_water - get_top_section_height()) < EPSILON:
            last_section = pop_from_stack()
            while current_section <= last_section:
                water_levels[current_section] = remaining_water
                current_section += 1
            current_section = last_section + 1
        if (current_section == next_section) or (
            remaining_water < heights[next_section - 1] + EPSILON
        ):
            while current_section < next_section:
                water_levels[current_section] = remaining_water
                current_section += 1
            remaining_water = transferred_water
            transferred_water = 0
            current_section = next_section
            push_to_stack(next_section)
            next_section += 1
    while current_section < next_section:
        water_levels[current_section] = remaining_water
        current_section += 1
    for i in range(num_sections):
        print(f"{water_levels[i]:.6f}")

n, C = input().split()
n = int(n)
C = float(C)

heights = [0 for _ in range(MAX_SECTIONS)]
for i in range(n - 1):
    heights[i] = int(input())

redistribute_water(n, C)
