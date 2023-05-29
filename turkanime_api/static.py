from enum import Enum
class Degerler(str, Enum):
    HEAD = "TurkAnime"
    MANUEL_FANSUB = "manuel_fansub"
    IZLERKEN_KAYDET = "izlerken_kaydet"
    INDIRILEN_DIR = "indirilenler"
    IZLENDI_IKON = "izlendi_ikonu"
    INDIRME_SAYISI = "paralel_indirme_sayisi"
    FIREFOX_KONUMU = "firefox_konumu"
    KEY = "key"
    def __str__(self) -> str:
        return self.value