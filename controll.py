
import view, model

def start():
    st = view.input_data('task')
    string = model.digital(st)
    example = ''.join(string)
# print(string)
# print(example)

    while len(string)>1:
        if '*' in string or '/' in string:
            for i in range(len(string)):
                if model.operation(string, i, '*'): break
                if model.operation(string, i, '/'): break

        elif '+' in string or '-' in string:
            for i in range(len(string)):
                if model.operation(string, i, '+'): break
                if model.operation(string, i, '-'): break
    view.output_result({string[0]})
