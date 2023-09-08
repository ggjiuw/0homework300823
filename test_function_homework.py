from function_homework import filter_string

def test_n_filter():
    expected_result = ['1', '2', '3', ' ', ' ', 'a', 'b', ' ']
    input_string = 'n123 N ab n'
    actual_result = filter_string(input_string)
    assert expected_result == actual_result


def test_m_filter():
    expected_result = ['1', '2', '3', ' ', ' ', 'a', 'b', ' ']
    input_string = 'm123 M ab m'
    actual_result = filter_string(input_string)
    assert expected_result == actual_result
