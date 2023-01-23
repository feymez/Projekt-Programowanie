import os, requests, time
import urllib.request

sciezki_bronie = ["karabinki-szturmowe", "karabiny-snajperskie", "karabiny-szturmowe", "karabiny-wyborowe", "lekkie-karabiny-maszynowe", "pistolety", "pistolety-maszynowe", "rewolwery",
"specjalne", "stacjonarne", "strzelby", "wyrzutnie-granatów"]

sciezki_obrazy = ["kamizelki", "pojemniki", "ammunicja", "kamizelki-taktyczne", "bronie", "helmy"]
sciezki_ammunicja = [".45 ACP", ".300 Blackout", ".338 Lapua Magnum", ".357 Magnum", ".366 TKM", "4.6x30 HK", "5.7x28 FN", "5.45x39", "5.56x45 NATO", "7.62x25 Tokarev",
"7.62x39", "7.62x51 NATO", "7.62x54", "9x18 Makarov", "9x19 Parabellum", "9x21 Gyurza", "12.7x55 STs-130", "12x70", "20x70", "23x75", "40x46", "Stationary Weapons"]

#Funkcja tworząca ścieżkę bronie/...
def directory():
    bronie = os.path.exists("bronie")
    if bronie == False:
        os.mkdir("bronie")
    for x in sciezki_bronie:
        directory = os.path.exists(f'bronie/{x}')
        if directory == False:
            os.mkdir(f"bronie/{x}")

#Funkcja tworząca ścieżkę obrazy/...
def directory2():
    obrazy = os.path.exists("obrazy")
    if obrazy == False:
        os.mkdir("obrazy")
    for x in sciezki_obrazy:
        directory = os.path.exists(f"obrazy/{x}")
        if directory == False:
            os.mkdir(f"obrazy/{x}")
    for y in sciezki_ammunicja:
        ammunicja = os.path.exists(f'obrazy/ammunicja/{y}')
        if ammunicja == False:
            os.mkdir(f'obrazy/ammunicja/{y}')


first1 = ["wykresy", "ammunicja", "kamizelki", "helmy", "zadania", "kryjowka"]
second2 = ["zadania/prapor", "zadania/therapist", "zadania/skier", "zadania/peacekeeper",
"zadania/mechanic", "zadania/ragman", "zadania/jaeger", "zadania/fence", "zadania/lightkeeper",
"kryjowka/biblioteka", "kryjowka/centrum-wywiadu", "kryjowka/choinka",
"kryjowka/filtr-powietrza", "kryjowka/fotowoltaika", "kryjowka/generator-alko", "kryjowka/generator-pradu",
"kryjowka/kolektor-wody", "kryjowka/koparka-krypto", "kryjowka/kuchnia", "kryjowka/lozko", "kryjowka/ochrona",
"kryjowka/ogrzewanie", "kryjowka/oswietlenie", "kryjowka/pojemnik-scava", "kryjowka/silownia", "kryjowka/stacja-medyczna",
"kryjowka/stol", "kryjowka/strzelnica", "kryjowka/szafa", "kryjowka/toaleta", "kryjowka/wentylacja"]

def check_all_dir(name):
    for x in name:
        path = os.path.exists(x)
        if path == False:
            os.mkdir(x)
            continue
        else:
            continue