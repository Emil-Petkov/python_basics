lab_length = float(input()) * 100
lab_width = float(input()) * 100

length_work_place = 120
width_work_place = 70

corridor = 100

work_places_length = lab_length // length_work_place
work_places_width = (lab_width - corridor) // width_work_place

total_work_places_in_lab = work_places_length * work_places_width - 3

print(total_work_places_in_lab)
