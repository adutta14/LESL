import json

labels = {}
execution = False
values = {}
all_tokens = {}

def print_error(err, row):
    # print row, ' : ', err
    print err
    exit(0)

def initial_check(rows):
    global labels
    global execution
    for index, row in enumerate(rows):
        row = row.strip()
        if 'shw' in row:
            execution = True

        if ':' in row:
            newlabels = row.split(':')
            newlabels = newlabels[:-1]
            for label in newlabels:
                label = label.strip()
                labels[label] = index

def find_elements(row):
    elements = row.split(' ', 1)[1]
    elements = elements.strip()
    tokens = elements.split(',')
    tokens = map(lambda x: x.strip(), tokens)
    return tokens

def find_labels(label):
    if label in list(labels.keys()):
        line = labels[label]
        return line
    else:
        return False

def move(row):
    global values
    global all_tokens

    tokens = find_elements(row)

    source = tokens[0]
    destination = tokens[1]

    if source == 'T' or source == 'F':
        values[destination] = source
        return None

    try:
        source = int(source)
        values[destination] = str(source)
        return None
    except:
        if source in list(values.keys()):
            values[destination] = values[source]
        else:
            if source in list(all_tokens.keys()):
                error = 'Variable ' + all_tokens[source] + ' not defined'
            else:
                error = 'Variable ' + source + ' not defined'
            print_error(error, row)
        return None

def division_sanity_check(source):
    source = eval(str(source))
    if source == 0:
        return False
    return True

def arithmetic(row, string, sign):
    global values
    global all_tokens

    tokens = find_elements(row)
    try:
        source = tokens[0]
        destination = tokens[1]
        storage = tokens[2]

        if source == 'T' or source == 'F':
            error = 'Cannot ' + string + ' binary variable to Register'
            print_error(error, row)
            return None

        elif destination == 'T' or destination == 'F':
            error = 'Cannot ' + string + ' binary variable to Register'
            print_error(error, row)
            return None

        else:
            try:
                source = int(source)
            except:
                if source in list(values.keys()):
                    source = values[source]
                else:
                    if source in list(all_tokens.keys()):
                        error = 'Variable ' + all_tokens[source] + ' is not defined'
                    else:
                        error = 'Variable ' + source + ' is not defined'
                    print_error(error, row)
                    return None

            try:
                destination = int(destination)
            except:
                if destination in list(values.keys()):
                    destination = values[destination]
                else:
                    if destination in list(all_tokens.keys()):
                        error = 'Variable ' + all_tokens[destination] + ' is not defined'
                    else:
                        error = 'Variable ' + destination + ' is not defined'
                    print_error(error, row)
                    return None

            if source == 'T' or source == 'F':
                error = 'Cannot ' + string + ' binary variable to Register'
                print_error(error, row)
                return None

            elif destination == 'T' or destination == 'F':
                error = 'Cannot ' + string + ' binary variable to Register'
                print_error(error, row)
                return None

            if string == 'div':
                flag = division_sanity_check(destination)
                if not flag:
                    error = 'Cannot divide by zero'
                    print_error(error, row)
                    return None

            new_value = '(' + str(source) + ')' + sign + '(' + str(destination) + ')'

            values[storage] = new_value
            return None

    except Exception as e:
        print_error(e, row)

def addition(row):
    arithmetic(row, 'add', '+')

def subtraction(row):
    arithmetic(row, 'sub', '-')

def multiplication(row):
    arithmetic(row, 'mul', '*')

def division(row):
    arithmetic(row, 'div', '/')

def modulus(row):
    arithmetic(row, 'mod', '%')

def jump(row):
    global labels
    tokens = find_elements(row)
    if len(tokens) > 1:
        error = 'Invalid jump command'
        print_error(error, row)

    label = tokens[0]
    line = find_labels(label)
    if line == False:
        error = 'Label ' + label + ' not found'
        print_error(error, row)
        return None
    else:
        return line

def conditional(row, sign):
    global labels
    global all_tokens

    tokens = find_elements(row)
    label = tokens[2]

    line = find_labels(label)

    if line == False:
        error = 'Label ' + label + ' not found'
        print_error(error, row)

    else:
        source = tokens[0]
        destination = tokens[1]

        if source == 'T' or source == 'F':
            error = 'Cannot compare with binary values'
            print_error(error, row)
            return None

        if destination == 'T' or destination == 'F':
            error = 'Cannot compare with binary values'
            print_error(error, row)
            return None

        try:
            source = int(source)
        except:
            if source in list(values.keys()):
                source_value = values[source]
                source_value = eval(str(source_value))
                values[source] = str(source_value)
                source = source_value
            else:
                if source in list(all_tokens.keys()):
                    error = 'Variable ' + all_tokens[source] + ' is not defined'
                else:
                    error = 'Variable ' + source + ' is not defined'
                print_error(error, row)
                return None

        try:
            destination = int(destination)
        except:
            if destination in list(values.keys()):
                destination_value = values[destination]
                destination_value = eval(str(destination_value))
                values[destination] = str(destination_value)
                destination = destination_value
            else:
                if destination in list(all_tokens.keys()):
                    error = 'Variable ' + all_tokens[destination] + ' is not defined'
                else:
                    error = 'Variable ' + destination + ' is not defined'

                print_error(error, row)
                return None

        expression = str(source) + sign + str(destination)
        # print expression, eval(expression), line
        if eval(str( expression)):
            return line
        else:
            return None

def jump_less_than_equal(row):
    counter = conditional(row, '<=')
    return counter

def jump_less_than(row):
    counter = conditional(row, '<')
    return counter

def jump_greater_than(row):
    counter = conditional(row, '>')
    return counter

def jump_greater_than_equal(row):
    counter = conditional(row, '>=')
    return counter

def jump_not_equal(row):
    counter = conditional(row, '!=')
    return counter

def jump_equal(row):
    global labels
    global all_tokens

    tokens = find_elements(row)
    label = tokens[2]

    line = find_labels(label)

    if line == False:
        error = 'Label ' + label + ' not found'
        print_error(error, row)

    else:
        source = tokens[0]
        destination = tokens[1]

        if source == 'T' or source == 'F':

            if destination == 'T' or destination == 'F':
                destination = values[destination]
            else:
                if destination in list(values.keys()):
                    destination = values[destination]
                    if source == destination:
                        return line
                    else:
                        return None
                else:
                    if destination in list(all_tokens.keys()):
                        error = 'Variable ' + all_tokens[destination] + ' is not defined'
                    else:
                        error = 'Variable ' + destination + ' is not defined'

                    print_error(error, row)

        elif destination == 'T' or destination == 'F':
            if source in list(values.keys()):
                source = values[source]
                if source == destination:
                    return line
                else:
                    return None

        else:
            counter = conditional(row, '==')
            return counter


def show(row):
    global tokens
    tokens = find_elements(row)

    variable = tokens[0]
    token = variable
    if variable in list(values.keys()):
        variable = values[variable]
        if variable == 'T':
            answer = 'True'
        elif variable == 'F':
            answer = 'False'
        else:
            answer = eval(str(variable))

        global all_tokens
        print 'value of ' + all_tokens[token] + ' is ', answer
        values[token] = answer

    else:
        error = 'Variable ' + variable + ' not defined'
        print_error(error, row)

    return None

def execute_statement(row):
    statements = {
        'mov' : move,
        'add' : addition,
        'sub' : subtraction,
        'mul' : multiplication,
        'div' : division,
        'mod' : modulus,
        'jmp' : jump,
        'jle' : jump_less_than_equal,
        'jl' : jump_less_than,
        'jg' : jump_greater_than,
        'jge' : jump_greater_than_equal,
        'jne' : jump_not_equal,
        'je' : jump_equal,
        'shw' : show
    }

    if ':' in row:
        row = row.split(':')[-1]

    row = row.strip()
    if row == '':
        return None

    tokens = row.split(' ', 1)
    # print 'tokens', tokens
    program_counter = statements[tokens[0]](row)
    return program_counter
    # print program_counter

def main():
    #Opening the file containing intermediate code
    global labels
    global execution
    global all_tokens

    try:
        file = open("intermediate.ic", "r")
    except IOError as e:
        print 'File could not be found'
        return
    except Exception as e:
        print 'Error in opening the file'
        return

    #Opening a tokens file
    try:
        tokensfile = open("tokens.json", "r")
    except IOError as e:
        print 'File could not be found'
        return
    except Exception as e:
        print 'Error in opening the file'
        return

    all_tokens = json.load(tokensfile)

    rows = file.readlines()
    # rows = ['mov 2, t1', 'add 3, t1, t1', 'sub t1, 1, t1', 'sub t1, 4, t1', 'div 4, t1, t1', 'shw t1']
    initial_check(rows)


    if execution:
        program_counter = 0

        while(program_counter < len(rows)):
            # print rows[program_counter  ]
            counter = execute_statement(rows[program_counter])
            if counter:
                program_counter = counter
            else:
                program_counter += 1

if __name__ == '__main__':
	main()