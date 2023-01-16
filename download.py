import os, requests, time
import urllib.request

karabinki_szturmowe = ["AS VAL", "OP-SKS", "SKS", "Vepr Hunter VPO-101"]
karabiny_snajperskie = ["AXMC", "DVL-10", "M700", "Mosin (Infantry)", "Mosin (Sniper)", "SV-98", "T-5000", "VPO-215"]
karabiny_szturmowe = ["ADAR 2-15", "AK-74", "AK-74M", "AK-74N", "AK-101", "AK-102", "AK-103", "AK-104", "AK-105", "AKM", "AKMN", "AKMS", "AKMSN", "AKS-74", "AKS-74N", "AKS-74U",
"AKS-74UB", "AKS-74UN", "ASh-12", "AUG A1", "AUG A3", "DT MDR 5.56x45", "DT MDR 7.62x51", "HK 416A5", "HK G36", "M4A1", "MCX", "Mk47", "RD-704", "SA-58", "SAG AK Short", "SAG AK",
"SCAR-H", "SCAR-L", "TX-15 DML", "Vepr AKM VPO-209", "Vepr KM VPO-136"]
karabiny_wyborowe = ["HK G28", "M1A", "Mk-18", "RFB", "RSASS", "SR-25", "SVDS", "VSS Vintorez"]
lekkie_karabiny_maszynowe = ["RPK-16"]
pistolety = ["APB", "APS", "FN 5-7", "Glock 17", "Glock 18C", "Glock 19X", "M9A3", "M45A1", "M1911A1", "MP-443 _Grach_", "P226R", "PB pistol", "PL-15", "PM (t) pistol",
"PM pistol", "SR-1MP Gyurza", "TT pistol (gold)", "TT pistol", "USP .45"]
pistolety_maszynowe = ["MP5", "MP5K", "MP7A1", "MP7A2", "MP9-N", "MP9", "MPX", "P90", "PP-9 _Klin_", "PP-19-01 Vityaz-SN", "PP-91 _Kedr_", "PP-91-01 _Kedr-B_", "PPSh-41",
"Saiga-9", "SR-2M", "STM-9", "UMP 45", "Vector .45", "Vector 9x19"]
rewolwery = ["CR50DS", "CR200DS", "RSh-12"]
specjalne = ["SP-81"]
stacjonarne = ["AGS-30", "NSV 'Utyos'"]
strzelby = ["KS-23M", "M3 Super 90", "M590A1", "M870", "MP-18", "MP-43-1C", "MP-133", "MP-153", "MP-155", "MTs-255-12", "Saiga-12", "TOZ-106"]
wyrzutnie_granatow = ["GL40", "M32A1"]
sciezki = ["karabinki-szturmowe", "karabiny-snajperskie", "karabiny-szturmowe", "karabiny-wyborowe", "lekkie-karabiny-maszynowe", "pistolety", "pistolety-maszynowe", "rewolwery",
"specjalne", "stacjonarne", "strzelby", "wyrzutnie-granatów"]

def check_connect():
    try:
        urllib.request.urlopen('http://google.com/')
        return True
    except:
        return False

def loop(list_name, category):
    for x in list_name:
        file = os.path.isfile(f'bronie/{category}/{x}.json')
        if file == False:
            internet_connection = check_connect()
            if internet_connection == False:
                print("Komputer nie ma połączenia z internetem.")
                quit()
            else:
                url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/bronie/{category}/{x}.json'
                response = requests.get(url)
                open(f'bronie/{category}/{x}.json', 'wb').write(response.content)

def directory():
    bronie = os.path.exists("bronie")
    internet_connection = check_connect()
    if internet_connection == False:
        print("Komputer nie ma połączenia z internetem.")
        quit()
    else:
        if bronie == False:
            os.mkdir("bronie")
            time.sleep(2)
        for x in sciezki:
            directory = os.path.exists(f'bronie/{x}')
            if directory == False:
                os.mkdir(f"bronie/{x}")
                time.sleep(1)

directory()
loop(karabinki_szturmowe, "karabinki-szturmowe")
loop(karabiny_snajperskie, "karabiny-snajperskie")
loop(karabiny_szturmowe, "karabiny-szturmowe")
loop(karabiny_wyborowe, "karabiny-wyborowe")
loop(lekkie_karabiny_maszynowe, "lekkie-karabiny-maszynowe")
loop(pistolety, "pistolety")
loop(pistolety_maszynowe, "pistolety-maszynowe")
loop(rewolwery, "rewolwery")
loop(specjalne, "specjalne")
loop(stacjonarne, "stacjonarne")
loop(strzelby, "strzelby")
loop(wyrzutnie_granatow, "wyrzutnie-granatów")