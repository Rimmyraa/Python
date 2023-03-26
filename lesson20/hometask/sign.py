def Sign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print('Sign.pyc module started')
    print(Sign(-4))