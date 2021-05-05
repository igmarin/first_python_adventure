players = []


def player_generate():
    name = input('Player name: ')
    goals = int(input(
        'Goals of {}: '.format(name)))
    games = int(input(
        '# of games for {}: '.format(name)))

    players.append({'name': name, 'goals': goals, 'games': games})


def print_players_stats(player):
    return print('{} has ({}) goals in {} game\n'.format(
        player['name'], player['goals'], player['games']))


def calculate_goal_avg(goals, games):
    return round((goals / games), 2)


print("Welcome to the goal average calculator\n")
how_many_players = int(input("how many players are we goint to compare? "))

for player in range(how_many_players):
    player_generate()

print("Basic information:\n")

for player in players:
    print_players_stats(player)
