def training_lab(length_in_meters: float, width_in_meters: float):
    length_in_centimeters = length_in_meters * 100
    width_in_centimeters = width_in_meters * 100

    one_work_place_length = 120  # cm.
    one_work_place_width = 70  # cm.

    corridor = 100  # cm.

    total_work_places_length = length_in_centimeters // one_work_place_length
    total_work_places_width = (width_in_centimeters - corridor) // one_work_place_width

    total_work_places = total_work_places_length * total_work_places_width - 3  # work places

    return f'{total_work_places:.0f}'


length = float(input())
width = float(input())
print(training_lab(length, width))
