import re

pattern = re.compile(r'(\d+\s\w+,\s\d+\s\w+,\s\d+\s\w+|\d+\s\w+,\s\d+\s\w+|\d+\s\w+)')


def get_max_balls(input_str):
    all_turns = pattern.findall(input_str)

    max_balls = [0, 0, 0]

    for turn in all_turns:
        all_balls = turn.split(', ')
        for ball in all_balls:
            [amount_in_str, color] = ball.split(' ')
            amount = int(amount_in_str)
            if color == 'red' and max_balls[0] < amount:
                max_balls[0] = amount
            elif color == 'blue' and max_balls[1] < amount:
                max_balls[1] = amount
            elif color == 'green' and max_balls[2] < amount:
                max_balls[2] = amount

    print(max_balls)
    return max_balls


# valid_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
# valid_game('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue')
# valid_game('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red')
# valid_game('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red')
# valid_game('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green')


answer = 0
with open('puzzle.txt', 'r') as file:
    for line in file:
        max_balls = get_max_balls(line)
        answer += (max_balls[0] * max_balls[1] * max_balls[2])


print(answer)
