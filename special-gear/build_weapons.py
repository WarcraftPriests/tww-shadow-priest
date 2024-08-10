"""
builds weapon strings
python build_weapons.py
"""

enchant = "enchant=authority_of_the_depths_3"

one_hands = {
    "1h_Unceremonious_Bloodletter_639": "main_hand=unceremonious_bloodletter,id=221165,ilevel=639",
    "1h_Kingslayers_Frostfang_639": "main_hand=kingslayers_frostfang,id=221171,ilevel=639",
    "1h_Scithewood_Scepter_639": "main_hand=scithewood_scepter,id=178709,ilevel=639",
    "1h_Wand_of_Untainted_Power_639": "main_hand=wand_of_untainted_power,id=133288,ilevel=639",
    "1h_Scepter_of_Manifested_Miasma_639": "main_hand=scepter_of_manifested_miasma,id=212404,ilevel=639",
    "1h_Sovereigns_Disdain_639": "main_hand=sovereigns_disdain,id=212394,ilevel=639",
}

off_hands = {
    "OH_Pail_of_Preserved_Obscurity_639": "off_hand=pail_of_preserved_obscurity,id=221172,ilevel=639",  # noqa: E501
}

combos = [(mh, oh) for mh in one_hands.keys() for oh in off_hands.keys()]

for combo in combos:
    name = combo[0] + "-" + combo[1]
    mh = one_hands[combo[0]] + f",{enchant}"
    oh = off_hands[combo[1]]
    profileset = f"profileset.\"{name}\"+={mh}\nprofileset.\"{name}\"+={oh}\n"
    print(profileset)
