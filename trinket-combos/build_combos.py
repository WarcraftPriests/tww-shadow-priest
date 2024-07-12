"""
builds trinket strings
python build_combos.py
"""

from itertools import combinations

combos = {
    # s1 dungeons (?/639)
    "Ara_Kara_Sacbrood_639": "arakara_sacbrood,id=219314,ilevel=639",
    "Harvesters_Edict_639": "harvesters_edict,id=219317,ilevel=639",
    "Cirral_Concoctory_639": "cirral_concoctory,id=219321,ilevel=639",
    "High_Speakers_Accretion_639": "high_speakers_accretion,id=219303,ilevel=639",
    "Empowering_Crystal_of_Anubikkaj_639": "empowering_crystal_of_anubikkaj,id=219312,ilevel=639",
    "Unbound_Changeling_All_639": "unbound_changeling,id=178708,ilevel=639",
    "Unbound_Changeling_Crit_639": "unbound_changeling,id=178708,ilevel=639",
    "Unbound_Changeling_Haste_639": "unbound_changeling,id=178708,ilevel=639",
    "Unbound_Changeling_Mastery_639": "unbound_changeling,id=178708,ilevel=639",
    "Satchel_of_Misbegotten_Minions_639": "satchel_of_misbegotten_minions,id=178772,ilevel=639",
    "Hadals_Nautilus_639": "hadals_nautilus,id=159622,ilevel=639",
    # neru'bar palace (?/639)
    "Aberrant_Spellforge_639": "aberrant_spellforge,id=212451,ilevel=639",
    "Mad_Queens_Mandate_639": "mad_queens_mandate,id=212454,ilevel=639",
    "Spymasters_Web_639": "spymasters_web,id=220202,ilevel=639",
    "Ovinaxs_Mercurial_Egg_639": "ovinaxs_mercurial_egg,id=220305,ilevel=639",
    "Treacherous_Transmitter_639": "treacherous_transmitter,id=221023,ilevel=639",
    # delves (626)
    "Imperfect_Ascendancy_Serum_626": "imperfect_ascendancy_serum,id=225654,ilevel=626",
    "Quickwick_Candlestick_626": "quickwick_candlestick,id=225649,ilevel=626",
    # pvp (626)
    "Forged_Gladiators_Badge_of_Ferocity_626": "forged_gladiators_badge_of_ferocity,id=218713,ilevel=626",
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
