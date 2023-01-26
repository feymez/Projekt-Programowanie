import random, time, os, json, requests, keyboard
from pick import pick
import urllib.request

def restart():
    while True:
        os.system('python main.py')
        quit()

def check_connect():
    try:
        urllib.request.urlopen('http://google.com/')
        return True
    except:
        return False

items = list(range(0, 57))
l = len(items)
#>----------- Sprawdzanie spójności plików oraz pobieranie brakujących -----------<
while True:
        #>----------- Sprawdzanie plików Python -----------<
    functionsExist = os.path.isfile('functions.py')
    optionsExist = os.path.isfile('functions.py')
    downloadExist = os.path.isfile('download.py')
    directoriesExist = os.path.isfile("directories.py")
    if optionsExist == False:
        print('Wykryto brakujący plik "options.py"')
        internet_connection = check_connect()
        if internet_connection == False:
            print("Komputer nie ma połączenia z internetem.")
            quit()
        else:
            url = 'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/options.py'
            response = requests.get(url)
            print('Pobieram brakujący plik')
            open('options.py', 'wb').write(response.content)
    if functionsExist == False:
        print('Wykryto brakujący plik "functions.py"')
        internet_connection = check_connect()
        if internet_connection == False:
            print("Komputer nie ma połączenia z internetem.")
            quit()
        else:
            url = 'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/functions.py'
            response = requests.get(url)
            print('Pobieram brakujący plik')
            open('functions.py', 'wb').write(response.content)
    if downloadExist == False:
        print("Wykryto brakujący plik 'download.py'")
        internet_connection = check_connect()
        if internet_connection == False:
            print("Komputer nie ma połączenia z internetem.")
            quit()
        else:
            url = 'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/download.py'
            response = requests.get(url)
            print("Pobieram brakując plik")
            open('download.py', 'wb').write(response.content)
    if directoriesExist == False:
        print("Wykryto brakujący plik 'directories.py'")
        internet_connection = check_connect()
        if internet_connection == False:
            print("Komputer nie ma połączenia z internetem.")
            quit()
        else:
            url = 'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/directories.py'
            response = requests.get(url)
            open("directories.py", 'wb').write(response.content)
    import functions, options, download, directories
    print('Weryfikuję pliki...')
    directories.check_all_dir(directories.first1)
    directories.check_all_dir(directories.second2)
    download.check()
    download.check2()
    download.check3()
    download.check4()
    functions.printProgressBar(0, l, prefix = 'Przebiega weryfikacja plików:', suffix = 'Ukończono', length = 50)
    for i, item in enumerate(items):
        time.sleep(0.1)
        functions.printProgressBar(i + 1, l, prefix = 'Przebiega weryfikacja plików:', suffix = 'Ukończono', length = 50)
    break

functions.printProgressBar(0, l, prefix = 'Wczytywanie potrzebnych składników:', suffix = 'Ukończono', length = 50)
for i, item in enumerate(items):
    time.sleep(0.05)
    functions.printProgressBar(i + 1, l, prefix = 'Wczytywanie potrzebnych składników:', suffix = 'Ukończono', length = 50)

while True:
    doing, index_doing = pick(options.doing_options, options.doing_title, options.indicator)
    if doing == "Porównanie":
        while True:
            #Wybieranie: Kamizelka / Hełm
            option, index = pick(options.option1, options.title1, options.indicator)
            if option == "Wstecz":
                break
            elif option == "Kamizelka":
                armor_type = "Kamizelka"
                while True:
                    #Wybieranie kamizelki
                    kamizelka, index_kamizelka = pick(options.option2, options.title2, options.indicator)
                    if kamizelka == "Wstecz":
                        break
                    kamizelka2 = kamizelka
                    kamizelka = functions.fast_replace(kamizelka)
                    vest_name, vest_durability, vest_effective_durability, vest_material, vest_class = functions.get_vest_info(kamizelka, kamizelka2)
                    while True:
                        #Wybieranie amunicji
                        option_ammo, index_ammo = pick(options.option3, options.title3, options.indicator)
                        title4 = f"Wybierz z {option_ammo}"
                        if option_ammo == "Wstecz":
                            break
                        elif option_ammo == "12x70mm":
                            option_ammo = "12x70mm"
                            functions.ammo(options.mm_12_70, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "20x70mm":
                            option_ammo = "20x70mm"
                            functions.ammo(options.mm_20_70, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "23x75mm":
                            option_ammo = "23x75mm"
                            functions.ammo(options.mm_23_75, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "9x18mm Makarov":
                            option_ammo = "9x18mm_makarov"
                            functions.ammo(options.mm_9_18_makarov, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "7.62x25mm Tokarev":
                            option_ammo = "7.62x25mm_tokarev"
                            functions.ammo(options.mm_762x25_tokarev, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "9x19mm Parabellum":
                            option_ammo = "9x19mm_parabellum"
                            functions.ammo(options.mm_9x19_parabellum, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == ".357 Magnum":
                            option_ammo = ".357_magnum"
                            functions.ammo(options.magnum_357, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == ".45 ACP":
                            option_ammo = ".45_acp"
                            functions.ammo(options.acp_45, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "9x21mm Gyurza":
                            option_ammo = "9x21mm_gyurza"
                            functions.ammo(options.mm_9x21_gyurza, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "5.7x28mm FN":
                            option_ammo = "5.7x28mm_fn"
                            functions.ammo(options.mm_28x57_fn, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "4.6x30mm HK":
                            option_ammo = "4.6x30mm_hk"
                            functions.ammo(options.mm_46x30_hk, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "9x39mm":
                            option_ammo = "9x39mm"
                            functions.ammo(options.mm_9x39, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == ".366 TKM":
                            option_ammo = ".366_tkm"
                            functions.ammo(options.tkm_366, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "5.45x39mm":
                            option_ammo = "5.45x39mm"
                            functions.ammo(options.mm_545x39, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "5.56x45mm NATO":
                            option_ammo = "5.56x45mm_nato"
                            functions.ammo(options.mm_556x45_nato, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == ".300 Blackout":
                            option_ammo = ".300_blackout"
                            functions.ammo(options.blackout_300, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "7.62x39mm":
                            option_ammo = "7.62x39mm"
                            functions.ammo(options.mm_762x39, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "7.62x51mm NATO":
                            option_ammo = "7.62x51mm_nato"
                            functions.ammo(options.mm_762x51_nato, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "7.62x54mmR":
                            option_ammo = "7.62x54mmr"
                            functions.ammo(options.mm_12_70, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == ".338 Lapua Magnum":
                            option_ammo = ".338_lapua_magnum"
                            functions.ammo(options.lapua_magnum_338, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "12.7x55mm STs-130":
                            option_ammo = "12.7x55mm_sts-130"
                            functions.ammo(options.mm_127x55_sts_130, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "40x46mm":
                            option_ammo = "40x46mm"
                            functions.ammo(options.mm_40x46, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        elif option_ammo == "Broń stacjonarna":
                            option_ammo = "stationary"
                            functions.ammo(options.stacjonarna, title4, vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, kamizelka2, option_ammo, armor_type, kamizelka)
                            break
                        continue
                    continue
                continue
            elif option == "Hełm":
                armor_type = "Hełm"
                while True:
                    #Wybieranie hełmu
                    helm, index_helm = pick(options.option5, options.title5, options.indicator)
                    if helm == "Wstecz":
                        break
                    helm2 = helm
                    helm = functions.fast_replace(helm)
                    helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class = functions.get_helmet_info(helm, helm2)
                    while True:
                        #Wybieranie amunicji
                        option_ammo, index_ammo = pick(options.option3, options.title3, options.indicator)
                        title4 = f"Wybierz z {option_ammo}"
                        if option_ammo == "Wstecz":
                            break
                        elif option_ammo == "12x70mm":
                            option_ammo = "12x70mm"
                            functions.ammo(options.mm_12_70, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "20x70mm":
                            option_ammo = "20x70mm"
                            functions.ammo(options.mm_20_70, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "23x75mm":
                            option_ammo = "23x75mm"
                            functions.ammo(options.mm_23_75, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "9x18mm Makarov":
                            option_ammo = "9x18mm_makarov"
                            functions.ammo(options.mm_9_18_makarov, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "7.62x25mm Tokarev":
                            option_ammo = "7.62x25mm_tokarev"
                            functions.ammo(options.mm_762x25_tokarev, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "9x19mm Parabellum":
                            option_ammo = "9x19mm_parabellum"
                            functions.ammo(options.mm_9x19_parabellum, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == ".357 Magnum":
                            option_ammo = ".357_magnum"
                            functions.ammo(options.magnum_357, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == ".45 ACP":
                            option_ammo = ".45_acp"
                            functions.ammo(options.acp_45, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "9x21mm Gyurza":
                            option_ammo = "9x21mm_gyurza"
                            functions.ammo(options.mm_9x21_gyurza, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "5.7x28mm FN":
                            option_ammo = "5.7x28mm_fn"
                            functions.ammo(options.mm_28x57_fn, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "4.6x30mm HK":
                            option_ammo = "4.6x30mm_hk"
                            functions.ammo(options.mm_46x30_hk, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "9x39mm":
                            option_ammo = "9x39mm"
                            functions.ammo(options.mm_9x39, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == ".366 TKM":
                            option_ammo = ".366_tkm"
                            functions.ammo(options.tkm_366, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "5.45x39mm":
                            option_ammo = "5.45x39mm"
                            functions.ammo(options.mm_545x39, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "5.45x45mm NATO":
                            option_ammo = "5.56x45mm_nato"
                            functions.ammo(options.mm_556x45_nato, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == ".300 Blackout":
                            option_ammo = ".300_blackout"
                            functions.ammo(options.blackout_300, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "7.62x39mm":
                            option_ammo = "7.62x39mm"
                            functions.ammo(options.mm_762x39, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "7.62x51mm NATO":
                            option_ammo = "7.62x51mm_nato"
                            functions.ammo(options.mm_762x51_nato, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "7.62x54mmR":
                            option_ammo = "7.62x54mmr"
                            functions.ammo(options.mm_12_70, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == ".338 Lapua Magnum":
                            option_ammo = ".338_lapua_magnum"
                            functions.ammo(options.lapua_magnum_338, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "12.7x55mm STs-130":
                            option_ammo = "12.7x55mm_sts-130"
                            functions.ammo(options.mm_127x55_sts_130, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "40x46mm":
                            option_ammo = "40x46mm"
                            functions.ammo(options.mm_40x46, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        elif option_ammo == "Broń stacjonarna":
                            option_ammo = "stationary"
                            functions.ammo(options.stacjonarna, title4, helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, helm2, option_ammo, armor_type, helm)
                            break
                        continue
                    continue
                continue
    elif doing == 'Sprawdzenie statystyk':
        while True:
            option_stats, index_stats = pick(options.stats_options, options.stats_title, options.indicator)
            if option_stats == "Wstecz":
                break
            elif option_stats == "Kamizelki":
                armor_type = "Kamizelka"
                while True:
                    #Wybieranie kamizelki
                    kamizelka, index_kamizelka = pick(options.option2, options.title2, options.indicator)
                    if kamizelka == "Wstecz":
                        break
                    kamizelka2 = kamizelka
                    kamizelka = functions.fast_replace(kamizelka)
                    functions.get_vest_info(kamizelka, kamizelka2)
                    exit = input("Jeśli chcesz wrócić do menu wybory wpisz cokolwiek:")
                    break
            elif option_stats == "Hełmy":
                armor_type = "Hełm"
                while True:
                    #Wybieranie hełmu
                    helm, index_helm = pick(options.option5, options.title5, options.indicator)
                    if helm == "Wstecz":
                        break
                    helm2 = helm
                    helm = functions.fast_replace(helm)
                    functions.get_helmet_info(helm, helm2)
                    exit = input("Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:")
                    break
            elif option_stats == "Ammunicja":
                option_ammo, index_ammo = pick(options.option3, options.title3, options.indicator)
                title4 = f"Wybierz z {option_ammo}"
                if option_ammo == "Wstecz":
                    break
                elif option_ammo == "12x70mm":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_12_70, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "20x70mm":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_20_70, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "23x75mm":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_23_75, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "9x18mm Makarov":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_9_18_makarov, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "7.62x25mm Tokarev":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_762x25_tokarev, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "9x19mm Parabellum":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_9x19_parabellum, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == ".357 Magnum":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.magnum_357, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == ".45 ACP":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.acp_45, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "9x21mm Gyurza":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_9x21_gyurza, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "5.7x28mm FN":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_28x57_fn, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "4.6x30mm HK":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_46x30_hk, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "9x39mm":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_9x39, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == ".366 TKM":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.tkm_366, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "5.45x39mm":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_545x39, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "5.45x45mm NATO":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_556x45_nato, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == ".300 Blackout":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.blackout_300, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "7.62x39mm":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_762x39, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "7.62x51mm NATO":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_762x51_nato, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "7.62x54mmR":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mmr_762x54, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == ".338 Lapua Magnum":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.lapua_magnum_338, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "12.7x55mm STs-130":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_127x55_sts_130, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "40x46mm":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.mm_40x46, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = functions.fast_replace(option_ammo)
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
                elif option_ammo == "Broń stacjonarna":
                    while True:
                        option_ammo_2, index_ammo_2 = pick(options.stacjonarna, title4, options.indicator)
                        if option_ammo_2 == "Wstecz":
                            break
                        option_ammo_2 = functions.fast_replace(option_ammo_2)
                        option_ammo = 'stationary'
                        functions.get_ammo_info(option_ammo, option_ammo_2)
                        exit = input('Jeśli chcesz wrócić do menu wyboru wpisz cokolwiek:')
                        break
    elif doing == "Kompatybilność":
        while True:
            compatibility_option, comatibility_index = pick(options.compatibility_options, options.compatibility_title, options.indicator)
            if compatibility_option == "Wstecz":
                break
            else:
                while True:
                    gun_option, gun_index = pick(options.guns_cat_options, options.guns_cat_title, options.indicator)
                    if gun_option == "Wstecz":
                        break
                    elif gun_option == "Broń podstawowa":
                        while True:
                            primary_option, primary_index = pick(options.primary_options, options.primary_title, options.indicator)
                            if primary_option == "Wstecz":
                                break
                            elif primary_option == "Karabiny szturmowe":
                                while True:
                                    assault_option, assault_index = pick(options.assault_options, options.assault_title, options.indicator)
                                    if assault_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('karabiny-szturmowe', assault_option)
                                        functions.get_back()
                                        break
                            elif primary_option == "Karabinki szturmowe":
                                while True:
                                    carabine_option, carabine_index = pick(options.carbines_options, options.carbines_title, options.indicator)
                                    if carabine_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('karabinki-szturmowe', carabine_option)
                                        functions.get_back()
                                        break
                            elif primary_option == "Lekkie karabiny maszynowe":
                                while True:
                                    lmg_option, lmg_index = pick(options.lmg_options, options.lmg_title, options.indicator)
                                    if lmg_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('lekkie-karabiny-maszynowe', lmg_option)
                                        functions.get_back()
                                        break
                            elif primary_option == "Pistolety maszynowe":
                                while True:
                                    smg_option, smg_index = pick(options.smg_options, options.smg_title, options.indicator)
                                    if smg_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('pistolety-maszynowe', smg_option)
                                        functions.get_back()
                                        break
                            elif primary_option == "Strzelby":
                                while True:
                                    pump_option, pump_index = pick(options.shotguns_options, options.shotguns_title, options.indicator)
                                    if pump_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('strzelby', pump_option)
                                        functions.get_back()
                                        break
                            elif primary_option == "Karabiny wyborowe":
                                while True:
                                    marksman_option, marksman_index = pick(options.marksman_options, options.marksman_title, options.indicator)
                                    if marksman_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('karabiny-wyborowe', marksman_option)
                                        functions.get_back()
                                        break
                            elif primary_option == "Karabiny snajperskie":
                                while True:
                                    sniper_option, sniper_index = pick(options.snipers_options, options.snipers_title, options.indicator)
                                    if sniper_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('karabiny-snajperskie', sniper_option)
                                        functions.get_back()
                                        break
                            elif primary_option == "Wyrzutnie granatów":
                                while True:
                                    launchers_option, launchers_index = pick(options.launchers_options, options.launchers_title, options.indicator)
                                    if launchers_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('wyrzutnie-granatów', launchers_option)
                                        functions.get_back()
                                        break
                    elif gun_option == "Broń drugorzędna":
                        secondary_option, secondary_index = pick(options.secondary_options, options.secondary_title, options.indicator)
                        if secondary_option == "Wstecz":
                            break
                        elif secondary_option == "Pistolety":
                            while True:
                                    pistol_option, pistol_index = pick(options.pistols_options, options.pistols_title, options.indicator)
                                    if pistol_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('pistolety', pistol_option)
                                        functions.get_back()
                                        break
                        elif secondary_option == "Rewolwery":
                            while True:
                                    revolver_option, revolver_index = pick(options.revolvers_options, options.revolvers_title, options.indicator)
                                    if revolver_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('rewolwery', revolver_option)
                                        functions.get_back()
                                        break
                    elif gun_option == "Broń specjalna":
                        while True:
                            special_option, special_index = pick(options.secspecial_options, options.secspecial_title, options.indicator)
                            if special_option == "Wstecz":
                                break
                            else:
                                functions.get_gun_info('specjalne', special_option)
                                functions.get_back()
                                break
                    elif gun_option == "Broń stacjonarna":
                        while True:
                            stationary_option, stationary_index = pick(options.stationary_options, options.stationary_title, options.indicator)
                            if stationary_option == "Wstecz":
                                break
                            else:
                                functions.get_gun_info('stacjonarne', stationary_option)
                                functions.get_back()
                                break
    elif doing == "Wyposażenie":
        while True:
            equipment_option, equipment_index = pick(options.equipment_options, options.equipment_title, options.indicator)
            if equipment_option == "Wstecz":
                break
            else:
                while True:
                    if equipment_option == "Plecaki":
                        backpacks_option, backpacks_title = pick(options.backpack_options, options.backpack_title, options.indicator)
                        if backpacks_option == "Wstecz":
                            break
                        backpacks_option = functions.fast_replace(backpacks_option)
                        functions.get_backpack_info(backpacks_option)
                        functions.get_back()
                        break
                    elif equipment_option == "Kamizelki Taktyczne":
                        chestrig_option, chestrig_index = pick(options.chestrig_options, options.chestrig_title, options.indicator)
                        if chestrig_option == "Wstecz":
                            break
                        chestrig_option = functions.fast_replace(chestrig_option)
                        functions.get_chestrig_info(chestrig_option)
                        functions.get_back()
    elif doing == "Pojemniki":
        while True:
            container_option, container_index = pick(options.containers_options, options.containers_title, options.indicator)
            if container_option == "Wstecz":
                break
            else:
                container_option = functions.fast_replace(container_option)
                functions.get_container_info(container_option)
                functions.get_back()
    elif doing == "Medykamenty":
        while True:
            medicament_option, medicament_index = pick(options.medicaments_options, options.medicaments_title, options.indicator)
            if medicament_option == "Wstecz":
                break
            else:
                medicament_option = functions.fast_replace(medicament_option)
                functions.get_medicament_info(medicament_option)
                functions.get_back()