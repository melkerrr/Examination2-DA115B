from player import Player
from game import Game
from stats import Stats
from cheat import Cheat
from difficulty import Difficulty
from statsmanager import StatsManager

def main():
    print('Welcome to Pig Dice Game!')

    stats_manager = StatsManager()
    player1_name = input('Enter name for player 1: ')
    player1 = Player(player1_name)
    
    while True:
        print('\n1. Play Game')
        print('2. View High Scores')
        print('3. Rules')
        print('4. Cheat')
        print('5. Change player names')
        print('6. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            player2_name = input('Enter name for player 2 (or press Enter to play vs computer): ')
            if player2_name:
                player2 = Player(player2_name)
            else:
                player2 = Player('Computer')
                difficulty_level = input('Choose difficulty level (easy/hard): ').lower()
                while difficulty_level not in ['easy', 'hard']:
                    print("Difficulty level invalid. Please choose 'easy' or 'hard'.")
                    difficulty_level = input('Choose difficulty level (easy/hard): ').lower()
                player2.difficulty = Difficulty(difficulty_level)

            game = Game(player1, player2)
            while not game.current_game_over:
                game.play_game()
                stats_manager.update_stats(player1.name, player1.score)
                stats_manager.update_stats(player2.name, player2.score)
                player1.reset_score()
                player2.reset_score()
                if not game.current_game_over:
                    restart = input('Do you want to restart the game? (yes/no): ').lower()
                    if restart != 'yes':
                        break
        elif choice == '2':
            print('\nHigh Scores:')
            high_scores = stats_manager.get_high_scores()
            for i, (name, data) in enumerate(high_scores):
                print(f"\n{i+1}. {name}: Score - {data['score']}, Games Played - {data['games_played']}")
        elif choice == '3':
            print('\nRules:')
            print('The game of Pig is a simple two-player dice game.')
            print('Each turn, a player rolls a six-sided dice.')
            print('If they roll a 1, their turn ends and they score no points for that turn.')
            print('If they roll any other number, it is added to their turn total and they can choose to roll again or hold.')
            print('The first player to reach 100 points win.')
        elif choice == '4':
            cheat_player = input('Enter name of player to activate cheat for: ')
            if cheat_player.lower() == player1.name.lower():
                cheat_player_name = Cheat.activate_cheat(player1)
                print(f'\nCheat activated for {cheat_player_name}.')
            elif player2 and cheat_player.lower() == player2.name.lower():
                cheat_player_name = Cheat.activate_cheat(player2)
                print(f'\nCheat activated for {cheat_player_name}.')
            else:
                print('\nPlayer not found!')
        elif choice == '5':
            new_name = input('Enter new name for player 1: ')
            player1.name = new_name
            print(f'Player 1 changed name to: {player1.name}')
        elif choice == '6':
            print('See you soon!')
            break
        else:
            print('Not a valid choice! Please choose again.')

if __name__ == '__main__':
    main()