import random, time, os, json, requests
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
#Sprawdzanie spójności plików oraz pobieranie brakujących
while True:
    launchExist = os.path.isfile('launch-options.json')
    if launchExist == False:
        print('Wykryto brakujący plik "launch-options.json"')
        internet_connection = check_connect()
        if internet_connection == False:
            print("Komputer nie ma połączenia z internetem.")
            quit()
        else:
            url = 'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/launch-options.json'
            response = requests.get(url)
            print('Pobieram brakujący plik')
            open('launch-options.json', 'wb').write(response.content)
    elif launchExist == True:
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
        else:
            import functions, options, download
            print('Weryfikuję pliki...')
            download.check()
            download.check2()
            download.check3()
            functions.printProgressBar(0, l, prefix = 'Przebiega weryfikacja plików:', suffix = 'Ukończono', length = 50)
            for i, item in enumerate(items):
                time.sleep(0.1)
                functions.printProgressBar(i + 1, l, prefix = 'Przebiega weryfikacja plików:', suffix = 'Ukończono', length = 50)
            wykresyExist = os.path.exists('wykresy')
            ammunicjaExist = os.path.exists('ammunicja')
            kamizelkiExist = os.path.exists('kamizelki')
            helmyExist = os.path.exists('helmy')
            ammunitionExist = os.path.isfile('ammunition.json')
            armorsExist = os.path.isfile('armors.json')
            headgearExist = os.path.isfile('headgear.json')
            zadaniaExist = os.path.exists('zadania')
            praporExist = os.path.exists('zadania/prapor')
            therapistExist = os.path.exists('zadania/therapist')
            skierExist = os.path.exists('zadania/skier')
            peacekeeperExist = os.path.exists('zadania/peacekeeper')
            mechanicExist = os.path.exists('zadania/mechanic')
            ragmanExist = os.path.exists('zadania/ragman')
            jaegerExist = os.path.exists('zadania/jaeger')
            fenceExist = os.path.exists('zadania/fence')
            lightkeeperExist = os.path.exists('zadania/lightkeeper')
            obrazyExist = os.path.exists('obrazy')
            pojemnikiExist = os.path.exists('obrazy/pojemniki')
            kamzyExist = os.path.exists('obrazy/kamizelki')
            if wykresyExist == False:
                os.mkdir('wykresy')
            if ammunicjaExist == False:
                os.mkdir('ammunicja')
            if kamizelkiExist == False:
                os.mkdir('kamizelki')
            if helmyExist == False:
                os.mkdir('helmy')
            if ammunitionExist == False:
                print('Wykryto brakujący plik "ammunition.json"')
                try:
                    internet_connection = check_connect()
                    if internet_connection == False:
                        print("Komputer nie ma połączenia z internetem.")
                        quit()
                    url = 'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/ammunition.json'
                    response = requests.get(url)
                    print('Pobieram brakujący plik')
                    open('ammunition.json', 'wb').write(response.content)
                except:
                    print('Operacja nie mogła zostać wykonana. Sprawdź połączenie. Gotowe rozwiązania -')
                    quit()
            if armorsExist == False:
                print('Wykryto brakujący plik "armors.json"')
                try:
                    internet_connection = check_connect()
                    if internet_connection == False:
                        print("Komputer nie ma połączenia z internetem.")
                        quit()
                    url = 'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/armors.json'
                    response = requests.get(url)
                    print('Pobieram brakujący plik')
                    open('armors.json', 'wb').write(response.content)
                except:
                    print('Operacja nie mogła zostać wykonana. Sprawdź połączenie. Gotowe rozwiązania -')
                    quit()
            if headgearExist == False:
                print('Wykryto brakujący plik "headgear.json"')
                try:
                    internet_connection = check_connect()
                    if internet_connection == False:
                        print("Komputer nie ma połączenia z internetem.")
                        quit()
                    url = 'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/headgear.json'
                    response = requests.get(url)
                    print('Pobieram brakujący plik')
                    open('headgear.json', 'wb').write(response.content)
                except:
                    print('Operacja nie mogła zostać wykonana. Sprawdź połączenie. Gotowe rozwiązania -')
                    quit()
            if zadaniaExist == False:
                os.mkdir('zadania')
            if praporExist == False:
                os.mkdir('zadania/prapor')
            if therapistExist == False:
                os.mkdir('zadania/therapist')
            if skierExist == False:
                os.mkdir('zadania/skier')
            if peacekeeperExist == False:
                os.mkdir('zadania/peacekeeper')
            if mechanicExist == False:
                os.mkdir('zadania/mechanic')
            if ragmanExist == False:
                os.mkdir('zadania/ragman')
            if jaegerExist == False:
                os.mkdir('zadania/jaeger')
            if fenceExist == False:
                os.mkdir('zadania/fence')
            if lightkeeperExist == False:
                os.mkdir('zadania/lightkeeper')
            if obrazyExist == False:
                os.mkdir('obrazy')
            if pojemnikiExist == False:
                os.mkdir('obrazy/pojemniki')
            if kamzyExist == False:
                os.mkdir('obrazy/kamizelki')
            break

functions.printProgressBar(0, l, prefix = 'Wczytywanie potrzebnych składników:', suffix = 'Ukończono', length = 50)
for i, item in enumerate(items):
    time.sleep(0.05)
    functions.printProgressBar(i + 1, l, prefix = 'Wczytywanie potrzebnych składników:', suffix = 'Ukończono', length = 50)

print("Witaj w Armor Inatorze")

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
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_12_70, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                            break
                        elif option_ammo == "20x70mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_20_70, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "23x75mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_23_75, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "9x18mm Makarov":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_9_18_makarov, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "7.62x25mm Tokarev":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_762x25_tokarev, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "9x19mm Parabellum":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_9x19_parabellum, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == ".357 Magnum":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.magnum_357, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == ".45 ACP":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.acp_45, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                print(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "9x21mm Gyurza":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_9x21_gyurza, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "5.7x28mm FN":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_28x57_fn, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "4.6x30mm HK":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_46x30_hk, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "9x39mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_9x39, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == ".366 TKM":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.tkm_366, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "5.45x39mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_545x39, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "5.56x45mm NATO":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_556x45_nato, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == ".300 Blackout":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.blackout_300, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "7.62x39mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_762x39, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "7.62x51mm NATO":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_762x51_nato, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "7.62x54mmR":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mmr_762x54, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == ".338 Lapua Magnum":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.lapua_magnum_338, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "12.7x55mm STs-130":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_127x55_sts_130, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "40x46mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_40x46, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "Broń stacjonarna":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.stacjonarna, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = 'stationary'
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class)
                                    functions.get_comparison(kamizelka2, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, kamizelka)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        continue
                    continue
                continue
            else:
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
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_12_70, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "20x70mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_20_70, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "23x75mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_23_75, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "9x18mm Makarov":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_9_18_makarov, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "7.62x25mm Tokarev":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_762x25_tokarev, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "9x19mm Parabellum":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_9x19_parabellum, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == ".357 Magnum":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.magnum_357, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == ".45 ACP":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.acp_45, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "9x21mm Gyurza":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_9x21_gyurza, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "5.7x28mm FN":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_28x57_fn, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "4.6x30mm HK":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_46x30_hk, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "9x39mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_9x39, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == ".366 TKM":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.tkm_366, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "5.45x39mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_545x39, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "5.45x45mm NATO":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_556x45_nato, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == ".300 Blackout":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.blackout_300, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "7.62x39mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_762x39, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "7.62x51mm NATO":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_762x51_nato, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "7.62x54mmR":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mmr_762x54, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == ".338 Lapua Magnum":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.lapua_magnum_338, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "12.7x55mm STs-130":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_127x55_sts_130, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "40x46mm":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.mm_40x46, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = functions.fast_replace(option_ammo)
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
                                    break
                        elif option_ammo == "Broń stacjonarna":
                            while True:
                                option_ammo_2, index_ammo_2 = pick(options.stacjonarna, title4, options.indicator)
                                if option_ammo_2 == "Wstecz":
                                    break
                                option_ammo_2 = functions.fast_replace(option_ammo_2)
                                option_ammo = 'stationary'
                                compare = functions.comparison()
                                if compare == "Tak":
                                    name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage = functions.get_ammo_info(option_ammo, option_ammo_2)
                                    x = functions.write()
                                    if x == "Tak":
                                        functions.write_ammo_info(name2, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage)
                                        functions.write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class)
                                    functions.get_comparison(helm2, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_penetration_power, ammo_damage, ammo_frag_chance, option_ammo, option_ammo_2, name2)
                                    chart = functions.chart()
                                    if chart == True:
                                        functions.create_chart(option_ammo, option_ammo_2, armor_type, helm)
                                        continue
                                    else:
                                        continue
                                else:
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
                                        x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                        break
                            elif primary_option == "Karabinki szturmowe":
                                while True:
                                    carabine_option, carabine_index = pick(options.carbines_options, options.carbines_title, options.indicator)
                                    if carabine_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('karabinki-szturmowe', carabine_option)
                                        x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                        break
                            elif primary_option == "Lekkie karabiny maszynowe":
                                while True:
                                    lmg_option, lmg_index = pick(options.lmg_options, options.lmg_title, options.indicator)
                                    if lmg_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('lekkie-karabiny-maszynowe', lmg_option)
                                        x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                        break
                            elif primary_option == "Pistolety maszynowe":
                                while True:
                                    smg_option, smg_index = pick(options.smg_options, options.smg_title, options.indicator)
                                    if smg_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('pistolety-maszynowe', smg_option)
                                        x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                        break
                            elif primary_option == "Strzelby":
                                while True:
                                    pump_option, pump_index = pick(options.shotguns_options, options.shotguns_title, options.indicator)
                                    if pump_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('strzelby', pump_option)
                                        x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                        break
                            elif primary_option == "Karabiny wyborowe":
                                while True:
                                    marksman_option, marksman_index = pick(options.marksman_options, options.marksman_title, options.indicator)
                                    if marksman_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('karabiny-wyborowe', marksman_option)
                                        x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                        break
                            elif primary_option == "Karabiny snajperskie":
                                while True:
                                    sniper_option, sniper_index = pick(options.snipers_options, options.snipers_title, options.indicator)
                                    if sniper_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('karabiny-snajperskie', sniper_option)
                                        x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                        break
                            elif primary_option == "Wyrzutnie granatów":
                                while True:
                                    launchers_option, launchers_index = pick(options.launchers_options, options.launchers_title, options.indicator)
                                    if launchers_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('wyrzutnie-granatów', launchers_option)
                                        x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
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
                                        x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                        break
                        elif secondary_option == "Rewolwery":
                            while True:
                                    revolver_option, revolver_index = pick(options.revolvers_options, options.revolvers_title, options.indicator)
                                    if revolver_option == "Wstecz":
                                        break
                                    else:
                                        functions.get_gun_info('rewolwery', revolver_option)
                                        x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                        break
                    elif gun_option == "Broń specjalna":
                        while True:
                            special_option, special_index = pick(options.secspecial_options, options.secspecial_title, options.indicator)
                            if special_option == "Wstecz":
                                break
                            else:
                                functions.get_gun_info('specjalne', special_option)
                                x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                break
                    elif gun_option == "Broń stacjonarna":
                        while True:
                            stationary_option, stationary_index = pick(options.stationary_options, options.stationary_title, options.indicator)
                            if stationary_option == "Wstecz":
                                break
                            else:
                                functions.get_gun_info('stacjonarne', stationary_option)
                                x = input("Jeśli chcesz wrócić wpisz cokolwiek:")
                                break
"""    elif doing == "Zadania":
        while True:
            trader, trader_index = pick(options.quests_options, options.quests_title, options.indicator)
            with open(f'{trader}.json') as f:
                """