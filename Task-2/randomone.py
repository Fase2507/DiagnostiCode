def bul(girdi, aran):
    if aran in girdi:
        print(f'{aran} var')
        if girdi.count(aran) > 0:
            sayac = girdi.count(aran)
            print(f'"{girdi}" içinde {sayac} tane {aran} var')
            girdi = girdi.replace(aran, f'\033[33m{aran}\033[0m')
            print(f"{girdi}")

    else:
        print('yok')


girdi = input("kelime gir \n")
aran = input("aramk istedigin \n")
bul(girdi, aran)
