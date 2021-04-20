class State:
    status = '...'

    def __str__(self):
        return str(self.status)


state = State()
for i in range(15):

    if i == 10:
        state.status = 'updated'

    a = 0

    print(f'State at index {i} {state}')
