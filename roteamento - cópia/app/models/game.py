class Game:
    games_list = []
    id_counter = 1

    def __init__(self, title, genre, platform):
        self.id = Game.id_counter
        self.title = title
        self.genre = genre
        self.platform = platform
        Game.id_counter += 1

    @classmethod
    def list_all(cls):
        return cls.games_list
    
    @classmethod
    def add(cls, title, genre, platform):
        new_game = cls(title, genre, platform)
        cls.games_list.append(new_game)
        return new_game

Game.add("The Legend of Zelda", "Adventure", "Nintendo Switch")
Game.add("Elden Ring", "RPG", "PC/PS5/Xbox")