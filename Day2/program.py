import os
def read_input(file_name: str) -> list[str]:
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as file:
        return file.readlines()

reports = []
for line in read_input('input'):
    reports.append([int(x) for x in line.split(' ')])

def safe(report):
    if report != sorted(report) and report != sorted(report)[::-1]:
        return False
    for i  in range(len(report)-1):
        if not 1 <= abs(report[i]-report[i+1]) <= 3:
            return False
    return True 


answer = sum([1 for report in reports if safe(report) ])
print(f'Part1: {answer}')

def safe_2(report):
    if safe(report):
        return True
    for i in range(len(report)):
        temp_report = report[:i] + report[i+1:]
        if safe(temp_report):
            return True
    return False

answer = sum([1 for report in reports if safe_2(report) ])
print(f'Part2: {answer}')