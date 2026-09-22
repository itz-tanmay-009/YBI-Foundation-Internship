def calculate_averages(df):
    """Calculate average values for important performance metrics."""

    return {
        "average_final": df["Final_Marks"].mean(),
        "average_study": df["Study_Hours"].mean(),
        "average_attendance": df["Attendance"].mean(),
        "average_assignment": df["Assignment_Score"].mean()
    }


def find_top_and_lowest_students(df):
    """Find the highest and lowest performing students."""

    highest_student = df.loc[df["Final_Marks"].idxmax()]
    lowest_student = df.loc[df["Final_Marks"].idxmin()]

    return highest_student, lowest_student


def performance_category(marks):
    """Classify a student based on final marks."""

    if marks >= 85:
        return "Excellent"
    elif marks >= 70:
        return "Good"
    else:
        return "Needs Improvement"


def add_performance_category(df):
    """Add performance category to the DataFrame."""

    df["Performance_Category"] = df["Final_Marks"].apply(
        performance_category
    )

    return df


def calculate_category_statistics(df):
    """Calculate category counts and percentages."""

    category_counts = df["Performance_Category"].value_counts()

    category_percentages = (
        df["Performance_Category"]
        .value_counts(normalize=True) * 100
    )

    return category_counts, category_percentages


def calculate_correlation(df):
    """Calculate correlation with final marks."""

    columns = [
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Previous_Marks",
        "Final_Marks"
    ]

    return df[columns].corr()["Final_Marks"]


def determine_class_performance(average_final):
    """Determine the overall class performance level."""

    if average_final >= 85:
        return "Excellent"
    elif average_final >= 70:
        return "Good"
    else:
        return "Needs Improvement"