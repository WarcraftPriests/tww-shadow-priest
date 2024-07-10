"""weight dict definitions"""

weights_nerubar_palace = {
    'pw_ba_1': 0.050,
    'pw_sa_1': 0.113,
    'pw_na_1': 0.488,
    'lm_ba_1': 0.013,
    'lm_sa_1': 0.075,
    'lm_na_1': 0.138,
    'hm_ba_1': 0.000,
    'hm_sa_1': 0.000,
    'hm_na_1': 0.038,
    'pw_ba_2': 0.000,
    'pw_sa_2': 0.075,
    'pw_na_2': 0.000,
    'lm_ba_2': 0.000,
    'lm_sa_2': 0.013,
    'lm_na_2': 0.000,
    'hm_ba_2': 0.000,
    'hm_sa_2': 0.000,
    'hm_na_2': 0.000,
    'pw_ba_4': 0.000,
    'pw_sa_4': 0.000,
    'pw_na_4': 0.000,
    'lm_ba_4': 0.000,
    'lm_sa_4': 0.000,
    'lm_na_4': 0.000,
    'hm_ba_4': 0.000,
    'hm_sa_4': 0.000,
    'hm_na_4': 0.000,
    'pw_ba_3': 0.000,
    'pw_sa_3': 0.000,
    'pw_na_3': 0.000,
    'lm_ba_3': 0.000,
    'lm_sa_3': 0.000,
    'lm_na_3': 0.000,
    'hm_ba_3': 0.000,
    'hm_sa_3': 0.000,
    'hm_na_3': 0.000,
}

weights_single = {
    'pw_na_1': 0.73584905660,
    'lm_na_1': 0.20754716981,
    'hm_na_1': 0.05660377358,
}

weights_two_targets = {
    'pw_ba_2': 0.000,
    'pw_sa_2': 0.8571428571,
    'pw_na_2': 0.000,
    'lm_ba_2': 0.000,
    'lm_sa_2': 0.1428571429,
    'lm_na_2': 0.000,
    'hm_ba_2': 0.000,
    'hm_sa_2': 0.000,
    'hm_na_2': 0.000,
}

weights_three_targets = {
    'pw_ba_3': 0.0,
    'pw_sa_3': 0.0,
    'pw_na_3': 0.8,
    'lm_ba_3': 0.0,
    'lm_sa_3': 0.0,
    'lm_na_3': 0.2,
    'hm_ba_3': 0.0,
    'hm_sa_3': 0.0,
    'hm_na_3': 0.0,
}

weights_four_targets = {
    'pw_ba_4': 0.0,
    'pw_sa_4': 0.0,
    'pw_na_4': 0.8,
    'lm_ba_4': 0.0,
    'lm_sa_4': 0.0,
    'lm_na_4': 0.2,
    'hm_ba_4': 0.0,
    'hm_sa_4': 0.0,
    'hm_na_4': 0.0,
}

weights_season_one = {
    "algethar-fort": 0.0625,
    "algethar-tyran": 0.0625,
    "azure-fort": 0.0625,
    "azure-tyran": 0.0625,
    "cos-fort": 0.0625,
    "cos-tyran": 0.0625,
    "hov-fort": 0.0625,
    "hov-tyran": 0.0625,
    "nokhud-fort": 0.0625,
    "nokhud-tyran": 0.0625,
    "rlp-fort": 0.0625,
    "rlp-tyran": 0.0625,
    "smbg-fort": 0.0625,
    "smbg-tyran": 0.0625,
    "temple-fort": 0.0625,
    "temple-tyran": 0.0625,
}

# bring down overperforming keys to get a better composite
weights_standard_season_two = {
    "bhh-fort-standard": 0.0600,
    "bhh-tyran-standard": 0.0600,
    "freehold-fort-standard": 0.0575,
    "freehold-tyran-standard": 0.0575,
    "hoi-fort-standard": 0.0750,
    "hoi-tyran-standard": 0.0750,
    "neltharus-fort-standard": 0.0575,
    "neltharus-tyran-standard": 0.0575,
    "nelths-fort-standard": 0.0500,
    "nelths-tyran-standard": 0.0500,
    "ulda-fort-standard": 0.0650,
    "ulda-tyran-standard": 0.0650,
    "ur-fort-standard": 0.0675,
    "ur-tyran-standard": 0.0675,
    "vtp-fort-standard": 0.0675,
    "vtp-tyran-standard": 0.0675,
}

weights_push_season_two = {
    "bhh-fort-push": 0.0600,
    "bhh-tyran-push": 0.0600,
    "freehold-fort-push": 0.0575,
    "freehold-tyran-push": 0.0575,
    "hoi-fort-push": 0.0750,
    "hoi-tyran-push": 0.0750,
    "neltharus-fort-push": 0.0575,
    "neltharus-tyran-push": 0.0575,
    "nelths-fort-push": 0.0500,
    "nelths-tyran-push": 0.0500,
    "ulda-fort-push": 0.0650,
    "ulda-tyran-push": 0.0650,
    "ur-fort-push": 0.0675,
    "ur-tyran-push": 0.0675,
    "vtp-fort-push": 0.0675,
    "vtp-tyran-push": 0.0675,
}

weights_standard_season_three = {
    "atal-fort-push": 0.0625,
    "atal-tyran-push": 0.0625,
    "brh-fort-push": 0.0625,
    "brh-tyran-push": 0.0625,
    "dht-fort-push": 0.0625,
    "dht-tyran-push": 0.0625,
    "everbloom-fort-push": 0.0625,
    "everbloom-tyran-push": 0.0625,
    "galakrond-fort-push": 0.0625,
    "galakrond-tyran-push": 0.0625,
    "murozond-fort-push": 0.0625,
    "murozond-tyran-push": 0.0625,
    "tott-fort-push": 0.0625,
    "tott-tyran-push": 0.0625,
    "waycrest-fort-push": 0.0625,
    "waycrest-tyran-push": 0.0625,
}

weights_push_season_three = {
    "atal-fort-standard": 0.0625,
    "atal-tyran-standard": 0.0625,
    "brh-fort-standard": 0.0625,
    "brh-tyran-standard": 0.0625,
    "dht-fort-standard": 0.0625,
    "dht-tyran-standard": 0.0625,
    "everbloom-fort-standard": 0.0625,
    "everbloom-tyran-standard": 0.0625,
    "galakrond-fort-standard": 0.0625,
    "galakrond-tyran-standard": 0.0625,
    "murozond-fort-standard": 0.0625,
    "murozond-tyran-standard": 0.0625,
    "tott-fort-standard": 0.0625,
    "tott-tyran-standard": 0.0625,
    "waycrest-fort-standard": 0.0625,
    "waycrest-tyran-standard": 0.0625,
}

weights_standard_season_four = {
    "algethar-fort-standard": 0.06,
    "algethar-tyran-standard": 0.067,
    "azure-fort-standard": 0.056,
    "azure-tyran-standard": 0.063,
    "bhh-fort-standard": 0.041,
    "bhh-tyran-standard": 0.047,
    "hoi-fort-standard": 0.069,
    "hoi-tyran-standard": 0.075,
    "neltharus-fort-standard": 0.058,
    "neltharus-tyran-standard": 0.065,
    "nokhud-fort-standard": 0.066,
    "nokhud-tyran-standard": 0.071,
    "rlp-fort-standard": 0.067,
    "rlp-tyran-standard": 0.071,
    "ulda-fort-standard": 0.059,
    "ulda-tyran-standard": 0.065,
}

weights_push_season_four = {
    "algethar-fort-push": 0.06,
    "algethar-tyran-push": 0.067,
    "azure-fort-push": 0.056,
    "azure-tyran-push": 0.063,
    "bhh-fort-push": 0.041,
    "bhh-tyran-push": 0.047,
    "hoi-fort-push": 0.069,
    "hoi-tyran-push": 0.075,
    "neltharus-fort-push": 0.058,
    "neltharus-tyran-push": 0.065,
    "nokhud-fort-push": 0.066,
    "nokhud-tyran-push": 0.071,
    "rlp-fort-push": 0.067,
    "rlp-tyran-push": 0.071,
    "ulda-fort-push": 0.059,
    "ulda-tyran-push": 0.065,
}


def find_weights(key):
    """return the matching dict"""
    if key == 'weightsSingle':
        return weights_single
    if key == 'weightsTwoTargets':
        return weights_two_targets
    if key == 'weightsThreeTargets':
        return weights_three_targets
    if key == 'weightsFourTargets':
        return weights_four_targets
    if key == 'weightsSeasonOne':
        return weights_season_one
    if key == 'weightsStandardSeasonTwo':
        return weights_standard_season_two
    if key == 'weightsPushSeasonTwo':
        return weights_push_season_two
    if key == 'weightsStandardSeasonThree':
        return weights_standard_season_three
    if key == 'weightsPushSeasonThree':
        return weights_push_season_three
    if key == 'weightsNerubarPalace':
        return weights_nerubar_palace
    if key == 'weightsStandardSeasonFour':
        return weights_standard_season_four
    if key == 'weightsPushSeasonFour':
        return weights_push_season_four
    print(f"{key} not found")
    return None
