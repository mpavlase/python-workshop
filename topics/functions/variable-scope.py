name = 'Tonda'

def get_name():
    print(f'{name} (inside)')
    name = 'Jolana'

print(f'{name} (before call)')
get_name()
print(f'{name} (after call)')
