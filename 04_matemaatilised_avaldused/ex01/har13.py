"""Basic list operations."""


def create_list_of_two_elements(a: int, b: int) -> list:
    """
    Return list of two elements a and b (in that order).

    create_list_of_two_elements(1, 2) => [1, 2]
    create_list_of_two_elements(81, 72) => [81, 72]
    """
    return [a, b]


def create_list_with_edge_elements(elements: list) -> list:
    """
    Create a new list with 2 elements: the first and the last element.

    The initial list has at least one element.
    If the initial list has only one element, the same element is
    both the first and the last element.

    create_list_with_edge_elements([1, 2, 3]) => [1, 3]
    create_list_with_edge_elements([1]) => [1, 1]
    create_list_with_edge_elements(["a", "b"]) => ["a", "b"]
    create_list_with_edge_elements(["a", "b", "c", "d", "f"]) => ["a", "f"]
    """
    return [elements[0], elements[-1]]


def get_middle_element_of_list(elements: list) -> any:
    """
    Return the middle element in the list with odd number of element.

    The list always has odd number of elements.
    get_middle_element_of_list([1]) = 1
    get_middle_element_of_list([1, 2, 3]) => 2
    get_middle_element_of_list(["a", "b", "c"]) => "b"
    """
    return elements[len(elements) // 2]


def get_middle_part_of_list(elements: list) -> list:
    """
    Create a new list of the input list where the first and the last element are removed.

    The initial list has at least 2 elements (don't have to validate that).

    get_middle_part_of_list([1, 2, 3]) => [2]
    get_middle_part_of_list([1, 3]) => []
    get_middle_part_of_list([1, 3, 6, 7]) => [3, 6]
    get_middle_part_of_list(["a", "b", "b", "a"]) => ["b", "b"]
    """
    return elements[1:-1]


def create_new_list_with_added_number(numbers: list, number: int) -> list:
    """
    Return a new list where a number has been added.

    Do not modify the existing list.
    create_new_list_with_added_number([1, 2, 3], 4) => [1, 2, 3, 4]
    """
    new_list_with_added_number = numbers.copy()
    new_list_with_added_number.append(number)
    return new_list_with_added_number


def swap_edge_elements(elements: list) -> list:
    """
    Swap the first and the last element.

    List always has at least 2 elements.
    Elements can be either numbers or strings.

    swap_edge_elements([1, 2, 3]) => [3, 2, 1]
    swap_edge_elements([1, 2]) => [2, 1]
    swap_edge_elements([1, 2, 1, 4]) => [4, 2, 1, 1]
    swap_edge_elements(["foo", "bar", "pub"]) => ["pub", "bar", "foo"]

    """
    first_element, last_element = elements[0], elements[-1]
    elements[0], elements[-1] = last_element, first_element
    return elements


def add_element_in_position(elements: list, new_element: any, position: int) -> list:
    """
    Add a new element into the list into the specified position.

    The position is always valid.
    The elements on the position and on the right are shifted by one.

    add_element_in_position([1, 2, 3], 2, 2) => [1, 2, 2, 3]
    add_element_in_position([1], 9, 0) => [9, 1]
    add_element_in_position([1], 9, 1) => [1, 9]
    """
    elements.insert(position, new_element)
    return elements


def get_repeated_list(elements: list, repetiton: int) -> list:
    """
    Repeat the elements by certain amount of times.

    get_repeated_list([1, 2], 2) => [1, 2, 1, 2]
    get_repeated_list([1], 5) => [1, 1, 1, 1, 1]
    get_repeated_list([1, 2], 0) => []
    """
    return elements * repetiton


def remove_first_element_from_list(elements: list) -> None:
    """
    Remove the first element of the list.

    The list will be modified, nothing is returned.
    There is at least 1 element in the list.

    x = [1, 2, 3]
    remove_first_element_from_list(x)
    x => [2, 3]
    """
    return elements.remove(elements[0])


def reverse_list(elements: list) -> list:
    """
    Return reversed list.

    reverse_list([1, 2, 3]) => [3, 2, 1]
    reverse_list(["a", "b"]) => ["b", "a"]
    """
    return elements[::-1]


if __name__ == "__main__":
    assert create_list_of_two_elements(1, 2) == [1, 2]
    assert create_list_of_two_elements(81, 72) == [81, 72]
    assert create_list_with_edge_elements([1, 2, 3]) == [1, 3]
    assert create_list_with_edge_elements([1]) == [1, 1]
    assert create_list_with_edge_elements(["a", "b"]) == ["a", "b"]
    assert create_list_with_edge_elements(["a", "b", "c"]) == ["a", "c"]
    assert create_list_with_edge_elements(["a", "b", "c", "d"]) == ["a", "d"]
    assert get_middle_element_of_list([1]) == 1
    assert get_middle_element_of_list([1, 2, 3]) == 2
    assert get_middle_element_of_list(["a", "b", "c"]) == "b"
    assert get_middle_part_of_list([1, 2, 3]) == [2]
    assert get_middle_part_of_list([1, 3]) == []
    assert get_middle_part_of_list([1, 3, 6, 7]) == [3, 6]
    assert get_middle_part_of_list(["a", "b", "b", "a"]) == ["b", "b"]
    assert create_new_list_with_added_number([1, 2, 3], 4) == [1, 2, 3, 4]
    assert swap_edge_elements([1, 2, 3]) == [3, 2, 1]
    assert swap_edge_elements([1, 2]) == [2, 1]
    assert swap_edge_elements([1, 2, 1, 4]) == [4, 2, 1, 1]
    assert swap_edge_elements(["foo", "bar", "pub"]) == ["pub", "bar", "foo"]
    assert add_element_in_position([1, 2, 3], 2, 2) == [1, 2, 2, 3]
    assert add_element_in_position([1], 9, 0) == [9, 1]
    assert add_element_in_position([1], 9, 1) == [1, 9]
    assert get_repeated_list([1, 2], 2) == [1, 2, 1, 2]
    assert get_repeated_list([1], 5) == [1, 1, 1, 1, 1]
    assert get_repeated_list([1, 2], 0) == []
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list(["a", "b"]) == ["b", "a"]