from collections import defaultdict

def generate_faculty_timetable(class_tt):
    faculty_tt = defaultdict(lambda: defaultdict(list))

    for day, periods in class_tt.items():
        for period, info in periods.items():
            if info:
                faculty_tt[info["faculty"]][day].append(period)

    return faculty_tt
