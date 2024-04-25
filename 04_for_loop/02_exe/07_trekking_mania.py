n_groups = int(input())
musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

total_peoples = 0

for _ in range(n_groups):
    n_peoples_in_group = int(input())

    total_peoples += n_peoples_in_group

    if n_peoples_in_group <= 5:
        musala += n_peoples_in_group

    elif n_peoples_in_group <= 12:
        mont_blanc += n_peoples_in_group

    elif n_peoples_in_group <= 25:
        kilimanjaro += n_peoples_in_group

    elif n_peoples_in_group <= 40:
        k2 += n_peoples_in_group

    elif n_peoples_in_group >= 41:
        everest += n_peoples_in_group

print(f'{(musala / total_peoples) * 100:.2f}%\n'
      f'{(mont_blanc / total_peoples) * 100:.2f}%\n'
      f'{(kilimanjaro / total_peoples) * 100:.2f}%\n'
      f'{(k2 / total_peoples) * 100:.2f}%\n'
      f'{(everest / total_peoples) * 100:.2f}%\n')
