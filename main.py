
f = open("program.b", "r")
program = f.read()
f.close()

array = []
for i in range(30000):
    array.append(int(0))

instruction_pointer = int(0)
data_pointer = int(0)

def matching_square(pointer, forward):
    nested_parentheses = 0
    while True:
        if forward:
            pointer += 1
            if program[pointer] == "[":
                nested_parentheses += 1
            elif program[pointer] == "]":
                if nested_parentheses > 0:
                    nested_parentheses -= 1
                else:
                    return pointer
        else:
            pointer -= 1
            if program[pointer] == "]":
                nested_parentheses += 1
            elif program[pointer] == "[":
                if nested_parentheses > 0:
                    nested_parentheses -= 1
                else:
                    return pointer

while instruction_pointer < len(program):
    match program[instruction_pointer]:
        case ">":
            data_pointer += 1
            instruction_pointer += 1
        case "<":
            data_pointer -= 1
            instruction_pointer += 1
        case "+":
            array[data_pointer] += 1
            instruction_pointer += 1
        case "-":
            array[data_pointer] -= 1
            instruction_pointer += 1
        case ".":
            print(chr(array[data_pointer]), end="")
            instruction_pointer += 1
        case ",":
            array[data_pointer] = int(input())
            instruction_pointer += 1
        case "[":
            if array[data_pointer] == 0:
                instruction_pointer = matching_square(instruction_pointer, True) + 1
            else:
                instruction_pointer += 1
        case "]":
            if array[data_pointer] != 0:
                instruction_pointer = matching_square(instruction_pointer, False) + 1
            else:
                instruction_pointer += 1
        case _:
            instruction_pointer += 1