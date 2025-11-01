def generate_bmr_mif_sanj(height:int, weight:int,year:int, male:bool) -> float:
    if male: return 10*weight + 6.25*height - 5*year + 5
    return 10*weight + 6.25*height - 5*year - 161


def generate_bmr_har_ben(year:int, height:int, weight:int, male:bool) -> float:
    if male: return 66 + 13.7*weight + 5*height - 6.8*year
    return 655 + 9.6*weight + 1.8*height - 4.7*year