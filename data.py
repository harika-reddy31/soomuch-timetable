DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
PERIODS = [1, 2, 3, 4, 5, 6]

CLASSES = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5"]

FACULTY = ["Bhargavi", "Lokesh", "Pavan", "Reddy"]

SUBJECTS = [
    {"name": "Math", "faculty": "Bhargavi", "priority": "HIGH", "weekly": 6},
    {"name": "English", "faculty": "Lokesh", "priority": "HIGH", "weekly": 5},
    {"name": "Science", "faculty": "Pavan", "priority": "HIGH", "weekly": 5},
    {"name": "Social", "faculty": "Reddy", "priority": "MEDIUM", "weekly": 4},
    {"name": "Computer", "faculty": "Lokesh", "priority": "LOW", "weekly": 2},
    {"name": "PE", "faculty": "Reddy", "priority": "LOW", "weekly": 2},
]
faculty_availability = {
    "Bhargavi": {d: PERIODS for d in DAYS},
    "Lokesh":   {d: PERIODS for d in DAYS},
    "Pavan":    {d: [2,3,4,5,6] for d in DAYS},
    "Reddy":    {d: [1,2,3,4,5] for d in DAYS},
}

