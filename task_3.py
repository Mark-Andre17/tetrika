tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564,
                        1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096,
                        1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500,
                        1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]


def appearance(intervals):
    all_time = 0
    start_less = intervals['lesson'][0]
    end_less = intervals['lesson'][1]
    less = {i for i in range(start_less, end_less)}
    pupil_set = set()
    pupil_time = intervals['pupil']
    for a in range(0, len(pupil_time) - 1, 2):
        temp_set = set(x for x in range(pupil_time[a], pupil_time[a + 1]))
        pupil_set = pupil_set | temp_set
    tutor_set = set()
    tutor_time = intervals['tutor']
    for b in range(0, len(tutor_time) - 1, 2):
        temp_set = set(x for x in range(tutor_time[b], tutor_time[b + 1]))
        tutor_set = tutor_set | temp_set
    all_set = pupil_set & less & tutor_set
    all_time += len(all_set)
    return all_time


if __name__ == '__main__':
    for i, test in enumerate(tests):
        print(appearance(test['data']))
