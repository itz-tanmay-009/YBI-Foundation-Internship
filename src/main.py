from data import create_student_dataset
from analysis import (
    calculate_averages,
    find_top_and_lowest_students,
    add_performance_category,
    calculate_category_statistics,
    calculate_correlation,
    determine_class_performance
)
from visualization import create_all_visualizations


def display_performance_summary(df, averages, class_level):
    """Display the final summary of student performance."""
    students_needing_improvement = (
        df["Performance_Category"] == "Needs Improvement"
    ).sum()

    print("\n" + "=" * 50)
    print("           PERFORMANCE SUMMARY")
    print("=" * 50)
    print(f"Total Students               : {len(df)}")
    print(f"Average Final Marks          : {averages['average_final']:.2f}")
    print(f"Highest Final Marks          : {df['Final_Marks'].max()}")
    print(f"Lowest Final Marks           : {df['Final_Marks'].min()}")
    print(
        f"Students Needing Improvement : "
        f"{students_needing_improvement}"
    )
    print(f"Overall Class Performance    : {class_level}")


def main():
    """Run the complete student performance analysis."""

    # Create the student dataset
    df = create_student_dataset()

    print("\n" + "=" * 50)
    print("       STUDENT PERFORMANCE ANALYSIS")
    print("=" * 50)

    # Display the dataset
    print("\n[1] STUDENT DATASET")
    print("-" * 50)
    print(df)

    # Display statistical summary
    print("\n[2] DATASET SUMMARY")
    print("-" * 50)
    print(df.describe())

    # Calculate average performance
    averages = calculate_averages(df)

    print("\n[3] AVERAGE PERFORMANCE")
    print("-" * 50)
    print(f"Average Final Marks       : {averages['average_final']:.2f}")
    print(f"Average Study Hours       : {averages['average_study']:.2f}")
    print(f"Average Attendance        : {averages['average_attendance']:.2f}%")
    print(
        f"Average Assignment Score  : "
        f"{averages['average_assignment']:.2f}"
    )

    # Find highest and lowest performing students
    highest_student, lowest_student = find_top_and_lowest_students(df)

    print("\n[4] HIGHEST PERFORMING STUDENT")
    print("-" * 50)
    print(highest_student)

    print("\n[5] LOWEST PERFORMING STUDENT")
    print("-" * 50)
    print(lowest_student)

    # Add performance categories
    df = add_performance_category(df)

    print("\n[6] PERFORMANCE CATEGORIES")
    print("-" * 50)
    print(
        df[
            ["Student_ID", "Final_Marks", "Performance_Category"]
        ]
    )

    # Calculate category statistics
    category_counts, category_percentages = (
        calculate_category_statistics(df)
    )

    print("\n[7] CATEGORY STATISTICS")
    print("-" * 50)

    print("Category Count:")
    print(category_counts)

    print("\nCategory Percentages:")
    for category, percentage in category_percentages.items():
        print(f"{category:<20}: {percentage:.1f}%")

    # Calculate correlations
    print("\n[8] CORRELATION WITH FINAL MARKS")
    print("-" * 50)
    print(calculate_correlation(df))

    # Generate visualizations
    print("\n[9] GENERATING VISUALIZATIONS")
    print("-" * 50)
    create_all_visualizations(df)

    # Determine overall class performance
    class_level = determine_class_performance(
        averages["average_final"]
    )

    # Display final summary
    display_performance_summary(
        df,
        averages,
        class_level
    )

    print("\nAnalysis completed successfully.")
    print("=" * 50)


if __name__ == "__main__":
    main()