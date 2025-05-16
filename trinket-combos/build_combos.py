"""
builds trinket strings
python build_combos.py
"""

from itertools import combinations

combos = {
    # s2 dungeons (671/684)
    "Entropic_Skardyn_Core_671": "entropic_skardyn_core,id=219296,ilevel=671",
    "Entropic_Skardyn_Core_684": "entropic_skardyn_core,id=219296,ilevel=684",
    "Signet_of_the_Priory_671": "signet_of_the_priory,id=219308,ilevel=671",
    "Signet_of_the_Priory_684": "signet_of_the_priory,id=219308,ilevel=684",
    "Synergistic_Brewterializer_671": "synergistic_brewterializer,id=219299,ilevel=671",
    "Synergistic_Brewterializer_684": "synergistic_brewterializer,id=219299,ilevel=684",
    "Carved_Blazikon_Wax_671": "carved_blazikon_wax,id=219305,ilevel=671",
    "Carved_Blazikon_Wax_684": "carved_blazikon_wax,id=219305,ilevel=684",
    "Soulletting_Ruby_671": "soulletting_ruby,id=178809,ilevel=671",
    "Soulletting_Ruby_684": "soulletting_ruby,id=178809,ilevel=684",
    "Ingenious_Mana_Battery_671": "ingenious_mana_battery,id=169344,ilevel=671",
    "Ingenious_Mana_Battery_684": "ingenious_mana_battery,id=169344,ilevel=684",
    # Liberation of Undermine (671/684)
    "Geargrinders_Spare_Keys_684": "geargrinders_spare_keys,id=230197,ilevel=684",
    "Reverb_Radio_684": "reverb_radio,id=230194,ilevel=684",
    "House_of_Cards_671": "house_of_cards,id=230027,ilevel=671",
    "House_of_Cards_684": "house_of_cards,id=230027,ilevel=684",
    "Mugs_Moxie_Jug_671": "mugs_moxie_jug,id=230192,ilevel=671",
    "Mugs_Moxie_Jug_684": "mugs_moxie_jug,id=230192,ilevel=684",
    "Eye_of_Kezan_671": "eye_of_kezan,id=230198,ilevel=671",
    "Eye_of_Kezan_684": "eye_of_kezan,id=230198,ilevel=684",
    # delves (671)
    "Quickwick_Candlestick_671": "quickwick_candlestick,id=225649,ilevel=671",
    "Suspicious_Energy_Drink_671": "suspicious_energy_drink,id=235363,ilevel=671",
    "Funhouse_Lens_671": "funhouse_lens,id=234217,ilevel=671",
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
            # TWW S2 Options
            if "Synergistic_Brewterializer" in trinket:
                result += f"profileset.\"{profileset_name}\"+=priest.synergistic_brewterializer_tof_chance=0.90\n"
                result += f"profileset.\"{profileset_name}\"+=priest.synergistic_brewterializer_barrel_hit_chance=0.75\n"
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
