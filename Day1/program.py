import os

def read_input(file_name: str) -> list[str]:
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as file:
        return file.readlines()


if __name__ == '__main__':
    
    input: list[str] = read_input('input')

    group1: list[int] = []
    group2: list[int] = []

    for line in input:
        num1, num2 = map(int, line.split())
        group1.append(num1)
        group2.append(num2)

    # Part 1
    result: int = 0
    zip_group: tuple[int, int] = zip(sorted(group1), sorted(group2))
    for num1, num2 in zip_group:
        diff: int = abs(num2 - num1)
        result += diff

    print(f"Part 1: {result}")
        

    # Part 2
    result: int = 0
    for num in group1:
        result += num * group2.count(num)
    
    print(f"Part 2: {result}")