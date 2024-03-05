from player import Player
from game import Game
from stats import Stats

def main():
    print('Welcome to Pig Dice Game!')

    player1_name = input('Enter name for player 1: ')
    player1 = Player(player1_name)

    player2_name = input('Enter name for player 2 (or press Enter to play vs computer): ')
    if player2_name:
        player2 = Player(player2_name)
    else:
        player2 = None

    game = Game(player1, player2)
    stats = Stats()

    while True:
        print('\n1. Play Game')
        print('2. View High Scores')
        print('3. Rules')
        print('4. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            game.play_game()
            print('\nGame Over!')
            print(f'\n{player1.name}: {player1.score}')
            if player2:
                print(f'{player2.name}: {player2.score}')
            if player1.score > player2.score:
                winner = player1.name
            elif player2.score > player1.score:
                winner = player2.name if player2 else 'Computer'
            else:
                winner = "It's a draw!"
            print(f'Winner: {winner}')
            stats.update_stats(player1.name, player1.score)
            if player2:
                stats.update_stats(player2.name, player2.score)
            player1.reset_score()
            if player2:
                player2.reset_score()
        elif choice == '2':
            print('\nHigh Scores:')
            high_scores = stats.get_high_scores()
            for i, (name, data) in enumerate(high_scores):
                print(f"\n{i+1}. {name}: Score - {data['score']}, Games Played - {data['games_played']}")
        elif choice == '3':
            print('\nRules:')
            print('The game of Pig is a simple two-player dice game.')
            print('Each turn, a player rolls a six-sided dice.')
            print('If they roll a 1, their turn ends and they score no points for that turn.')
            print('If they roll any other number, it is added to their turn total and they can choose to roll again or hold.')
            print('The first player to reach 100 points win.')
        elif choice =='4':
            print('See you soon!')
            break
        else:
            print('Not a valid choice! Please choose again.')

if __name__ == '__main__':
    main()