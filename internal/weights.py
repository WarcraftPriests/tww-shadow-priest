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
    'pw_ba_8': 0.000,
    'pw_sa_8': 0.000,
    'pw_na_8': 0.000,
    'lm_ba_8': 0.000,
    'lm_sa_8': 0.000,
    'lm_na_8': 0.000,
    'hm_ba_8': 0.000,
    'hm_sa_8': 0.000,
    'hm_na_8': 0.000,
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

weights_eight_targets = {
    'pw_ba_8': 0.0,
    'pw_sa_8': 0.0,
    'pw_na_8': 0.8,
    'lm_ba_8': 0.0,
    'lm_sa_8': 0.0,
    'lm_na_8': 0.2,
    'hm_ba_8': 0.0,
    'hm_sa_8': 0.0,
    'hm_na_8': 0.0,
}

weights_season_one = {
    "arakara": 0.125,
    "cityofthreads": 0.125,
    "dawnbreaker": 0.125,
    "grimbatol": 0.125,
    "mists": 0.125,
    "necrotic": 0.125,
    "siege": 0.125,
    "stonevault": 0.125,
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
    if key == 'weightsEightTargets':
        return weights_eight_targets
    if key == 'weightsSeasonOne':
        return weights_season_one
    if key == 'weightsNerubarPalace':
        return weights_nerubar_palace
    print(f"{key} not found")
    return None
