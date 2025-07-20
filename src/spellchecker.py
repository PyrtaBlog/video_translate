from pyaspeller import YandexSpeller

def check_spell(text):
    speller = YandexSpeller(lang="en")
    return speller.spelled(text)