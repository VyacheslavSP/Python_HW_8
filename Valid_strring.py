OPERATOR = ['+', '-', '*', '/', '^']
# приоритетность задана через индес строчки с элементом в списке
operator_priority = [['('], ['+', '-'], ['*', '/'], ['^']]


def to_valid_string(input_string):
    valid_string = ''
    stack_char = []
    for char in input_string:
        try:
            int_char = int(char)
            if (0 <= int_char <= 9):
                valid_string += (str(int_char)+' ')
        except:
            if (char == '('):
                stack_char.append(char)
            elif (char == ')'):
                for stack_element in stack_char:
                    if (stack_element != '('):
                        valid_string += stack_element
                    else:
                        stack_char.pop(stack_char.index('('))
            elif (char in OPERATOR):
                #    while (len(stack_char) != 0):
                count = 0
                for count in range(len(stack_char)):
                   # for element_of_stack in stack_char:
                    for i in operator_priority:
                        for j in i:
                            if (char == j):
                                idex_priority = operator_priority.index(i)
                            elif len(stack_char) > 0:
                                if (stack_char[0] == j):
                                    Index_stack_element = operator_priority.index(
                                        i)
                    if (Index_stack_element >= idex_priority):
                        valid_string += str(stack_char.pop()) + ' '
                stack_char.append(char)
               # stack_char.pop(0)
    for stack_element in stack_char:
        valid_string += str(stack_element)

    return valid_string


print(to_valid_string("6/2+1*5-7"))
