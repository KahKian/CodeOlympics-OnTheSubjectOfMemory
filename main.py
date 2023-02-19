def get_pos_from_button(buttons, number):
    for pos in range(len(buttons)):
        if buttons[pos] == number:
            return pos

def get_button_from_position(pos, buttons):
    number = buttons[pos]
    return number

def get_button_array(sequence):
    buttons = sequence[0:4]
    return buttons

def get_prompt_from_sequence(sequence):
    prompt = sequence[4]
    return prompt

def findbutton(command, buttons, results_pos, results_number):
    if command in [11, 12]:
        return get_button_from_position(1, buttons)
    elif command in [13, 33]:
        return get_button_from_position(2, buttons)
    elif command in [14]:
        return get_button_from_position(3, buttons)
    elif command in [22, 34]:
        return 4
    elif command in [22, 24, 41, 51]:
        # stage 1 button pos
        pos = results_pos[0]
        return get_button_from_position(pos, buttons)
    elif command in [23, 42]:
        return get_button_from_position(0, buttons)
    elif command in [31]:
        return results_number[1]
    elif command in [32]:
        return results_number[0]
    elif command in [43, 44, 52]:
        # stage 2 button pos
        pos = results_pos[1]
        return get_button_from_position(pos, buttons)
    elif command in [53]:
        # stage 3 button pos
        pos = results_pos[2]
        return get_button_from_position(pos, buttons)
    elif command in [54]:
        # stage 4 button pos
        pos = results_pos[3]
        return get_button_from_position(pos, buttons)


input = [[1,3,2,4,1],
         [3,1,2,4,3],
         [2,3,4,1,2],
         [2,1,4,3,1],
         [4,1,2,3,4]]

# storage for previous results
results_pos = [0,0,0,0,0]
results_number = [0,0,0,0,0]
stage = 1
answer = ""

for sequence in input:
    buttons = get_button_array(sequence)
    command = str(stage)+str(get_prompt_from_sequence(sequence))
    number = findbutton(int(command), buttons, results_pos, results_number)
    # save results in array for future reference
    results_pos[stage-1] = get_pos_from_button(buttons, number)
    results_number[stage-1] = number
    # increment for next stage
    stage += 1
    answer += str(number)
print(answer)