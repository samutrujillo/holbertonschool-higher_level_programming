#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for allNames in dir(hidden_4):
        if not allNames.startswith('__'):
            print("{}".format(allNames))
