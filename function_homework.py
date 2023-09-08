
def filter_string(input_string) -> list:
    result = []
    count = 0
    symbol = 0
    while symbol < len(input_string) and count < 100:
        char = input_string[symbol].lower()
        if char != 'm' and char != 'n':
            result.append(input_string[symbol])
            count += 1
        symbol += 1
    return result
