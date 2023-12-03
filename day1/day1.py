def get_value_from_input(file_path):
    _sum = 0;

    with open(file_path, 'r') as file:
        for text in file:
            value = f"{get_first_number(text)}{get_last_number(text)}"
            _sum += int(value)

    return _sum


def get_first_number(s: str):
    for char in s:
        if char.isdigit():
            return int(char)
    return None


def get_last_number(s):
    last_digit = 0;
    for char in s:
        if char.isdigit():
            last_digit = char
    return last_digit


if __name__ == "__main__":
    file_path = "day1/input.txt"
    value = get_value_from_input(file_path)
    print(f"The sum of the input is: {value}")