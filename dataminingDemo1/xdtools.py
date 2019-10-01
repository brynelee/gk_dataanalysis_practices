def print_line(char,times):

    print(char * times)

def print_one_line():
    print_line('*', 50)

def print_lines():

    row = 0

    while row < 5:

        print_line("*",50)

        row += 1

print_lines()
