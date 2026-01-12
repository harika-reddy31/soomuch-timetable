from collections import defaultdict
import random
from data import DAYS, PERIODS, SUBJECTS, faculty_availability


def generate_timetable():
    timetable = {day: {p: None for p in PERIODS} for day in DAYS}
    faculty_busy = defaultdict(lambda: defaultdict(set))
    subject_day_count = defaultdict(lambda: defaultdict(int))

    priority_order = {"HIGH": 1, "MEDIUM": 2, "LOW": 3}
    sorted_subjects = sorted(SUBJECTS, key=lambda x: priority_order[x["priority"]])


    for subject in sorted_subjects:
        assigned = 0
        while assigned < subject["weekly"]:
            day = random.choice(DAYS)
            period = random.choice(PERIODS)
            faculty = subject["faculty"]

            if timetable[day][period]:
                continue
            if period not in faculty_availability[faculty][day]:
                continue
            if period in faculty_busy[faculty][day]:
                continue
            if subject["priority"] != "HIGH" and subject_day_count[subject["name"]][day] >= 1:
                continue

            timetable[day][period] = {
                "subject": subject["name"],
                "faculty": faculty
            }
            faculty_busy[faculty][day].add(period)
            subject_day_count[subject["name"]][day] += 1
            assigned += 1

    return timetable
