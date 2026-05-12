class Game:
    def __init__(self, name):
        self.name = name
        self.games = []

    def get_played_amount(self, player_name)-> int:
        """"/game/{name}/amount" - tagastab int-i, mis kirjeldab, mitu mängu nimega name on mängitud"""
        pass

    def get_favorite_games(self, game_name)-> int:
        """"/game/{name}/player-amount" - tagastab int-i, mis kirjeldab,
         mitme mängijaga mängu nimega game_name enim / kõige tihedamini mängitud on"""
        pass

    def get_most_wins_player(self, game_name)-> str:
        """"/game/{name}/most-wins" - tagastab mängija string,
        kellel on mängus nimega game_name enim võite (seda funktsiooni võidakse kutsuda ükskõik,
         mis tüüpi mängu korral)"""
        pass

    def get_most_frequent_winner(self, game_name)-> str:
        """"/game/{name}/most-frequent-winner" - tagastab mängija string, kelle võiduprotsent
         mängus nimega game_name on suurim (seda funktsiooni võidakse kutsuda ükskõik, mis tüüpi mängu korral)"""
        pass

    def get_most_losses(self, game_name)-> str:
        """"/game/{name}/most-losses" - tagastab mängija string, kellel on mängus nimega
        game_name enim kaotusi (viimasele kohale jäämisi)
         (seda funktsiooni kutsutakse vaid points või places mängu korral)"""
        pass

    def get_most_frequent_loser(self, game_name)-> str:
        """"/game/{name}/most-frequent-loser" - tagastab mängija string, kelle kaotuse protsent (protsent kordadest,
        kui mängija jäi viimasele kohale)
         mängus nimega game_name on suurim (seda funktsiooni kutsutakse vaid points või places mängu korral)"""
        pass

    def get_record_holder(self, game_name):
        """"/game/{name}/record-holder" - tagastab mängija (string),
        kes on mängus nimega game_name saanud enim punkte (ühe mängu jooksul), viigi korral tagastada see,
        kes selle tulemuse esimesena saavutas (seda funktsiooni kutsutakse vaid points mängu korral)"""
        pass