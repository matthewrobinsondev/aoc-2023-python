def get_value_from_input(file_path):
    _sum = 0

    with open(file_path, 'r') as file:
        for text in file:
            first_number_value = get_number(text, 'First')
            last_number_value = get_number(text, 'Last')
            value = f"{first_number_value}{last_number_value}"
            _sum += int(value)

    return _sum


def get_number(text: str, option: str):
    final_number = 0
    previous_number = 0
    loop = 0
    array_key = 'after_number'

    if option == 'First':
        array_key = 'before_number'

    while loop == 0:
        response = check_for_written_numbers(text)
        if response['found_number'] is not None:
            previous_number = response['found_number']

        if response[array_key] is not None:
            text = response[array_key]

        if response.get('found_number') is None and response.get(array_key) is None:
            final_number = previous_number
            loop = 1

    if len(text) >= 1:
        result = check_for_number_in_haystack(text, option)
        if result is not None:
            final_number = result

    if isinstance(final_number, str) and len(final_number) >= 3:
        final_number = get_mapped_string_value(final_number)

    return final_number


def get_mapped_string_value(input_string: str):
    number_mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # Check if the input string is a valid key in the mapping
    return number_mapping.get(input_string, None)


def check_for_number_in_haystack(text: str, option: str):
    if option == 'First':
        final_number = get_first_number(text)
        return final_number

    return get_last_number(text)


def get_first_number(text: str):
    for char in text:
        if char.isdigit():
            return int(char)
    return None


def get_last_number(text: str):
    last_digit = None
    for char in text:
        if char.isdigit():
            last_digit = char
    return last_digit


def check_for_written_numbers(text: str):
    written_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    found_number = None

    for number_value in written_numbers:
        index = text.find(number_value)
        if index != -1:
            found_number = number_value
            break

    if found_number is not None:
        before_subset = text[:index + 1]
        after_subset = text[index + len(found_number) - 1:]

        return {
            'found_number': found_number,
            'before_number': before_subset,
            'after_number': after_subset
        }

    else:

        return {
            'found_number': None,
            'before_number': None,
            'after_number': None
        }


if __name__ == "__main__":
    file_path = "day2/input.txt"
    value = get_value_from_input(file_path)
    print(f"The sum of the input is: {value}")
