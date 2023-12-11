import re

max_balls = {
    'red': 12,
    'blue': 14,
    'green': 13
}

pattern = re.compile(r'(\d+\s\w+,\s\d+\s\w+,\s\d+\s\w+|\d+\s\w+,\s\d+\s\w+|\d+\s\w+)')


def valid_game(input_str):
    all_turns = pattern.findall(input_str)

    for turn in all_turns:
        all_balls = turn.split(', ')
        for ball in all_balls:
            [amount, color] = ball.split(' ')
            if max_balls[color] < int(amount):
                return False
    return True


# valid_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
# valid_game('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue')
# valid_game('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red')
# valid_game('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red')
# valid_game('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green')


answer = 0
idx = 1
with open('puzzle.txt', 'r') as file:
    for line in file:
        if valid_game(line):
            answer += idx
        idx += 1

print(answer)
