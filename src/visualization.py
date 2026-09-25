import matplotlib.pyplot as plt


def plot_relationship(df, x_column, x_label, title):
    """Create a scatter plot between an academic factor and final marks."""
    plt.figure(figsize=(8, 5))
    plt.scatter(df[x_column], df["Final_Marks"])
    plt.xlabel(x_label)
    plt.ylabel("Final Marks")
    plt.title(title)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_study_hours_vs_marks(df):
    """Plot study hours against final marks."""
    plot_relationship(
        df,
        "Study_Hours",
        "Study Hours",
        "Study Hours vs Final Marks"
    )


def plot_attendance_vs_marks(df):
    """Plot attendance against final marks."""
    plot_relationship(
        df,
        "Attendance",
        "Attendance (%)",
        "Attendance vs Final Marks"
    )


def plot_assignment_vs_marks(df):
    """Plot assignment score against final marks."""
    plot_relationship(
        df,
        "Assignment_Score",
        "Assignment Score",
        "Assignment Score vs Final Marks"
    )


def create_all_visualizations(df):
    """Generate all student performance visualizations."""
    plot_study_hours_vs_marks(df)
    plot_attendance_vs_marks(df)
    plot_assignment_vs_marks(df)