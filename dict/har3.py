"""
Ülesanne 3
Loo juurde kaks uut sõnastiku (e_inglise, e_itaalia), mille võti ei ole mitte eesti keeles,
vaid vastavalt kas inglise või itaalia keeles. Lisa sõnastikku ka kõik eelmises sõnastikus olevad sõnad.
"""
from har1 import english_dict, italia_dict


def swap_dict_key_value(original_dict):
    new_dict = {}
    for key, value in original_dict.items():
        new_dict[value] = key
    return new_dict


english_eesti_dict = swap_dict_key_value(english_dict)
italia_eesti_dict = swap_dict_key_value(italia_dict)


if __name__ == '__main__':
    print(italia_eesti_dict)
    print(english_eesti_dict)