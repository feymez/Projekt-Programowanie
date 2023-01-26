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

armors = ["5.11_Hexgrid.png", "5.11_TacTec.png", "6B2.png", "6B3TM-01M.png", "6B5-15.png", "6B5-16.png", "6B13.png", "6B13M.png", "6B23-1.png", "6B23-2.png", "6B43.png", "AA_A18.png", "AA_CPC_MOD2.png", "ANA_M1.png", "ANA_M2.png", "BNTI_Kirasa.png", 
"BNTI_Module-3M.png", "BNTI_Zhuk-6a.png", "CP_AVS.png", "CP_CPC.png", "CP_Precision_AVS_MBAV.png", "CQC_MK4A_Protection.png", "CQC_MK4A.png", "DRD.png", "EI_MMAC.png", "FORT_Defender-2.png", "FORT_Redut-M.png", "FORT_Redut-T5.png", 
"Gen4HMK.png", "Gzhel-K.png", "Hexatac_HPC.png", "Highcom_Trooper_TFO.png", "IOTV_Gen4_FP.png", "IOTV_Gen4.png", "Korund-VM.png", "LBT-6094A.png", "MF-UNTAR.png", "npp_klass_bagariy.png", "PACA_Rivals_Edition.png", "PACA.png", "RBAV-AF.png",
"S&S_Precision.png", "Shellback_Tactical_Banshee.png", "Strandhogg.png", "tasmanian_tiger_sk.png", "THOR_Concealable.png", "THOR_IC.png", "Wartech_TV-110.png", "Zhuk-3_Press.png"]
helmets = ["6B47_Ratnik-BSh_helmet.gif", "Altyn_bulletproof_helmet.png", "BNTI_LShZ-2DTM_helmet.png", "Bomber_Beanie.png", "Crye_Precision_AirFrame_helmet.png", "DevTac_Ronin_ballistic_helmet.png", 
"Diamond_Age_Bastion_helmet.png", "FORT_Kiver-M_bulletproof_helmet.png", "Galvion_Caiman_Hybrid_helmet.png", "HighCom_Striker_ACHHC_IIIA_helmet.gif", "HighCom_Striker_ULACH_IIIA_helmet.gif", 
"Jack-o-lantern_tactical_pumpkin_helmet.png", "Kolpak-1S_riot_helmet.png", "LShZ_light_helmet.png", "Maska-1SCh_bulletproof_helmet.gif", "MSA_ACH_TC-2001_MICH_Series_helmet.png", "MSA_ACH_TC-2002_MICH_Series_helmet.png", 
"MSA_Gallet_TC_800_High_Cut_combat_helmet.png", "NFM_'HJELM'_helmet.png", "Ops-Core_FAST_MT_Super_High_Cut_helmet.gif", "PSh-97_DJETA_riot_helmet.png", "Rys-T_bulletproof_helmet.png", "ShPM_Firefighter_helmet.png", "SSh-68_steel_helmet.png",
"SSSh-94_SFERA-S_helmet.png", "Tac-Kek_FAST_MT_helmet_replica.png", "Team_Wendy_EXFIL_Ballistic_Helmet.gif", "TSh-4M-L_soft_tank_crew_helmet.png", "UNTAR_helmet.png", "Vulkan-5_LShZ-5_bulletproof_helmet.png", "ZSh-1-2M_helmet.gif"]
containers = ["Ammo_case.png", "Docs_case.png", "dogtag_case.png", "gingy.png", "Grenade_case.png", "Injector_case.png", "Items_case.png", "Junkbox.png", "key_tool.png", "keycard_holder.png", "Magazine_box.png", "Medicine_case.png",
"Money_case.png", "Mr._Holodilnick_thermobag.png", "Pistol_case.png", "SICC_pouch.png", "THICCItems_case.png", "THICCWeapon_case.png", "Wallet.png", "Weapon_case.png", "wz_wallet.png"]

acp_45 = ["45_ACP_AP.png", "45_ACP_Hydra-Shok.png", "45_ACP_Lasermatch_FMJ.png", "45_ACP_Match_FMJ.png", "45_ACP_RIP.png"]
blackout_300 = ["300_AP.png", "300_BCP_FMJ.png", "300_M62_Tracer.png", "300_V-Max.png", "300_Whisper.png"]
lapua_magnum_338 = ["338_Lapua_Magnum_AP.png", "338_Lapua_Magnum_FMJ.png", "338_Lapua_Magnum_TAC-X.png", "338_Lapua_Magnum_UCW.png"]
magnum_357 = ["357_FMJ.png", "357_HP.png", "357_JHP.png", "357_SP.png"]
tkm_366 = ["366_TKM_AP-M.png", "366_TKM_EKO.png", "366_TKM_FMJ.png", "366_TKM_Geksa.png"]
hk_4630 = ["4.630_Action_SX.png", "4.630_AP_SX.png", "4.630_FMJ_SX.png", "4.630_Subsonic_SX.png"]
fn_5728 = ["5.728_L191.png", "5.728_R37.F.png", "5.728_R37.X.png", "5.728_SB193.png", "5.728_SS190.png", "5.728_SS197SR.png", "5.728_SS198LF.png"]
mm_54539 = ["5.4539_7N40.png", "5.4539_BP_gs.png", "5.4539_BS_gs.png", "5.4539_BT_gs.png", "5.4539_FMJ.png", "5.4539_HP.png", "5.4539_PP_gs.png", "5.4539_PPBS_gs_'Igolnik'.png", "5.4539_PRS_gs.png", "5.4539_PS_gs.png",
"5.4539_SP.png", "5.4539_T_gs.png", "5.4539_US_gs.png"]
nato_55645 = ["5.5645_FMJ.png", "5.5645_HP.png", "5.5645_M855.png", "5.5645_M855A1.png", "5.5645_M856.png", "5.5645_M856A1.png", "5.5645_M995.png", "5.5645_MK_255_MOD0_RRLP.png", "5.5645_MK_318_MOD0_SOST.png",
"5.5645_SSA_AP.png", "5.5645_Warmageddon.png"]
tokarev_76225 = ["7.6225_TT_FMJ43.png", "7.6225_TT_LRN.png", "7.6225_TT_AKBS.png", "7.6225_TT_LRNPC.png", "7.6225_TT_P_gl.png", "7.6225_TT_Pst_gzh.png", "7.6225_TT_PT_gzh.png"]
mm_76239 = ["7.6239_BP_gzh.png", "7.6239_HP.png", "7.6239_MAI_AP.png", "7.6239_PS_gzh.png", "7.6239_T-45M1_gzh.png", "7.6239_US_gzh.png"]
nato_76251 = ["7.6251_BCP_FMJ.png", "7.6251_M61.png", "7.6251_M62_Tracer.png", "7.6251_M80.png", "7.6251_M993.png", "7.6251_TCW_SP.png", "7.6251_Ultra_Nosler.png"]
mm_76254 = ["7.6254_R_BS_gs.png", "7.6254_R_BT_gzh.png", "7.6254_R_LPS_gzh.png", "7.6254_R_PS_gzh.png", "7.6254_R_SNB_gzh.png", "7.6254_R_T-46M_gzh.png"]
makarov_918 = ["918_PM_BZhT_gzh.png", "918_PM_P_gzh.png", "918_PM_PBM_gzh.png", "918_PM_PPe_gzh.png", "918_PM_PPT_gzh.png", "918_PM_PRS_gs.png", "918_PM_PS_gs.png", "918_PM_PSO_gzh.png", "918_PM_Pst_gzh.png",
"918_PM_PSV.png", "918_PM_RG028_gzh.png", "918_PM-SP7_gzh.png", "918_PM-SP8_gzh.png", "918_PMM_PstM_gzh.png"]
parabellum_919 = ["919_AP_6.3.png", "919_Green_Tracer.png", "919_Luger_CCI.png", "919_PBP_gzh.png", "919_PSO_gzh.png", "919_Pst_gzh.png", "919_QuakeMaker.png", "919_RIP.png"]
gyurza_921 = ["921_BT_gzh.png", "921_P_gzh.png", "921_PE_gzh.png", "921_PS_gzh.png"]
mm_939 = ["939_BP_gs.png", "939_PAB-9_gs.png", "939_SP-5_gs.png", "939_SP-6_gs.png", "939_SPP_gs.png"]
STs = ["12.755_PS12.png", "12.755_PS12A.png", "12.755_PS12B.png"]
mm_1270 = ["1270_.50_BMG.png", "1270_7mm_Buckshot.png", "1270_65mm_Express_buckshot.png", "1270_85mm_Magnum_buckshot.png", "1270_525mm_Buckshot.png", "1270_AP-20.png", "1270_CSP_HP.png", "1270_Dual_Sabot.png", "1270_Flechette.png",
"1270_FTX.png", "1270_Grizzly_40.png", "1270_Lead_slug.png", "1270_Poleva-3.png", "1270_Poleva-6u.png", "1270_Rip.png", "1270_SFHP.png"]
mm_2070 = ["2070_56mm_Buckshot.png", "2070_62mm_Buckshot.png", "2070_73mm_Buckshot.png", "2070_75mm_Buckshot.png", "2070_Devastator.png", "2070_Elephant_killer.png", "2070_Explosive.png",
"2070_Flechetta_plus.png", "2070_Poleva-3.png", "2070_Poleva-6u.png", "2070_Star.png"]
mm_2375 = ["2375_Barrikada.png", "2375_Sharpnel-10.png", "2375_Sharpnel-25.png", "2375_Zvezda.png"]
mm_4046 = ["4046_M576.png"]
stationary_weapons = ["12.7108_B-32.png", "12.7108_BZT-44M.png", "3029_VOG-30.png"]

plecaki = ["3V_Gear_Paratus_3-Day_Operator_s_Tactical_backpack.png", "6Sh118_raid_backpack.png", "ANA_Tactical_Beta_2_Battle_backpack.png", "Camelbak_Tri-Zip_assault_backpack.png",
"Duffle_bag.png", "Eberlestock_F4_Terminator_load_bearing_backpack.png", "Eberlestock_F5_Switchblade_backpack.png", "Eberlestock_G2_Gunslinger_II_backpack.png",
"Flyye_MBSS_backpack.png", "Gruppa_99_T20_backpack.gif", "Gruppa_99_T30_backpack.gif", "Hazard_4_Drawbridge_backpack.png", "Hazard_4_Pillbox_backpack.png",
"Hazard_4_Takedown_sling_backpack.gif", "LBT-1476A_3Day_Pack.png", "LBT-8005A_Day_Pack_backpack.png", "LolKek_3F_Transfer_tourist_backpack.png", "Mystery_Ranch_Blackjack_50_backpack.png",
"Mystery_Ranch_NICE_COMM_3_BVS_frame_system.png", "Oakley_Mechanism_heavy_duty_backpack.png", "Pilgrim_tourist_backpack.png", "Sanitar_s_bag.png", "Santa_s_Bag.png", "Scav_backpack.png",
"SSO_Attack_2_raid_backpack.png", "Tactical_sling_bag.png", "Tasmanian_Tiger_Trooper_35_backpack.png", "Transformer_Bag.png", "VKBO_army_bag.png", "WARTECH_Berkut_BB-102_backpack.png"]
kamizelki_taktyczne = ["6B5-16_Zh-86_Uley_armored_rig.png", "Eagle_Industries_'MMAC'_plate_carrier_Ranger_Green.png", "Shellback_Tactical_Banshee_plate_carrier_A-Tacs_AU.png", "Ars_Arma_A18_Skanda_plate_carrier.png",
"WARTECH_TV-110_plate_carrier_rig.png", "FirstSpear_'Strandhogg'_plate_carrier_rig_Ranger_Green.png", "ECLiPSE_RBAV-AF_plate_carrier_Ranger_Green.png", "CQC_Osprey_MK4A_plate_carrier_Assault,_MTP.png",
"6B3TM-01M_armored_rig.png", "6B5-15_Zh-86_Uley_armored_rig.png", "ANA_Tactical_M2_armored_rig.png", "ANA_Tactical_M1_armored_rig.png", "Crye_Precision_AVS_plate_carrier.png", "5.11_Tactical_TacTec_plate_carrier.png",
"Ars_Arma_CPC_MOD.2_plate_carrier.png", "Crye_Precision_CPC_plate_carrier_Goons_Edition.png", "S&S_Precision_PlateFrame_plate_carrier_Goons_Edition.png", "CQC_Osprey_MK4A_plate_carrier_Protection,_MTP.png",
"NPP_KlASS_Bagariy_armored_rig.png", "Tasmanian_Tiger_SK_plate_carrier_Multicam_Black.png", "Crye_Precision_AVS_MBAV_Tagilla_Edition.png", "Scav_Vest.png", "Security_vest.png", "DIY_IDEA_chest_rig.png",
"Spiritus_Systems_Bank_Robber_chest_rig.png", "SOE_Micro_Rig.png", "WARTECH_TV-109_+_TV-106_chest_rig.png", "CSA_chest_rig.png", "UMTBS_6sh112_Scout-Sniper.png", "Azimut_SS_'Khamelion'_chest_harness_Olive.png",
"Splav_Tarzan_M22_chest_rig.png", "Haley_Strategic_D3CRX_Chest_Harness.png", "Dynaforce_Triton_M43-A_chest_harness.png", "BlackHawk!_Commando_chest_harness.gif", "Direct_Action_Thunderbolt_compact_chest_rig.png",
"Gear_Craf_GC-BSS-MK1_chest_rig.png", "Umka_M33-SET1_hunter_vest.png", "LBT-1961A_Load_Bearing_Chest_Rig.png", "LBT-1961A_Load_Bearing_Chest_Rig_Goons_Edition.png", "Stich_Profi_Chest_Rig_MK2_Recon,_A-TACS_FG.png",
"Stich_Profi_Chest_Rig_MK2_Assault,_A-TACS_FG.png", "BlackRock_chest_rig.png", "WARTECH_MK3_TV-104_chest_rig.png", "ANA_Tactical_Alpha_chest_rig.png", "Azimut_SS_'Zhuk'_chest_harness.png",
"Velocity_Systems_MPPV_Multi-Purpose_Patrol_Vest.png", "Beltcombo.png"]

medykamenty = ["Analgin_painkillers.png", "Augmentin_antibiotic_pills.png", "Ibuprofen_painkillers.png", "Vaseline_balm.png",
"Golden_Star_balm.png", "Immobilizing_splint.png", "Aluminum_splint.png", "CMS_surgical_kit.png", "Surv12_field_surgical_kit.png",
"Aseptic_bandage.png", "Army_bandage.png", "Esmarch_tourniquet.png", "CALOK-B_hemostatic_applicator.png", "CAT_hemostatic_tourniquet.png",
"AI-2_medkit.png", "Car_first_aid_kit.png", "Salewa_first_aid_kit.png", "IFAK_individual_first_aid_kit.png",
"AFAK_tactical_individual_first_aid_kit.png", "Grizzly_medical_kit.png"]

json_files = ["ammunition.json", "armors.json", "backpacks.json", "chestrigs.json", "containers.json",
"headgear.json", "medykamenty/medicaments.json"]

#Funkcja sprawdzająca połączenie z internetem
def check_connect():
    try:
        urllib.request.urlopen('http://google.com/')
        return True
    except:
        return False

#Pętla pobierająca pliki JSON broni
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

#Pętla pobierająca pliki PNG / GIF
def loop2(list_name, category):
    for x in list_name:
        file = os.path.isfile(f'obrazy/{category}/{x}')
        if file == False:
            internet_connection = check_connect()
            if internet_connection == False:
                print("Komputer nie ma połączenia z internetem.")
                quit()
            else:
                url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/{category}/{x}'
                response = requests.get(url)
                open(f'obrazy/{category}/{x}', 'wb').write(response.content)

#Pętla pobierająca pliki PNG ammunicji
def loop3(list_name, caliber):
    for x in list_name:
        file = os.path.isfile(f"obrazy/ammunicja/{caliber}/{x}")
        if file == False:
            internet_connection = check_connect()
            if internet_connection == False:
                print("Komputer nie ma połączenia z internetem.")
                quit()
            else:
                if caliber == ".45 ACP":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/.45%20ACP/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/.45 ACP/{x}', 'wb').write(response.content)
                elif caliber == ".300 Blackout":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/.300%20Blackout/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/.300 Blackout/{x}', 'wb').write(response.content)
                elif caliber == ".338 Lapua Magnum":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/.338%20Lapua%20Magnum/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/.338 Lapua Magnum/{x}', 'wb').write(response.content)
                elif caliber == ".357 Magnum":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/.357%20Magnum/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/.357 Magnum/{x}', 'wb').write(response.content)
                elif caliber == ".366 TKM":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/.366%20TKM/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/.366 TKM/{x}', 'wb').write(response.content)
                elif caliber == "4.6x30 HK":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/4.6x30%20HK/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/4.6x30 HK/{x}', 'wb').write(response.content)
                elif caliber == "5.7x28 FN":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/5.7x28%20FN/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/5.7x28 FN/{x}', 'wb').write(response.content)
                elif caliber == "5.45x39":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/5.45x39/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/5.45x39/{x}', 'wb').write(response.content)
                elif caliber == "5.56x45 NATO":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/5.56x45%20NATO/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/5.56x45 NATO/{x}', 'wb').write(response.content)
                elif caliber == "7.62x25 Tokarev":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/7.62x25%20Tokarev/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/7.62x25 Tokarev/{x}', 'wb').write(response.content)
                elif caliber == "7.62x39":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/7.62x39/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/7.62x39/{x}', 'wb').write(response.content)
                elif caliber == "7.62x51 NATO":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/7.62x51%20NATO/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/7.62x51 NATO/{x}', 'wb').write(response.content)
                elif caliber == "7.62x54":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/7.62x54/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/7.62x54/{x}', 'wb').write(response.content)
                elif caliber == "9x18 Makarov":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/9x18%20Makarov/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/9x18 Makarov/{x}', 'wb').write(response.content)
                elif caliber == "9x19 Parabellum":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/9x19%20Parabellum/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/9x19 Parabellum/{x}', 'wb').write(response.content)
                elif caliber == "9x21 Gyurza":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/9x21%20Gyurza/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/9x21 Gyurza/{x}', 'wb').write(response.content)
                elif caliber == "9x39":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/9x39/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/9x39/{x}', 'wb').write(response.content)
                elif caliber == "12.7x55 STs-130":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/12.7x55%20STs-130/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/12.7x55 STs-130/{x}', 'wb').write(response.content)
                elif caliber == "12x70":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/12x70/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/12x70/{x}', 'wb').write(response.content)
                elif caliber == "20x70":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/20x70/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/20x70/{x}', 'wb').write(response.content)
                elif caliber == "23x75":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/23x75/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/23x75/{x}', 'wb').write(response.content)
                elif caliber == "40x46":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/40x46/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/40x46/{x}', 'wb').write(response.content)
                elif caliber == "Stationary Weapons":
                    url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/obrazy/ammunicja/Stationary%20Weapons/{x}'
                    response = requests.get(url)
                    open(f'obrazy/ammunicja/Stationary Weapons/{x}', 'wb').write(response.content)
    

#Pętla pobierająca pliki JSON
def loop4(files):
    for x in files:
        file = os.path.isfile(x)
        if file == False:
            internet_connection = check_connect()
            if internet_connection == False:
                print("Komputer nie ma połączenia z internetem.")
                quit()
            else:
                url = f'https://raw.githubusercontent.com/feymez/Projekt-Programowanie/main/{x}'
                response = requests.get(url)
                open(f'{x}', 'wb').write(response.content)


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
    loop2(helmets, "helmy")
    loop2(containers, "pojemniki")
    loop2(plecaki, "plecaki")
    loop2(kamizelki_taktyczne, "kamizelki-taktyczne")
    loop2(medykamenty, "medykamenty")

#Funkcja sprawdzająca spójność plików PNG ammunicji.
def check3():
    directories.directory2()
    loop3(acp_45, ".45 ACP")
    loop3(blackout_300, ".300 Blackout")
    loop3(lapua_magnum_338, ".338 Lapua Magnum")
    loop3(magnum_357, ".357 Magnum")
    loop3(tkm_366, ".366 TKM")
    loop3(hk_4630, "4.6x30 HK")
    loop3(fn_5728, "5.7x28 FN")
    loop3(mm_54539, "5.45x39")
    loop3(nato_55645, "5.56x45 NATO")
    loop3(tokarev_76225, "7.62x25 Tokarev")
    loop3(mm_76239, "7.62x39")
    loop3(nato_76251, "7.62x51 NATO")
    loop3(mm_76254, "7.62x54")
    loop3(makarov_918, "9x18 Makarov")
    loop3(parabellum_919, "9x19 Parabellum")
    loop3(gyurza_921, "9x21 Gyurza")
    loop3(mm_939, "9x39")
    loop3(STs, "12.7x55 STs-130")
    loop3(mm_1270, "12x70")
    loop3(mm_2070, "20x70")
    loop3(mm_2375, "23x75")
    loop3(mm_4046, "40x46")
    loop3(stationary_weapons, "Stationary Weapons")

def check4():
    loop4(json_files)