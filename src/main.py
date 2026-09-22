import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Create student performance dataset
data = {
    "Student_ID": range(1, 21),
    "Study_Hours": [2, 5, 3, 7, 4, 6, 1, 8, 5, 3, 7, 2, 6, 4, 9, 3, 5, 8, 2, 6],
    "Attendance": [65, 85, 72, 95, 80, 88, 60, 97, 82, 70, 92, 68, 90, 78, 98, 75, 84, 94, 63, 87],
    "Assignment_Score": [55, 82, 68, 91, 76, 85, 48, 94, 80, 65, 89, 58, 86, 73, 96, 70, 81, 92, 52, 84],
    "Previous_Marks": [50, 78, 65, 88, 72, 82, 45, 91, 76, 60, 85, 54, 80, 70, 94, 66, 79, 89, 48, 81],
    "Final_Marks": [52, 80, 67, 92, 75, 86, 47, 95, 81, 64, 90, 57, 84, 74, 97, 69, 82, 93, 50, 85]
}

df = pd.DataFrame(data)

print("STUDENT PERFORMANCE ANALYSIS")
print("=" * 35)


# Display dataset
print("\nStudent Dataset:")
print(df)


# Basic statistics
print("\nDataset Summary:")
print(df.describe())


# Calculate averages
average_final = df["Final_Marks"].mean()
average_study = df["Study_Hours"].mean()
average_attendance = df["Attendance"].mean()
average_assignment = df["Assignment_Score"].mean()

print(f"\nAverage Final Marks: {average_final:.2f}")
print(f"Average Study Hours: {average_study:.2f}")
print(f"Average Attendance: {average_attendance:.2f}%")
print(f"Average Assignment Score: {average_assignment:.2f}")


# Find highest and lowest performing students
highest_student = df.loc[df["Final_Marks"].idxmax()]
lowest_student = df.loc[df["Final_Marks"].idxmin()]

print("\nHighest Performing Student:")
print(highest_student)

print("\nLowest Performing Student:")
print(lowest_student)


# Performance categorization
def performance_category(marks):
    if marks >= 85:
        return "Excellent"
    elif marks >= 70:
        return "Good"
    else:
        return "Needs Improvement"


df["Performance_Category"] = df["Final_Marks"].apply(
    performance_category
)

print("\nPerformance Categories:")
print(
    df[
        ["Student_ID", "Final_Marks", "Performance_Category"]
    ]
)


# Category count and percentage
category_counts = df["Performance_Category"].value_counts()

category_percentages = (
    df["Performance_Category"].value_counts(normalize=True) * 100
)

print("\nCategory Count:")
print(category_counts)

print("\nPerformance Category Percentages:")

for category, percentage in category_percentages.items():
    print(f"{category}: {percentage:.1f}%")


# Correlation analysis
print("\nCorrelation with Final Marks:")

print(
    df[
        [
            "Study_Hours",
            "Attendance",
            "Assignment_Score",
            "Previous_Marks",
            "Final_Marks"
        ]
    ].corr()["Final_Marks"]
)


# Visualization 1: Study Hours vs Final Marks
plt.figure(figsize=(8, 5))

plt.scatter(
    df["Study_Hours"],
    df["Final_Marks"]
)

plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")
plt.grid(True)

plt.show()


# Visualization 2: Attendance vs Final Marks
plt.figure(figsize=(8, 5))

plt.scatter(
    df["Attendance"],
    df["Final_Marks"]
)

plt.xlabel("Attendance (%)")
plt.ylabel("Final Marks")
plt.title("Attendance vs Final Marks")
plt.grid(True)

plt.show()


# Visualization 3: Assignment Score vs Final Marks
plt.figure(figsize=(8, 5))

plt.scatter(
    df["Assignment_Score"],
    df["Final_Marks"]
)

plt.xlabel("Assignment Score")
plt.ylabel("Final Marks")
plt.title("Assignment Score vs Final Marks")
plt.grid(True)

plt.show()


# Quick performance summary
print("\n--- Performance Summary ---")

print(f"Total Students: {len(df)}")

print(
    f"Average Final Marks: "
    f"{average_final:.2f}"
)

print(
    f"Highest Final Marks: "
    f"{df['Final_Marks'].max()}"
)

print(
    f"Lowest Final Marks: "
    f"{df['Final_Marks'].min()}"
)

print(
    f"Students Needing Improvement: "
    f"{(df['Performance_Category'] == 'Needs Improvement').sum()}"
)


# Identify the overall class performance level
if average_final >= 85:
    class_level = "Excellent"
elif average_final >= 70:
    class_level = "Good"
else:
    class_level = "Needs Improvement"

print(f"Overall Class Performance: {class_level}")


print("\nAnalysis completed successfully.")