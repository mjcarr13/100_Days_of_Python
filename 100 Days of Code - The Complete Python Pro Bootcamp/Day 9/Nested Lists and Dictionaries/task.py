student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    score = student_scores[name]

    if 91 <= score <= 100:
        student_grades[name] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[name] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"