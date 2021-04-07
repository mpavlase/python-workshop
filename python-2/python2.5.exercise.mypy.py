def decorate_print(msg):
    print('<🐍>', end='')
    print(msg, end='')
    print('</🐍>')


def describe_function(fn):
    return 'Passed function looks like this: ' + str(fn)


def print_table1(table):
    print('print_table:')
    for row in table:
        grams = row[1] * 1000
        line = f'Weight of {row[0]} is {row[1]}kg ({int(grams)}g)'
        print(line)


def print_table2(table):
    print('print_dict_table:')
    for name, weight in table.items():
        grams = weight * 1000
        line = f'Weight of {name} is {weight}kg ({int(grams)}g)'
        print(line)


decorate_print('python code')

# `str` is a data type, but actually also a function
print(describe_function(str))

table1 = [
    ('pasta', 0.5),
    ('egg size S', 0.05),
    ('indian runner duck', 1.8)
]
print_table1(table1)

table2 = {
    'pasta': 0.5,
    'egg size S': 0.05,
    'indian runner duck': 1.8,
}
print_table2(table2)
