def task(array):
    for k, v in enumerate(array):
        if v == '0':
            return k


def task_1(array):
    return array.index('0')


if __name__ == '__main__':
    print(task('1111111111111111100000000000000000000'))
    print(task_1('1111111111111111100000000000000000000'))
