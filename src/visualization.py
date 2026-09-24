import matplotlib.pyplot as plt


def plot_study_hours_vs_marks(df):
    """Plot the relationship between study hours and final marks."""
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Study_Hours"], df["Final_Marks"])
    plt.xlabel("Study Hours")
    plt.ylabel("Final Marks")
    plt.title("Study Hours vs Final Marks")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_attendance_vs_marks(df):
    """Plot the relationship between attendance and final marks."""
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Attendance"], df["Final_Marks"])
    plt.xlabel("Attendance (%)")
    plt.ylabel("Final Marks")
    plt.title("Attendance vs Final Marks")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_assignment_vs_marks(df):
    """Plot the relationship between assignment scores and final marks."""
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Assignment_Score"], df["Final_Marks"])
    plt.xlabel("Assignment Score")
    plt.ylabel("Final Marks")
    plt.title("Assignment Score vs Final Marks")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def create_all_visualizations(df):
    """Generate all student performance visualizations."""
    plot_study_hours_vs_marks(df)
    plot_attendance_vs_marks(df)
    plot_assignment_vs_marks(df)