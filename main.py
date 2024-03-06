from player import Player
from game import Game
from stats import Stats
from cheat import Cheat
from difficulty import Difficulty
from statsmanager import StatsManager
from human_player import HumanPlayer
import cmd

class CmdInterface(cmd.Cmd):
    prompt = '>> '
    intro = "Welcome to Pig Dice Game! Type 'help' for available commands."

    def __init__(self):
        super().__init__()
        self.stats_manager = StatsManager()
        self.player1 = None
        self.player2 = None
        self.game = None

    def do_play(self, arg):
        '""Start a new game""'
        if not self.player1:
            player1_name = input('Enter name for player 1: ')
            self.player1 = Player(player1_name)
        self.game_mode()
        
    def game_mode(self):
        print('\nChoose game mode')
        print('1. Play against computer')
        print('2. Play as 2 players')
        mode_choice = input('Enter your choice: ')

        if mode_choice == '1':
            self.play_against_computer()
        elif mode_choice == '2':
            self.play_as_two_players()
        else:
            print('\nInvalid choice! Choose again.')
            self.game_mode()

    def play_against_computer(self):
        """Play against computer"""
        player2_name = input('Enter name for computer: ')
        self.player2 = Player(player2_name)
        difficulty_level = input('Choose difficulty level (easy/hard): ').lower()
        while difficulty_level not in ['easy', 'hard']:
            print("Invalid difficulty level. Please choose 'easy' or 'hard'.")
            difficulty_level = input('Choose difficulty level (easy/hard): ').lower()
        self.player2.difficulty = Difficulty(difficulty_level)
        self.start_game()

    def play_as_two_players(self):
        """Play as 2 players"""
        player2_name = input('Enter name for player 2: ')
        self.player2 = HumanPlayer(player2_name)
        self.start_game()

    def start_game(self):
        """Start the game"""
        self.game = Game(self.player1, self.player2)
        while not self.game.current_game_over:
            self.game.play_game()
            self.stats_manager.update_stats(self.player1.name, self.player1.score)
            self.stats_manager.update_stats(self.player2.name, self.player2.score)
            self.player1.reset_score()
            self.player2.reset_score()
            if not self.game.current_game_over:
                restart = input('Do you want to restart the game? (yes/no): ').lower()
                if restart != 'yes':
                    break

    def do_scores(self, arg):
        '""View high scores""'
        print('\nHigh Scores:')
        high_scores = self.stats_manager.get_high_scores()
        for i, (name, data) in enumerate(high_scores):
            print(f"\n{i+1}. {name}: Score - {data['score']}, Games Played - {data['games_played']}")

    def do_rules(self, arg):
        '""View game rules""'
        print('\nRules:')
        print('The game of Pig is a simple 2-player dice game.')
        print('Each turn, a player rolls a six-sided dice.')
        print('If they roll a 1, their turn ends and they score no points for that turn.')
        print('If they roll any other numbeer, it is added to their turn total and they can choose to roll again or hold.')
        print('The first player to reach 100 points win.')

    def do_cheat(self, arg):
        '""Activate cheat for a player""'
        cheat_player = input('Enter name of player to activate cheat for: ')
        if cheat_player.lower() == self.player1.name.lower():
            cheat_player_name = Cheat.activate_cheat(self.player1)
            print(f'\nCheat activated for {cheat_player_name}.')
        elif self.player2 and cheat_player.lower() == self.player2.name.lower():
            cheat_player_name = Cheat.activate_cheat(self.player2)
            print(f'\nCheat activated for {cheat_player_name}.')
        else:
            print('\nPlayer not found!')

    def do_rename(self, arg):
        """Change player 1's name"""
        new_name = input('Enter new name for player 1: ')
        self.player1.name = new_name
        print(f'Player 1 changed name to: {self.player1.name}')

    def do_quit(self, arg):
        """Quit the game"""
        print('See you soon!')
        return True
    
def main():
    cmd_interface = CmdInterface()
    cmd_interface.cmdloop()

if __name__ == '__main__':
    main()