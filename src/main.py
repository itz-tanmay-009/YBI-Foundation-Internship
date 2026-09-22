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


def main():
    """Run the complete student performance analysis."""

    # Create dataset
    df = create_student_dataset()

    print("STUDENT PERFORMANCE ANALYSIS")
    print("=" * 35)

    # Display dataset
    print("\nStudent Dataset:")
    print(df)

    # Basic statistics
    print("\nDataset Summary:")
    print(df.describe())

    # Calculate averages
    averages = calculate_averages(df)

    print(
        f"\nAverage Final Marks: "
        f"{averages['average_final']:.2f}"
    )

    print(
        f"Average Study Hours: "
        f"{averages['average_study']:.2f}"
    )

    print(
        f"Average Attendance: "
        f"{averages['average_attendance']:.2f}%"
    )

    print(
        f"Average Assignment Score: "
        f"{averages['average_assignment']:.2f}"
    )

    # Find highest and lowest performers
    highest_student, lowest_student = (
        find_top_and_lowest_students(df)
    )

    print("\nHighest Performing Student:")
    print(highest_student)

    print("\nLowest Performing Student:")
    print(lowest_student)

    # Add performance categories
    df = add_performance_category(df)

    print("\nPerformance Categories:")
    print(
        df[
            [
                "Student_ID",
                "Final_Marks",
                "Performance_Category"
            ]
        ]
    )

    # Category statistics
    category_counts, category_percentages = (
        calculate_category_statistics(df)
    )

    print("\nCategory Count:")
    print(category_counts)

    print("\nPerformance Category Percentages:")

    for category, percentage in category_percentages.items():
        print(
            f"{category}: "
            f"{percentage:.1f}%"
        )

    # Correlation analysis
    print("\nCorrelation with Final Marks:")

    print(calculate_correlation(df))

    # Generate visualizations
    create_all_visualizations(df)

    # Performance summary
    print("\n--- Performance Summary ---")

    print(f"Total Students: {len(df)}")

    print(
        f"Average Final Marks: "
        f"{averages['average_final']:.2f}"
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

    # Overall class performance
    class_level = determine_class_performance(
        averages["average_final"]
    )

    print(
        f"Overall Class Performance: "
        f"{class_level}"
    )

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()