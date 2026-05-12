class Player:
    def __init__(self, name):
        self.__name = name
        self.__games = []

    def get_played_game_count(self, player_name)-> int:
        """""/player/{name}/amount" - tagastab int-i, mis kirjeldab,
         mitu mängu on mängija nimega player_name mänginud"""
        return len(self.__games)

    def get_favorite_game(self, player_name)-> str:
        """"/player/{name}/favourite" - tagastab mängu (str, kus on mängu nimi),
         mida mängija nimega player_name on enim mänginud"""
        pass

    def get_amount_of_victory_games(self, player_name)-> int:
        """"/player/{name}/won" - tagastab int-i, mis kirjeldab, mitu mängu mängija nimega player_name on võitnud"""
        pass