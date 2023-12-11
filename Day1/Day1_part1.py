def create_number(inp: str) -> int:
    result_str = ''
    for c in inp:
        if c.isnumeric():
            result_str += c
            break
    for c in inp[::-1]:
        if c.isnumeric():
            result_str += c
            break
    result = int(result_str)
    return result


answer = 0
with open('Day1_part1.txt', 'r') as file:
    for line in file:
        answer += create_number(line)

print(answer)
