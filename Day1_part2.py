hm = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def find_first_number(sentence: str):
    first_num_word = None
    first_num_word_idx = None

    for num_word in hm.keys():
        if num_word in sentence:
            if not first_num_word:
                first_num_word = num_word
                first_num_word_idx = sentence.find(num_word)
            elif sentence.find(num_word) > first_num_word_idx:
                continue
            else:
                first_num_word = num_word
                first_num_word_idx = sentence.find(num_word)
            # print(sentence, " : ", num_word, " : ", sentence.find(num_word))

    # print(sentence, ":", first_num_word, ":", first_num_word_idx)

    first_num = None
    first_num_idx = None
    for idx, letter in enumerate(sentence):
        if letter.isnumeric():
            first_num = letter
            first_num_idx = idx
            break
    # print(sentence, " : ", first_num, ":", first_num_idx)

    final_first_num = None
    if first_num_word and first_num:
        if first_num_word_idx < first_num_idx:
            final_first_num = hm[first_num_word]
        else:
            final_first_num = first_num
    elif first_num_word and not first_num:
        final_first_num = hm[first_num_word]
    else:
        final_first_num = first_num

    # print(sentence, "final_first_num :", final_first_num)
    return final_first_num


def find_last_number(sentence: str):
    last_num_word = None
    last_num_word_idx = None

    for num_word in hm.keys():
        if num_word in sentence:
            if not last_num_word:
                last_num_word = num_word
                last_num_word_idx = sentence.rfind(num_word)
            elif sentence.rfind(num_word) < last_num_word_idx:
                continue
            else:
                last_num_word = num_word
                last_num_word_idx = sentence.rfind(num_word)
            # print(sentence, " : ", num_word, " : ", sentence.find(num_word))

    # print(sentence, ":", last_num_word, ":", last_num_word_idx)

    last_num = None
    last_num_idx = None
    for idx, letter in enumerate(reversed(sentence)):
        if letter.isnumeric():
            last_num = letter
            last_num_idx = len(sentence) - 1 - idx
            # last_num_idx = idx
            break
    # print(sentence, " : ", last_num, ":", last_num_idx)

    final_last_num = None
    if last_num_word and last_num:
        if last_num_word_idx > last_num_idx:
            final_last_num = hm[last_num_word]
        else:
            final_last_num = last_num
    elif last_num_word and not last_num:
        final_last_num = hm[last_num_word]
    else:
        final_last_num = last_num

    # print(sentence, "final_last_num :", final_last_num)
    return final_last_num


# find_first_number('two1nine')
# find_first_number('eightwothree')
# find_first_number('abcone2threexyz')
# find_first_number('xtwone3four')
# find_first_number('4nineeightseven2')
# find_first_number('zoneight234')
# find_first_number('7pqrstsixteen')

# find_last_number('two1nine')
# find_last_number('eightwothree')
# find_last_number('abcone2threexyz')
# find_last_number('xtwone3four')
# find_last_number('4nineeightseven2')
# find_last_number('zoneight234')
# find_last_number('7pqrstsixteen')
# find_last_number('sixthree8sixjxjqsjgjgp')


answer = 0
with open('Day1_part1.txt', 'r') as file:
    for line in file:
        first_num_char = find_first_number(line)
        last_num_char = find_last_number(line)
        num = int((first_num_char + last_num_char))
        print(num)
        answer += num

print(answer)
