import os, requests, time, directories
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

armors = ["5.11_Hexgrid", "5.11_TacTec", "6B2", "6B3TM-01M", "6B5-15", "6B5-16", "6B13", "6B13M", "6B23-1", "6B23-2", "6B43", "AA_A18", "AA_CPC_MOD2", "ANA_M1", "ANA_M2", "BNTI_Kirasa", 
"BNTI_Module-3M", "BNTI_Zhuk-6a", "CP_AVS", "CP_CPC", "CP_Precision_AVS_MBAV", "CQC_MK4A_Protection", "CQC_MK4A", "DRD", "EI_MMAC", "FORT_Defender-2", "FORT_Redut-M", "FORT_Redut-T5", 
"Gen4HMK", "Gzhel-K", "Hexatac_HPC", "Highcom_Trooper_TFO", "IOTV_Gen4_FP", "IOTV_Gen4", "Korund-VM", "LBT-6094A", "MF-UNTAR", "npp_klass_bagariy", "PACA_Rivals_Edition", "PACA", "RBAV-AF",
"S&S_Precision", "Shellback_Tactical_Banshee", "Strandhogg", "tasmanian_tiger_sk", "THOR_Concealable", "THOR_IC", "Wartech_TV-110", "Zhuk-3_Press"]

acp_45 = ["45_ACP_AP", "45_ACP_Hydra-Shok", "45_ACP_Lasermatch_FMJ", "45_ACP_Match_FMJ", "45_ACP_RIP"]
blackout_300 = ["300_AP", "300_BCP_FMJ", "300_M62_Tracer", "300_V-Max", "300_Whisper"]
lapua_magnum_338 = ["338_Lapua_Magnum_AP", "338_Lapua_Magnum_FMJ", "338_Lapua_Magnum_TAC-X", "338_Lapua_Magnum_UCW"]
magnum_357 = ["357_FMJ", "357_HP", "357_JHP", "357_SP"]
tkm_366 = ["366_TKM_AP-M", "366_TKM_EKO", "366_TKM_FMJ", "366_TKM_Geksa"]
hk_4630 = ["4.630_Action_SX", "4.630_AP_SX", "4.630_FMJ_SX", "4.630_Subsonic_SX"]
fn_5728 = ["5.728_L191", "5.728_R37.F", "5.728_R37.X", "5.728_SB193", "5.728_SS190", "5.728_SS197SR", "5.728_SS198LF"]
mm_54539 = ["5.4539_7N40", "5.4539_BP_gs", "5.4539_BS_gs", "5.4539_BT_gs", "5.4539_FMJ", "5.4539_HP", "5.4539_PP_gs", "5.4539_PPBS_gs_'Igolnik'", "5.4539_PRS_gs", "5.4539_PS_gs",
"5.4539_SP", "5.4539_T_gs", "5.4539_US_gs"]
nato_55645 = ["5.5645_FMJ", "5.5645_HP", "5.5645_M855", "5.5645_M855A", "5.5645_M856", "5.5645_856A", "5.5645_M995", "5.5645_MK_255_MOD0_RRLP", "5.5645_MK_318_MOD0_SOST",
"5.5645_SSA_AP", "5.5645_Warmageddon"]
tokarev_76225 = ["7.6225_T_FMJ43", "7.6225_T_LRN", "7.6225_TT_AKBS", "7.6225_TT_LRNPC", "7.6225_TT_P_gl", "7.6225_TT_Pst_gzh", "7.6225_TT_PT_gzh"]
mm_76239 = ["7.6239_BP_gzh", "7.6239_HP", "7.6239_MAI_AP", "7.6239_PS_gzh", "7.6239_T-45M1_gzh", "7.6239_US_gzh"]
nato_76251 = ["7.6251_BCP_FMJ", "7.6251_M61", "7.6251_M62_Tracer", "7.6251_M80", "7.6251_M993", "7.6251_TCW_SP", "7.6251_Ultra_Nosler"]
mm_76254 = ["7.6254_R_BS_gs", "7.6254_R_BT_gzh", "7.6254_R_LPS_gzh", "7.6254_R_PS_gzh", "7.6254_R_SNB_gzh", "7.6254_R_T-46M_gzh"]
makarov_918 = ["918_PM_BZhT_gzh", "918_PM_P_gzh", "918_PM_PBM_gzh", "918_PM_PPe_gzh", "918_PM_PPT_gzh", "918_PM_PRS_gs", "918_PM_PS_gs", "918_PM_PSO_gzh", "918_PM_Pst_gzh",
"918_PM_PSV", "918_PM_RG028_gzh", "918_PM-SP7_gzh", "918_PM-SP8_gzh", "918_PMM_PstM_gzh"]
parabellum_919 = ["919_AP_6.3", "919_Green_Tracer", "919_Luger_CCI", "919_PBP_gzh", "919_PSO_gzh", "919_Pst_gzh", "919_QuakeMaker", "919_RIP"]
gyurza_921 = ["921_BT_gzh", "921_P_gzh", "921_PE_gzh", "921_PS_gzh"]
mm_939 = ["939_BP_gs", "939_PAB-9_gs", "939_SO-5_gs", "939_SP-6_gs", "939_SPP_gs"]
STs = ["12.55_PS12", "12.55_PS12A", "12.55_PS12B"]
mm_1270 = ["1270_.50_BMG", "1270_7mm_Buckshot", "1270_65mm_Express_buckshot", "1270_85mm_Magnum_buckshot", "1270_AP-20", "1270_CSP_HP", "1270_Dual_Sabot", "1270_Flechette",
"1270_FTX", "1270_Grizzly_40", "1270_Lead_slug", "1270_Poleva-3", "1270_Poleva-6u", "1270_Rip", "1270_SFHP"]
mm_2070 = ["2070_56mm_Buckshot", "2070_62mm_Buckshot", "2070_73mm_Buckshot", "2070_75mm_Buckshot", "2070_Devastator", "2070_Elephant_killer", "2070_Explosive",
"2070_Flechetta_plus", "2070_Poleva-3", "2070_Poleva-6u", "2070_Star"]
mm_2375 = ["2375_Barrikada", "2375_Sharpnel-10", "2375_Sharpnel-25", "2375_Zvezda"]
mm_4046 = ["4046_M576"]
stationary_weapons = ["12.7108_B-32", "12.7108_BZT-44M", "3029_VOG-30"]

#Funkcja sprawdzająca połączenie z internetem
def check_connect():
    try:
        urllib.request.urlopen('http://google.com/')
        return True
    except:
        return False

#Pętla pobierająca pliki JSON
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

#Pętla pobierająca pliki PNG
def loop2(list_name, category):
    for x in list_name:
        file = os.path.isfile(f'obrazy/{category}/{x}.png')
        if file == False:
            internet_connection = check_connect()
            if internet_connection == False:
                print("Komputer nie ma połączenia z internetem.")
                quit()
            else:
                url = f'https://github.com/feymez/Projekt-Programowanie/blob/main/obrazy/{category}/{x}.png'
                response = requests.get(url)
                open(f'obrazy/{category}/{x}.png', 'wb').write(response.content)

#Pętla pobierająca pliki PNG ammunicji
def loop3(list_name, category, caliber):
    for x in list_name:
        file = os.path.isfile(f"obrazy/{category}/{caliber}/{x}.png")
        if file == False:
            internet_connection = check_connect()
            if internet_connection == False:
                print("Komputer nie ma połączenia z internetem.")
                quit()
            else:
                url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/{category}/{caliber}/{x}.png'
                response = requests.get(url)
                open(f'obrazy/{category}/{caliber}/{x}.png', 'wb').write(response.content)

    
#Funkcja sprawdzająca spójność plików JSON broni.
def check():
    directories.directory()
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

#Funkcja sprawdzająca spójność plików PNG.
def check2():
    directories.directory2()
    loop2(armors, "kamizelki")

#Funkcja sprawdzająca spójność plików PNG ammunicji.
def check3():
    directories.directory2()
    loop3(acp_45, "ammunicja", ".45 ACP")
    loop3(blackout_300, "ammunicja", ".300 Blackout")
    loop3(lapua_magnum_338, "ammunicja", ".338 Lapua Magnum")
    loop3(magnum_357, "ammunicja", ".357 Magnum")
    loop3(tkm_366, "ammunicja", ".366 TKM")
    loop3(hk_4630, "ammunicja", "4.6x30 HK")
    loop3(fn_5728, "ammunicja", "5.7x28 FN")
    loop3(mm_54539, "ammunicja", "5.45x39")
    loop3(nato_55645, "ammunicja", "5.56x45 NATO")
    loop3(tokarev_76225, "ammunicja", "7.62x25 Tokarev")
    loop3(mm_76239, "ammunicja", "7.62x39")
    loop3(nato_55645, "ammunicja", "7.62x51 NATO")
    loop3(makarov_918, "ammunicja", "9x18 Makarov")
    loop3(parabellum_919, "ammunicja", "9x19 Parabellum")
    loop3(gyurza_921, "ammunicja", "9x21 Gyurza")
    loop3(mm_939, "ammunicja", "9x39")
    loop3(mm_1270, "ammunicja", "12x70")
    loop3(mm_2070, "ammunicja", "20x70")
    loop3(mm_2375, "ammunicja", "23x75")
    loop3(mm_4046, "ammunicja", "40x46")
    loop3(stationary_weapons, "ammunicja", "Stationary Weapons")