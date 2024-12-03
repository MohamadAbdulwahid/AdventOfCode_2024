import os
import re

def read_input(file_name: str) -> str:
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as file:
        return file.read()

if __name__ == '__main__':
    input_str = read_input('input')
    
    pattern_mul = r"mul\((\d+),\s*(\d+)\)"
    pattern_do = r"do\(\)"
    pattern_dont = r"don't\(\)"
    
    # Part 1: Ignore do and don't instructions
    matches = re.findall(pattern_mul, input_str)
    total1 = sum(int(a) * int(b) for a, b in matches)
    
    # Part 2: Follow do and don't instructions
    mul_enabled = True
    total2 = 0
    
    # Split the input into tokens based on the patterns
    tokens = re.split(r"(do\(\)|don't\(\)|mul\(\d+,\s*\d+\))", input_str)
    
    for token in tokens:
        if re.match(pattern_do, token):
            mul_enabled = True
        elif re.match(pattern_dont, token):
            mul_enabled = False
        elif mul_enabled:
            matches = re.findall(pattern_mul, token)
            for a, b in matches:
                total2 += int(a) * int(b)
    
    print(f"Part1: {total1}")
    print(f"Part2: {total2}")