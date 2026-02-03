"""
On selge, et auto kiiruse tõstmine vähendab sõidule kuluvat aega ehk ma jõuame varem sihtpunkti. Kui palju me aga ajas võidame? Koostage programm,
 mis küsib käivitamisel läbitava vahemaa pikkust (kilomeetrites, see kehtib kogu programmitöö aja),
seejärel aga küsib kasutajalt korduvalt kiirust (km/h) ning väljastab selle põhjal korrektse lausega sõiduks kuluva aja ja erinevuse eelmisest tulemusest.
Kui kasutaja uut kiirust ei sisesta, vaid vajutab lihtsalt sisestusklahvile, siis katkestatakse tsükkel ja tänatakse kasutajat.
"""


def speed_time():
    road_length = int(input("Vahemaa pikkust kilomeetrites?: "))
    speed = "0"
    old_time = 0
    while speed != 0:
        speed = input("Kiirus on (km/h)?: ")
        if not speed.isnumeric():
            break
        time_road = road_length / int(speed) * 60
        print(result_formating(time_road, old_time))
        old_time = time_road
    print("Aitah!")


def result_formating(time_road, old_time):
    hours, minute, seconds = converter_to_hours_min_sec(time_road)
    if old_time == 0:
        return f"Sõiduks kuluva aja Hours {hours}, minut {minute} sec {seconds:.1f}"
    else:
        return f"Uus  aeg on {time_road} min ja erinevuse eelmisest tulemusest {time_road - old_time} min"


def converter_to_hours_min_sec(time):
    hours = int(time // 60)
    remaining_min = time % 60
    minute = int(remaining_min)
    remaining_min = remaining_min % 60
    seconds = remaining_min
    return hours, minute, seconds


if __name__ == '__main__':
    speed_time()