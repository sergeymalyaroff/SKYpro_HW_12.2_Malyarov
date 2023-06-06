from utils import arrs

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

def test_get_existing_index():
    array = [1, 2, 3, 4, 5]
    index = 2
    default_value = "Not found"  # Добавлено объявление переменной default_value
    expected_value = 3

    result = arrs.get(array, index, default=default_value)
    assert result == expected_value



def test_get_non_existing_index():
    array = [1, 2, 3, 4, 5]
    index = 5
    default_value = "Not found"
    expected_value = "Not found"

    result = arrs.get(array, index, default=default_value)
    assert result == expected_value

def test_my_slice_default_arguments():
    array = [1, 2, 3, 4, 5]
    expected_result = [1, 2, 3, 4, 5]

    result = arrs.my_slice(array)
    assert result == expected_result

def test_my_slice_with_start_index():
    array = [1, 2, 3, 4, 5]
    start = 2
    expected_result = [3, 4, 5]

    result = arrs.my_slice(array, start=start)
    assert result == expected_result

def test_my_slice_with_end_index():
    array = [1, 2, 3, 4, 5]
    end = 3
    expected_result = [1, 2, 3]

    result = arrs.my_slice(array, end=end)
    assert result == expected_result

def test_my_slice_with_negative_start_and_end():
    array = [1, 2, 3, 4, 5]
    start = -3
    end = -1
    expected_result = [3, 4]

    result = arrs.my_slice(array, start=start, end=end)
    assert result == expected_result
