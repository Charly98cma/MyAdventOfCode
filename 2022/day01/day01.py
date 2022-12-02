def process_input():
    with open('input.txt', 'r') as in_file:
        calories = []
        cal_sum = 0
        for line in in_file:
            line = line.strip()
            if not line:
                calories.append(cal_sum)
                cal_sum = 0
            else:
                cal_sum += int(line)
    return sorted(calories)

def hightest_calories(calories_list: list, n_elfs: int = 1):
    return sum(calories_list[-n_elfs:])


def main():
    calories_list = process_input()
    print(hightest_calories(calories_list))
    print(hightest_calories(calories_list, 3))


if __name__ == "__main__":
    main()