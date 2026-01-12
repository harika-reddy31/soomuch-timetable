from flask import Flask, render_template, request, redirect, url_for, abort
from generator import generate_timetable
from faculty_view import generate_faculty_timetable
from data import CLASSES, FACULTY, SUBJECTS

app = Flask(__name__)

# -----------------------------
# In-memory storage (demo)
# -----------------------------
CLASS_TIMETABLES = {}

# -----------------------------
# Helpers
# -----------------------------
def get_timetable(class_name):
    """
    Generate timetable once per class (auto-generated first)
    """
    if class_name not in CLASS_TIMETABLES:
        CLASS_TIMETABLES[class_name] = generate_timetable()
    return CLASS_TIMETABLES[class_name]


def has_faculty_collision(current_class, day, period, faculty):
    """
    Prevent a faculty from being assigned to two classes
    at the same day + period
    """
    for cls, timetable in CLASS_TIMETABLES.items():
        if cls == current_class:
            continue
        slot = timetable.get(day, {}).get(period)
        if slot and slot["faculty"] == faculty:
            return True
    return False

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    selected_class = request.args.get("class_name", "Class 5")
    class_tt = get_timetable(selected_class)
    faculty_tt = generate_faculty_timetable(class_tt)

    return render_template(
        "timetable.html",
        class_tt=class_tt,
        faculty_tt=faculty_tt,
        classes=CLASSES,
        subjects=[s["name"] for s in SUBJECTS],
        faculty=FACULTY,
        selected_class=selected_class,
        mode="view"
    )


@app.route("/edit")
def edit():
    selected_class = request.args.get("class_name", "Class 5")
    class_tt = get_timetable(selected_class)
    faculty_tt = generate_faculty_timetable(class_tt)

    return render_template(
        "timetable.html",
        class_tt=class_tt,
        faculty_tt=faculty_tt,
        classes=CLASSES,
        subjects=[s["name"] for s in SUBJECTS],
        faculty=FACULTY,
        selected_class=selected_class,
        mode="edit"
    )


@app.route("/update", methods=["POST"])
def update():
    class_name = request.form["class_name"]
    day = request.form["day"]
    period = int(request.form["period"])
    subject = request.form["subject"]
    faculty = request.form["faculty"]

    # -----------------------------
    # Collision validation
    # -----------------------------
    if has_faculty_collision(class_name, day, period, faculty):
        abort(400, description="Collision detected: Faculty already assigned at this time")

    # -----------------------------
    # Update timetable
    # -----------------------------
    CLASS_TIMETABLES[class_name][day][period] = {
        "subject": subject,
        "faculty": faculty
    }

    return redirect(url_for("edit", class_name=class_name))


# -----------------------------
# App runner
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


