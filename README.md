# Student Performance Analysis Using Python

A Python-based data analysis project for studying student academic performance using
Pandas, NumPy, and Matplotlib.

---

## 📌 Project Overview

**Student Performance Analysis Using Python** is a data analysis project developed
to understand and analyze the academic performance of students using Python.

The project uses a structured dataset containing information about students'
study hours, attendance, assignment scores, previous marks, and final examination
marks.

The collected information is analyzed using Python programming and data analysis
techniques to identify patterns, calculate statistical values, classify student
performance, and generate meaningful visualizations.

This project demonstrates how Python can be used to transform raw student data
into useful information that can help in understanding academic performance.

---

## 🎯 Project Objectives

The main objectives of this project are:

- To create and work with a structured student performance dataset.
- To understand how Pandas can be used for data analysis.
- To calculate important statistical values from the dataset.
- To analyze average student performance.
- To identify the highest and lowest performing students.
- To study the relationship between study hours and final marks.
- To analyze the relationship between attendance and final marks.
- To analyze the relationship between assignment scores and final marks.
- To compare previous marks with final examination marks.
- To classify students into different performance categories.
- To calculate the percentage of students in each category.
- To determine the overall class performance level.
- To visualize important relationships using Matplotlib.
- To demonstrate practical Python programming and data analysis skills.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Jupyter Notebook | Interactive analysis |
| Google Colab | Notebook development and execution |
| Git | Version control |
| GitHub | Project hosting and collaboration |

---

## 📚 Python Concepts Demonstrated

This project demonstrates several fundamental Python concepts, including:

- Variables
- Lists
- Dictionaries
- Functions
- Conditional statements
- Loops
- String formatting
- DataFrames
- Data filtering
- Statistical calculations
- Functions from Python libraries
- File and project organization

---
### 🧩 Module Responsibilities

The Python implementation is divided into separate modules to keep the project
organized and maintainable.

| Module | Responsibility |
|---|---|
| `data.py` | Creates and prepares the student dataset |
| `analysis.py` | Performs calculations, classification, statistics, and correlation analysis |
| `visualization.py` | Generates charts and visualizations |
| `main.py` | Controls the complete analysis workflow and displays the results |

This modular structure separates different responsibilities instead of keeping
the complete application in a single Python file.

# 📊 Dataset Description

The project contains data for **20 students**.

Each student record contains the following attributes:

| Column | Data Type | Description |
|---|---|---|
| `Student_ID` | Integer | Unique identification number of the student |
| `Study_Hours` | Integer | Number of hours spent studying |
| `Attendance` | Integer | Attendance percentage |
| `Assignment_Score` | Integer | Score obtained in assignments |
| `Previous_Marks` | Integer | Marks obtained previously |
| `Final_Marks` | Integer | Final examination marks |

### Example

```text
Student_ID    Study_Hours    Attendance    Assignment_Score    Final_Marks
1             2              65            55                  52
2             5              85            82                  80
3             3              72            68                  67