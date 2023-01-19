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
        time.sleep(2)
    for x in sciezki_bronie:
        directory = os.path.exists(f'bronie/{x}')
        if directory == False:
            os.mkdir(f"bronie/{x}")
            time.sleep(1)

#Funkcja tworząca ścieżkę obrazy/...
def directory2():
    obrazy = os.path.exists("obrazy")
    if obrazy == False:
        os.mkdir("obrazy")
        time.sleep(2)
    for x in sciezki_obrazy:
        directory = os.path.exists(f"obrazy/{x}")
        if directory == False:
            os.mkdir(f"obrazy/{x}")
            time.sleep(1)
    for y in sciezki_ammunicja:
        ammunicja = os.path.exists(f'obrazy/ammunicja/{y}')
        if ammunicja == False:
            os.mkdir(f'obrazy/ammunicja/{y}')
            time.sleep(1)