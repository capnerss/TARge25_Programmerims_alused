"""
Ülesanne 1
Loo fail tuttavad.txt ja lisa sinna vähemalt 6 tuttava perekonna- ja eesnimed (iga tuttav uuele reale, perekonna- ja eesnimi tühikuga eraldatult).
Koosta programm, mis loeb failist andmed ja väljastab need ekraanile tähestikulises järjekorras.
Mõistlik on ilmselt kasutada järjendit ja sellega seonduvaid võimalusi (järjestamist). Tähestikulises järjekorras salvestage tuttavate nimed ka uude faili tuttavad1.txt.
"""

people = ["Juri Saki", "Riho Sepp", "Kivi Kangur", "Vasja Pupkin", "John Doe", "Jane Doe"]
def preparation(fail_name, list_of_names):
    """Loo fail tuttavad.txt , lisa sinna vähemalt 6 tuttava perekonna- ja eesnimed (iga tuttav uuele reale, perekonna- ja eesnimi tühikuga eraldatult). """

    with open(fail_name, "w") as a:
        for i in list_of_names:
            a.write(i+"\n")
            print(i)


def read_names(file_name):
    result = []
    with open(file_name, "r") as f:
        for line in f:
            name = line.strip()
            if len(line) > 0:
                result.append(name)
        print(result)
        return result


def sort_names():
    names_list = []
    new_list = sorted(read_names("tuttavad.txt"))
    print(new_list)
    return new_list


if __name__ == '__main__':
    preparation("tuttavad.txt", people)
    preparation("tuttavad.txt", sort_names())
