import pandas as pd


def create_student_dataset():
    """Create and return the student performance dataset."""

    data = {
        "Student_ID": range(1, 21),
        "Study_Hours": [
            2, 5, 3, 7, 4, 6, 1, 8, 5, 3,
            7, 2, 6, 4, 9, 3, 5, 8, 2, 6
        ],
        "Attendance": [
            65, 85, 72, 95, 80, 88, 60, 97, 82, 70,
            92, 68, 90, 78, 98, 75, 84, 94, 63, 87
        ],
        "Assignment_Score": [
            55, 82, 68, 91, 76, 85, 48, 94, 80, 65,
            89, 58, 86, 73, 96, 70, 81, 92, 52, 84
        ],
        "Previous_Marks": [
            50, 78, 65, 88, 72, 82, 45, 91, 76, 60,
            85, 54, 80, 70, 94, 66, 79, 89, 48, 81
        ],
        "Final_Marks": [
            52, 80, 67, 92, 75, 86, 47, 95, 81, 64,
            90, 57, 84, 74, 97, 69, 82, 93, 50, 85
        ]
    }

    return pd.DataFrame(data)