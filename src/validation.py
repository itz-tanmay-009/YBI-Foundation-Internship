def validate_dataset(df):
    """Validate the structure and values of the student dataset."""

    required_columns = {
        "Student_ID",
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Previous_Marks",
        "Final_Marks"
    }

    # Check required columns
    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    # Check for empty dataset
    if df.empty:
        raise ValueError("The student dataset is empty.")

    # Check for duplicate student IDs
    if df["Student_ID"].duplicated().any():
        raise ValueError("Duplicate Student_ID values found.")

    # Check marks are within valid range
    if not df["Final_Marks"].between(0, 100).all():
        raise ValueError("Final marks must be between 0 and 100.")

    if not df["Previous_Marks"].between(0, 100).all():
        raise ValueError("Previous marks must be between 0 and 100.")

    if not df["Assignment_Score"].between(0, 100).all():
        raise ValueError("Assignment scores must be between 0 and 100.")

    # Check attendance is within valid range
    if not df["Attendance"].between(0, 100).all():
        raise ValueError("Attendance must be between 0 and 100.")

    # Check study hours
    if (df["Study_Hours"] < 0).any():
        raise ValueError("Study hours cannot be negative.")

    return True