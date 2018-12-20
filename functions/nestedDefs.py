def outer(param):
    state=0
    def nested(num):
        nonlocal state
        print('this is state ', num**state)
        state+=1
    return nested

new=outer(0)
new(3)
new(3)
new(4)
input('enter to exit')
