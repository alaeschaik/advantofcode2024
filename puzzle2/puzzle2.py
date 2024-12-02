def safe(report):
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    for i in range(len(report) - 1):
        if not (1 <= abs(report[i] - report[i + 1]) <= 3):
            return False
    return True

def safe_2(report):
    if safe(report):
        return True
    for i in range(len(report)):
        temp_report = report[:i] + report[i + 1:]
        if safe(temp_report):
            return True
    return False

def main():
    with open('input.txt') as f:
        reports = [[int(x) for x in line.split()] for line in f if line.strip()]

    answer_part_1 = sum(1 for report in reports if safe(report))
    print(f'answer to part 1 is {answer_part_1}')

    answer_part_2 = sum(1 for report in reports if safe_2(report))
    print(f'answer to part 2 is {answer_part_2}')

if __name__ == "__main__":
    main()