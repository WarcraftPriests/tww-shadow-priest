"""
builds trinket strings
python build_combos.py
"""

from itertools import combinations

combos = {
    # timewalking (619)
    # "Energy_Siphon_619": "energy_siphon,id=156021,ilevel=619",
    # "Living_Flame_619": "living_flame,id=155947,ilevel=619",
    # s2 dungeons (665/678)
    "Entropic_Skardyn_Core_678": "entropic_skardyn_core,id=219296,ilevel=678",
    # "Sigil_of_Algari_Concordance_678": "sigil_of_algari_concordance,id=219295,ilevel=678",
    "Signet_of_the_Priory_678": "signet_of_the_priory,id=219308,ilevel=678",
    # "Bursting_Lightshard_678": "bursting_lightshard,id=219310,ilevel=678",
    "Synergistic_Brewterializer_678": "synergistic_brewterializer,id=219299,ilevel=678",
    # "Remnant_of_Darkness_678": "remnant_of_darkness,id=219307,ilevel=678",
    "Carved_Blazikon_Wax_678": "carved_blazikon_wax,id=219305,ilevel=678",
    # "Gigazaps_Zap_Cap_678": "gigazaps_zapcap,id=232545,ilevel=678",
    "Soulletting_Ruby_678": "soulletting_ruby,id=178809,ilevel=678",
    "Ingenious_Mana_Battery_678": "ingenious_mana_battery,id=169344,ilevel=678",
    # Liberation of Undermine (665/678)
    "Geargrinders_Spare_Keys_678": "geargrinders_spare_keys,id=230197,ilevel=678",
    # "Flarendos_Pilot_Light_678": "flarendos_pilot_light,id=230191,ilevel=678",
    "Reverb_Radio_678": "reverb_radio,id=230194,ilevel=678",
    # "Mister_Lock_N_Stalk_678": "mister_locknstalk,id=230193,ilevel=678",
    "House_of_Cards_678": "house_of_cards,id=230027,ilevel=678",
    "Mugs_Moxie_Jug_678": "mugs_moxie_jug,id=230192,ilevel=678",
    "Eye_of_Kezan_678": "eye_of_kezan,id=230198,ilevel=678",
    # Nerubar
    "Spymasters_Web_639": "spymasters_web,id=220202,ilevel=639",
    # delves (665)
    "Quickwick_Candlestick_665": "quickwick_candlestick,id=225649,ilevel=665",
    # "Shadowbinding_Ritual_Knife_665": "shadowbinding_ritual_knife,id=215178,ilevel=665",
    "Suspicious_Energy_Drink_665": "suspicious_energy_drink,id=235363,ilevel=665",
    "Funhouse_Lens_665": "funhouse_lens,id=234217,ilevel=665",
    "Amorphous_Relic_665": "amorphous_relic,id=232891,ilevel=665",
    # pvp (?)
    "Prized_Gladiators_Badge_of_Ferocity_658": "prized_gladiators_badge_of_ferocity,id=229780,ilevel=658",
}


def item_id(trinket):
    """given a comma-separated definition for a trinket, returns just the id"""
    i = trinket.split(",")[1]
    return i[3:]


def build_combos():
    """generates the combination list with unique equipped trinkets only"""
    trinkets = combinations(combos.keys(), 2)
    unique_trinkets = []
    for pair in trinkets:
        # check if item id matches, trinkets are unique
        if item_id(combos[pair[0]]) != item_id(combos[pair[1]]):
            unique_trinkets.append(pair)
    print(f"Generated {len(unique_trinkets)} combinations.")
    return unique_trinkets


def build_simc_string(trinkets):
    """build profileset for each trinket combination"""
    result = ""
    for combo in trinkets:
        for trinket in combo:
            trinket_one = combo[0]
            trinket_two = combo[1]
            trinket_one_value = combos[trinket_one]
            trinket_two_value = combos[trinket_two]
            profileset_name = f"{trinket_one}-{trinket_two}"
            # TWW S1 Options
            if "Unbound_Changeling" in trinket:
                stat_type = trinket.split("_")[2].lower()
                result += f"profileset.\"{profileset_name}\"+=shadowlands.unbound_changeling_stat_type={stat_type}\n"
        result += f"profileset.\"{profileset_name}\"+=trinket1={trinket_one_value}\n"
        result += f"profileset.\"{profileset_name}\"+=trinket2={trinket_two_value}\n\n"
    return result


def generate_sim_file(input_string):
    """reads in the base simc file and creates the generated.simc file"""
    with open("base.simc", 'r', encoding="utf8") as file:
        data = file.read()
        file.close()
    with open("generated.simc", 'w+', encoding="utf8") as file:
        file.writelines(data)
        file.writelines(input_string)


if __name__ == '__main__':
    trinket_combos = build_combos()
    SIMC_STRING = build_simc_string(trinket_combos)
    generate_sim_file(SIMC_STRING)
