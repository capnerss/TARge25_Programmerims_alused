class Statistic:
    def __init__(self, filename):
        self.filename = filename

    def get_stats(self, path: str):
        """/players - tagastab listi mängijate nimedest (nimede järjekord pole oluline)"""

        """"/games" - tagastab listi mängude nimedest (nimede järjekord pole oluline)"""

        """"/total" - tagastab int-i, mis kirjeldab, mitu mängu on mängitud"""

        """"/total/{result_type}" - kus {result_type} on string võimalike väärtustega points, places või winner, 
        funktsioon peab tagastama, mitu seda tüüpi mängu on mängitud"""
        pass