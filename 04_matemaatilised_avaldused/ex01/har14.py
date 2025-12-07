"""Dictionary exercises."""


def get_hobbies(hobbies_dict: dict, name: str) -> list:
    """
    Return the hobbies of a given person.

    hobbies = {
    "Tom": ["running", "reading"],
    "John": ["movies", "music", "swimming"]
    }

    get_hobbies(hobbies, "Tom")  => ["running", "reading"]
    get_hobbies(hobbies, "Timmy")  => "name not in dictionary"

    :param hobbies_dict: dictionary with peoples' hobbies.
    :param name: name of person whose hobbies are to be returned.

    :return: List of hobbies of the person with given name or "name not in dictionary".
    """
    list_of_hobbies = "name not in dictionary"
    if name in hobbies_dict:
        list_of_hobbies = list(hobbies_dict[name])
    return list_of_hobbies


def find_tallest(height_dict: dict) -> str:
    """
    Return the name of the tallest peron in given dictionary.

    find_tallest({"Tom": 186, "Mari": 175, "Jhon": 190}) => "Jhon"

    :param height_dict: dictionary with peoples' names and heights
    :return name of tallest person in given dict.
    """
    name_of_tallest = ""
    for a, b in height_dict.items():
        if b == sorted(height_dict.values(), reverse=True)[0]:
            name_of_tallest = a
    return name_of_tallest


def remove_sixes(six_dict: dict) -> dict:
    """
    Return a dictionary where all keys which's values are dividable by six are removed.

    remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}) => {"a": 4, "b": 8}

    :param six_dict: dictionary to be modified.
    :return: dict without values that are dividable by six.
    """
    dict_without_six = {}
    for k, v in six_dict.items():
        if v % 6 != 0:
            dict_without_six[k] = v
    return dict_without_six


def exchange_keys_and_values(exchange_dict: dict) -> dict:
    """
    Return a dict where keys and values have been exchanged.

    exchange_keys_and_values({"a": "b", "c": "d"}) => {"b": "a", "d": "c"}

    :param exchange_dict: dictionary to be modified.
    :return dictionary where values and keys have been exchanged.
    """
    value_keys_exchanged = {}
    for k, v in exchange_dict.items():
        value_keys_exchanged[v] = k
    return value_keys_exchanged


def count_symbol_appearances(stringy: str) -> dict:
    """
    Return dict where key is the symbol and the value is the count this symbol is present in the string.

    count_symbol_appearances("hello hi") => {'h': 2, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'i': 1}

    :param stringy: string to be processed.
    :return: dictionary with symbol counts.
    """
    symbol_dict = {}
    for i in stringy:
        symbol_dict[i] = stringy.count(i)
    return symbol_dict


def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where key the is a symbol and the value is a list of words starting with this symbol.

    organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]) =>
        {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}

    :param strings: list of strings.
    :return: dict with starting symbol and corresponding words in order of appearance.
    """
    starting_symbols_dict = {}
    for i in strings:
        first_symbol = i[0]
        if first_symbol in starting_symbols_dict:
            starting_symbols_dict[first_symbol].append(i)
        else:
            starting_symbols_dict[first_symbol] = [i]
    return starting_symbols_dict