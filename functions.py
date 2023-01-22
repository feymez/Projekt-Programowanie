import json, options, time, os, keyboard
from pick import pick
import matplotlib.pyplot as plt
import matplotlib as mpl
from os.path import exists
from PIL import Image

space = ">---------------------------------------------------------<"

def get_vest_info(name, name2):
    with open('armors.json', encoding='UTF-8') as f:
        armors = json.load(f)
        armor = armors[name]
        if name in armors:
            armor_name = armor["name"]
            armor_material = armor["material"]
            armor_class = armor["class"]
            armor_areas = armor["areas"]
            armor_durability = armor["durability"]
            armor_effective_durability = armor["effective_durability"]
            armor_movement_speed = armor["movement_speed"]
            armor_turning_speed = armor["turning_speed"]
            armor_ergonomics = armor["ergonomics"]
            armor_weight = armor["weight"]
            armor_image = armor['image']
            print(space)
            print(f"Oto wszystkie informacje na temat kamizelki {name2}")
            print(space)
            print(f"Pełna nazwa: {armor_name}")
            print(f"Materiał: {armor_material}")
            print(f"Klasa pancerza: {armor_class}")
            print(f"Chronione strefy: {armor_areas}")
            print(f"Trwałość: {armor_durability}")
            print(f"Efektywna trwałość: {armor_effective_durability}")
            print(f"Prędkość ruchu: {armor_movement_speed}")
            print(f"Prędkość obrotu: {armor_turning_speed}")
            print(f"Ergonomia: {armor_ergonomics}")
            print(f"Waga: {armor_weight}kg")
            image = Image.open(f"obrazy/kamizelki/{armor_image}")
            image.show()
            return armor_name, armor_durability, armor_effective_durability, armor_material, armor_class

def get_helmet_info(name, name2):
    with open('headgear.json', encoding='UTF-8') as f:
        helmets = json.load(f)
        helmet = helmets[name]
        if name in helmets:
            helmet_name = helmet["name"]
            helmet_material = helmet["material"]
            helmet_class = helmet["class"]
            helmet_areas = helmet["areas"]
            helmet_durability = helmet["durability"]
            helmet_effective_durability = helmet["effective_durability"]
            helmet_movement_speed = helmet["movement_speed"]
            helmet_turning_speed = helmet["turning_speed"]
            helmet_ergonomics = helmet["ergonomics"]
            helmet_weight = helmet["weight"]
            helmet_image = helmet["image"]
            print(space)
            print(f"Oto wszystkie informacje na temat hełmu {name2}")
            print(space)
            print(f"Pełna nazwa: {helmet_name}")
            print(f"Materiał: {helmet_material}")
            print(f"Klasa pancerza: {helmet_class}")
            print(f"Chronione strefy: {helmet_areas}")
            print(f"Trwałość: {helmet_durability}")
            print(f"Efektywna trwałość: {helmet_effective_durability}")
            print(f"Prędkość ruchu: {helmet_movement_speed}")
            print(f"Prędkość obrotu: {helmet_turning_speed}")
            print(f"Ergonomia: {helmet_ergonomics}")
            print(f"Waga: {helmet_weight}kg")
            image = Image.open(f"obrazy/helmy/{helmet_image}")
            image.show()
            return helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class

def get_ammo(caliber):
    with open('ammunition.json', encoding='UTF-8') as f:
        ammos = json.load(f)
        ammo = ammos[caliber]
        choices = ammo.keys()
        return choices

def get_ammo_info(caliber, name):
    with open("ammunition.json", encoding='UTF-8') as f:
        ammos = json.load(f)
        ammos = ammos[caliber]
        ammos = ammos[name]
        ammo_name = ammos["name"]
        ammo_damage = ammos["damage"]
        ammo_penetration_power = ammos["penetration_power"]
        ammo_armor_damage = ammos["armor_damage"]
        ammo_accuracy = ammos["accuracy"]
        ammo_recoil = ammos["recoil"]
        ammo_frag_chance = ammos["frag_chance"]
        ammo_light_bleeding = ammos["light_bleeding"]
        ammo_heavy_bleeding = ammos["heavy_bleeding"]
        ammo_bullet_effectiveness_against_armor_class = ammos["bullet_effectiveness_against_armor_class"]
        ammo_bullet_effectiveness_against_armor_class = str(ammo_bullet_effectiveness_against_armor_class)
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace("'", "")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace(":", "")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace("{", "")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace("}", "")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace(",", "")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace("class", "Klasa")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace("Klasa1", "Klasa 1:")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace("Klasa2", "Klasa 2:")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace("Klasa3", "Klasa 3:")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace("Klasa4", "Klasa 4:")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace("Klasa5", "Klasa 5:")
        ammo_bullet_effectiveness_against_armor_class = ammo_bullet_effectiveness_against_armor_class.replace("Klasa6", "Klasa 6:")
        ammo_tracer = ammos["isTracer"]
        ammo_subsonic = ammos["isSubsonic"]
        ammo_listedOnFleaMarket = ammos["listedOnFleaMarket"]
        ammo_image = ammos["image"]
        if ammo_tracer == True:
            ammo_tracer = "Tak"
        else:
            ammo_tracer = "Nie"
        if ammo_subsonic == True:
            ammo_subsonic = "Tak"
        else:
            ammo_subsonic = "Nie"
        if ammo_listedOnFleaMarket == True:
            ammo_listedOnFleaMarket = "Tak"
        else:
            ammo_listedOnFleaMarket = "Nie"
        if ammo_damage == None:
            ammo_damage = "Żadne"
        if ammo_penetration_power == None:
            ammo_penetration_power = "Żadna"
        if ammo_armor_damage == None:
            ammo_armor_damage = "Żadne"
        if ammo_accuracy == None:
            ammo_accuracy = "Żadna"
        if ammo_recoil == None:
            ammo_recoil = "Żaden"
        if ammo_frag_chance == None:
            ammo_frag_chance = "Żadna"
        if ammo_light_bleeding == None:
            ammo_light_bleeding = "Żadna"
        if ammo_heavy_bleeding == None:
            ammo_heavy_bleeding = "Żadna"
        print(space)
        print(f"Oto wszystkie informacje na temat pocisku {ammo_name}")
        print(space)
        print(f"Pełna nazwa: {ammo_name}")
        print(f"Obrażenia: {ammo_damage}")
        print(f"Siła penetracji: {ammo_penetration_power}")
        print(f"Obrażenia pancerza: {ammo_armor_damage}")
        print(f"Celność: {ammo_accuracy}")
        print(f"Odrzut: {ammo_recoil}")
        print(f"Szansa zabójstwa: {ammo_frag_chance}")
        print(f"Szansa słabego krwawienia: {ammo_light_bleeding}")
        print(f"Szansa silnego krwawienia: {ammo_heavy_bleeding}")
        print(f"Efektywność przeciwko klasom pancerza: {ammo_bullet_effectiveness_against_armor_class}")
        print(f"Typu tracer: {ammo_tracer}")
        print(f"Poddźwiękowa: {ammo_subsonic}")
        print(f"Listowana na Flea Market: {ammo_listedOnFleaMarket}")
        image = Image.open(f"obrazy/ammunicja/{ammo_image}.png")
        image.show()
        return ammo_name, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage

def fast_replace(name):
    name = name.lower()
    name = name.replace(" ","_")
    name = name.replace("(", "")
    name = name.replace(")", "")
    return name

def fast_replace_2(str):
    str = str.replace("%", "")
    str = str.replace("x", "")
    return str

def fast_replace_3(str):
    str = str.replace("_", " ")
    return str

def get_back():
    print("Wciśnij BACKSPACE aby wrócić")
    while True:
        try:
            if keyboard.is_pressed('backspace'):
                break
        except:
            continue

def comparison():
    comparison_choice, comparison_index = pick(options.comparison_options, options.comparison_title, indicator="->")
    comparison_choice = comparison_choice
    return comparison_choice

def get_comparison(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class, ammo_power, ammo_damage, ammo_chance, caliber, name, name2):
    with open('ammunition.json', encoding='UTF-8') as f:
        ammo = json.load(f)
        ammos = ammo[caliber]
        ammos = ammos[name]
        ammo_class = ammos["bullet_effectiveness_against_armor_class"]
        if vest_class == 1:
            ammo_class = ammo_class["class1"]
        elif vest_class == 2:
            ammo_class = ammo_class["class2"]
        elif vest_class == 3:
            ammo_class = ammo_class["class3"]
        elif vest_class == 4:
            ammo_class = ammo_class["class4"]
        elif vest_class == 5:
            ammo_class = ammo_class["class5"]
        elif vest_class == 6:
            ammo_class = ammo_class["class4"]
        print(space)
        print(f"Porównanie {name2} oraz {vest_name}")
        print(space)
        print(f"Efektywność tej kuli przeciwko temu pancerzowi to: {ammo_class}/6")
        print(space)
        if "x" in ammo_damage:
            vest_durability = float(vest_durability)
            vest_effective_durability = float(vest_effective_durability)
            ammo_damage = fast_replace_2(ammo_damage)
            ammo_chance = fast_replace_2(ammo_chance)
            ammo_damage = float(ammo_damage)
            ammo_chance = float(ammo_chance)
            if ammo_damage != 0:
                x = vest_durability / ammo_damage
                if ammo_chance != 0:
                    y = vest_effective_durability / ammo_chance
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
                else:
                    y = vest_effective_durability
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
            else:
                x = vest_durability
                if ammo_chance != 0:
                    y = vest_effective_durability / ammo_chance
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
                else:
                    y = vest_effective_durability
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
            z = round(z)
            print(f'Do zniszczenia kamizelki potrzeba {z} strzałów')
            return z
        else:
            vest_durability = float(vest_durability)
            vest_effective_durability = float(vest_effective_durability)
            ammo_chance = fast_replace_2(ammo_chance)
            ammo_damage = fast_replace_2(ammo_damage)
            ammo_damage = float(ammo_damage)
            ammo_chance = float(ammo_chance)
            if ammo_damage != 0:
                x = vest_durability / ammo_damage
                if ammo_chance != 0:
                    y = vest_effective_durability / ammo_chance
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
                else:
                    y = vest_effective_durability
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
            else:
                x = vest_durability
                if ammo_chance != 0:
                    y = vest_effective_durability / ammo_chance
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
                else:
                    y = vest_effective_durability
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
            z = round(z)
            print(f'Do zniszczenia kamizelki potrzeba {z} strzałów')
            return z

def get_comparison_helmet(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class, ammo_power, ammo_damage, ammo_chance, caliber, name, name2):
    with open('ammunition.json', encoding='UTF-8') as f:
        ammo = json.load(f)
        ammos = ammo[caliber]
        ammos = ammos[name]
        ammo_class = ammos["bullet_effectiveness_against_armor_class"]
        if helmet_class == 1:
            ammo_class = ammo_class["class1"]
        elif helmet_class == 2:
            ammo_class = ammo_class["class2"]
        elif helmet_class == 3:
            ammo_class = ammo_class["class3"]
        elif helmet_class == 4:
            ammo_class = ammo_class["class4"]
        elif helmet_class == 5:
            ammo_class = ammo_class["class5"]
        elif helmet_class == 6:
            ammo_class = ammo_class["class4"]
        print(space)
        print(f"Porównanie {name2} oraz {helmet_name}")
        print(space)
        print(f"Efektywność tej kuli przeciwko temu pancerzowi to: {ammo_class}/6")
        print(space)
        if "x" in ammo_damage:
            helmet_durability = float(helmet_durability)
            helmet_effective_durability = float(helmet_effective_durability)
            ammo_damage = fast_replace_2(ammo_damage)
            ammo_chance = fast_replace_2(ammo_chance)
            ammo_damage = float(ammo_damage)
            ammo_chance = float(ammo_chance)
            if ammo_damage != 0:
                x = helmet_durability / ammo_damage
                if ammo_chance != 0:
                    y = helmet_effective_durability / ammo_chance
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
                else:
                    y = helmet_effective_durability
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
            else:
                x = helmet_durability
                if ammo_chance != 0:
                    y = helmet_effective_durability / ammo_chance
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
                else:
                    y = helmet_effective_durability
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
            z = round(z)
            print(f'Do zniszczenia hełmu potrzeba {z} strzałów')
            time.sleep(10)
            return z
        else:
            helmet_durability = float(helmet_durability)
            helmet_effective_durability = float(helmet_effective_durability)
            ammo_chance = fast_replace_2(ammo_chance)
            ammo_damage = fast_replace_2(ammo_damage)
            ammo_damage = float(ammo_damage)
            ammo_chance = float(ammo_chance)
            if ammo_damage != 0:
                x = helmet_durability / ammo_damage
                if ammo_chance != 0:
                    y = helmet_effective_durability / ammo_chance
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
                else:
                    y = helmet_effective_durability
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
            else:
                x = helmet_durability
                if ammo_chance != 0:
                    y = helmet_effective_durability / ammo_chance
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
                else:
                    y = helmet_effective_durability
                    z = x * y
                    z = z * ammo_power
                    z = z / 25
            z = round(z)
            print(f'Do zniszczenia hełmu potrzeba {z} strzałów')
            time.sleep(10)
            return z
            
def chart():
    option, index = pick(options.chart_options, options.chart_title, options.indicator)
    if option == "Tak":
        return True
    else:
        return False

def create_chart(caliber, name, armor_type, vest_name):
    if armor_type == "Kamizelka":
        with open('armors.json', encoding='UTF-8') as f:
            armors = json.load(f)
            armors = armors[vest_name]
            armor_class = armors['class']
            if armor_class == 1:
                armor_classes = [-2, armor_class, -2, -2, -2, -2, -2]
            elif armor_class == 2:
                armor_classes = [-2, -2, armor_class, -2, -2, -2, -2]
            elif armor_class == 3:
                armor_classes = [-2, -2, -2, armor_class, -2, -2, -2]
            elif armor_class == 4:
                armor_classes = [-2, -2, -2, -2, armor_class, -2, -2]
            elif armor_class == 5:
                armor_classes = [-2, -2, -2, -2, -2, armor_class, -2]
            elif armor_class == 6:
                armor_classes = [-2, -2, -2, -2, -2, -2, armor_class]
        with open('ammunition.json', encoding='UTF-8') as f:
            ammos = json.load(f)
            ammos = ammos[caliber]
            ammos = ammos[name]
            ammos = ammos['bullet_effectiveness_against_armor_class']
            if armor_class == 1:
                ammos_class = ammos['class1']
                ammos_class = [-2, ammos_class, -2, -2, -2, -2, -2]
            elif armor_class == 2:
                ammos_class = ammos['class2']
                ammos_class = [-2, -2, ammos_class, -2, -2, -2, -2]
            elif armor_class == 3:
                ammos_class = ammos['class3']
                ammos_class = [-2, -2, -2, ammos_class, -2, -2, -2]
            elif armor_class == 4:
                ammos_class = ammos['class4']
                ammos_class = [-2, -2, -2, -2, ammos_class, -2, -2]
            elif armor_class == 5:
                ammos_class = ammos['class5']
                ammos_class = [-2, -2, -2, -2, -2, ammos_class, -2]
            else:
                ammos_class = ammos['class6']
                ammos_class = [-2, -2, -2, -2, -2, -2, ammos_class]
            
            name = fast_replace_3(name)
            name = name.capitalize()
            vest_name = fast_replace_3(vest_name)
            vest_name = vest_name.capitalize()
            mpl.rcParams['figure.dpi'] = 100
            plt.figure(facecolor="#252525")
            plt.plot(armor_classes, ammos_class, 'o', color='red', label = 'Punkt przebicia pancerza')
            plt.legend(loc=(0.01, 0.01), frameon = True)
            plt.title(f"Przebicie kuli {name} względem {vest_name}")
            plt.xlim(-1, 7)
            plt.ylim(-1, 7)
            plt.xlabel(xlabel = "Klasyfikacja pancerza", fontsize = 15, color = 'red')
            plt.ylabel(ylabel = "Klasyfikacja pocisku", fontsize = 15, color='red')
            plt.savefig(f'wykresy\{name}-{vest_name}.jpg', dpi=400)
            plt.savefig(f'wykresy\{name}-{vest_name}.pdf', dpi=400)
            plt.show()
    else:
        with open('headgear.json', encoding='UTF-8') as f:
            helmets = json.load(f)
            helmets = helmets[vest_name]
            helmet_class = helmets['class']
            if helmet_class == 1:
                helmet_classes = [-2, helmet_class, -2, -2, -2, -2, -2]
            elif helmet_class == 2:
                helmet_classes = [-2, -2, helmet_class, -2, -2, -2, -2]
            elif helmet_class == 3:
                helmet_classes = [-2, -2, -2, helmet_class, -2, -2, -2]
            elif helmet_class == 4:
                helmet_classes = [-2, -2, -2, -2, helmet_class, -2, -2]
            elif helmet_class == 5:
                helmet_classes = [-2, -2, -2, -2, -2, helmet_class, -2]
            elif helmet_class == 6:
                helmet_classes = [-2, -2, -2, -2, -2, -2, helmet_class]
        with open('ammunition.json', encoding='UTF-8') as f:
            ammos = json.load(f)
            ammos = ammos[caliber]
            ammos = ammos[name]
            ammos = ammos['bullet_effectiveness_against_armor_class']
            if helmet_class == 1:
                ammos_class = ammos['class1']
                ammos_class = [-2, ammos_class, -2, -2, -2, -2, -2]
            elif helmet_class == 2:
                ammos_class = ammos['class2']
                ammos_class = [-2, -2, ammos_class, -2, -2, -2, -2]
            elif helmet_class == 3:
                ammos_class = ammos['class3']
                ammos_class = [-2, -2, -2, ammos_class, -2, -2, -2]
            elif helmet_class == 4:
                ammos_class = ammos['class4']
                ammos_class = [-2, -2, -2, -2, ammos_class, -2, -2]
            elif helmet_class == 5:
                ammos_class = ammos['class5']
                ammos_class = [-2, -2, -2, -2, -2, ammos_class, -2]
            else:
                ammos_class = ammos['class6']
                ammos_class = [-2, -2, -2, -2, -2, -2, ammos_class]
            name = fast_replace_3(name)
            name = name.capitalize()
            vest_name = fast_replace_3(vest_name)
            vest_name = vest_name.capitalize()
            mpl.rcParams['figure.dpi'] = 100
            plt.figure(facecolor="#252525")
            plt.plot(helmet_classes, ammos_class, 'o', color='red', label = 'Punkt przebicia hełmu')
            plt.legend(loc=(0.01, 0.01), frameon = True)
            plt.title(f"Przebicie kuli {name} względem {vest_name}", color="white")
            plt.xlim(-1, 7)
            plt.ylim(-1, 7)
            plt.xlabel(xlabel = "Klasyfikacja hełmu", fontsize = 15, color = 'red')
            plt.ylabel(ylabel = "Klasyfikacja pocisku", fontsize = 15, color='red')
            plt.savefig(f'wykresy\{name}-{vest_name}.jpg', dpi=400)
            plt.savefig(f'wykresy\{name}-{vest_name}.pdf', dpi=400)
            plt.show()

def restart():
    while True:
        os.system('python main.py')
        quit()
        
#Funkcja printProgressBar nie została stworzona przeze mnie. Znalazłem ją w internecie oraz dodałem do programu w celach wyglądowych programu.
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

def write():
    choice, index = pick(options.write_options, options.write_title, options.indicator)
    return choice

def write_ammo_info(ammo_name, ammo_penetration_power, ammo_armor_damage, ammo_frag_chance, ammo_damage):
    dict = {
        "name": f"{ammo_name}",
        "penetration_power": f"{ammo_penetration_power}",
        "ammo_armor_damage": f"{ammo_armor_damage}",
        "ammo_frag_chance": f"{ammo_frag_chance}",
        "ammo_damage": f"{ammo_damage}"
    }
    with open(f'ammunicja\{ammo_name}.json', 'w', encoding='UTF-8') as f:
        json.dump(dict, f)

def write_vest_info(vest_name, vest_durability, vest_effective_durability, vest_material, vest_class):
    dict = {
        "name": f"{vest_name}",
        "durability": f"{vest_durability}",
        "effective_durability": f"{vest_effective_durability}",
        "material": f"{vest_material}",
        "class": f"{vest_class}"
    }
    with open(f'kamizelki\{vest_name}.json', 'w', encoding='UTF-8') as f:
        json.dump(dict, f)

def write_helmet_info(helmet_name, helmet_durability, helmet_effective_durability, helmet_material, helmet_class):
    dict = {
        "name": f"{helmet_name}",
        "durability": f"{helmet_durability}",
        "effective_durability": f"{helmet_effective_durability}",
        "material": f"{helmet_material}",
        "class": f"{helmet_class}"
    }
    with open(f'helmy\{helmet_name}.json', 'w', encoding='UTF-8') as f:
        json.dump(dict, f)

def get_gun_info(category, name):
    with open(f'bronie/{category}/{name}.json', encoding='UTF-8') as f:
        gun = json.load(f)
        gun_type = gun['type']
        gun_slot = gun['slot']
        gun_weight = gun['weight']
        gun_grid_size = gun['grid_size']
        gun_recoils = gun['recoil']
        gun_ver_recoil = gun_recoils['vertical']
        gun_hor_recoil = gun_recoils['horizontal']
        gun_distance = gun['effective_distance']
        gun_ergonomics = gun['ergonomics']
        gun_firing_modes = gun['firing_mode']
        gun_rpm = gun['rpm']
        gun_moa = gun['moa']
        gun_caliber = gun['caliber']
        gun_default_ammo = gun['default_ammo']
        gun_muzzle_velocity = gun['muzzle_velocity']
        gun_default_mag = gun['default_mag']
        gun_accepted_ammunition = gun['accepted_ammunition']
        print(space)
        print(f"Wszystkie informacje na temat {name}")
        print(space)
        print(f'Rodzaj: {gun_type}')
        print(f'Miejsce: {gun_slot}')
        print(f'Waga: {gun_weight}')
        print(f'Rozmiar siatki: {gun_grid_size}')
        print(f'Odrzut wertykalny: {gun_ver_recoil}')
        print(f'Odrzut horyzontalny: {gun_hor_recoil}')
        print(f'Efektywny dystans: {gun_distance}')
        print(f'Ergonomia: {gun_ergonomics}')
        print(f'Tryby ognia: {gun_firing_modes}')
        print(f'RPM: {gun_rpm}')
        print(f'MOA: {gun_moa}')
        print(f'Kaliber: {gun_caliber}')
        print(f'Domyślnia ammunicja: {gun_default_ammo}')
        print(f'Prędkość wylotowa kuli: {gun_muzzle_velocity}')
        print(f'Domyślny magazynek: {gun_default_mag}')
        print(f'Obsługiwana ammunicja: {gun_accepted_ammunition}')

def check_file_extension(directory, name):
    filepng = os.path.isfile(f"{directory}/{name}.png")
    filegif = os.path.isfile(f"{directory}/{name}.gif")

    if filepng == True:
        file = "PNG"
        return file
    elif filegif == True:
        file = "GIF"
        return file

def get_backpack_info(name):
    with open("backpacks.json", encoding="UTF-8") as f:
        backpack = json.load(f)
        backpack = backpack[name]
        backpack_name = backpack["name"]
        backpack_slots = backpack["slots"]
        backpack_outer_grid = backpack["outer_grid"]
        backpack_inner_grid = backpack["inner_grid"]
        backpack_efficiency = backpack["efficiency"]
        backpack_holds = backpack["holds"]
        backpack_weight = backpack["weight"]
        backpack_sold = backpack["sold_by"]
        backpack_image = backpack["image"]
        print(f"Pełna nazwa: {backpack_name}")
        print(f"Pojemność: {backpack_slots}")
        print(f"Zajmowane miejsce: {backpack_outer_grid}")
        print(f"Siatka wewnętrzna: {backpack_inner_grid}")
        print(f"Wydajność plecaka: {backpack_efficiency}")
        print(f"Może przechowywać: {backpack_holds}")
        print(f"Waga: {backpack_weight}kg")
        print(f"Możliowść kupienia u: {backpack_sold}")
        image = Image.open(f"obrazy/plecaki/{backpack_image}")
        image.show()

def get_chestrig_info(name):
    with open("")