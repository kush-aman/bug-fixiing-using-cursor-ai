# Student Grading Utility — Bug Fixing & Refactoring

This repository contains a Python utility for calculating student grades and running automated unit tests. It demonstrates common programming pitfalls, their fixes, and best practices for code readability and maintainability.

---

## 📁 Repository Structure

| File | Description |
|------|-------------|
| [`error-code.py`](error-code.py) | Original code containing syntax errors, logical bugs, and Jupyter notebook artifacts. Kept in its original state for reference. |
| [`fixed-code.py`](fixed-code.py) | Fully fixed, refactored, and self-contained version with clear variable names, type hints, docstrings, and passing unit tests. |
| [`README.md`](README.md) | Project documentation and bug analysis report. |

---

## 🐛 Identified Bugs & Solutions

### 1. Jupyter Notebook Magic Commands
* **Problem**: The original script contained `%%writefile student_utils.py` and `%%writefile test_student_utils.py` lines, which are valid in Jupyter notebooks but cause syntax errors when executed with standard Python.
* **Fix**: Removed notebook magic commands and unified the code into a standard Python script.

### 2. Off-by-One in Average Calculation
* **Problem**: The average calculation function divided the total sum by `len(marks) - 1`. For a single-item list, this caused a `ZeroDivisionError`, and for multiple items, it produced an inflated average.
* **Fix**: Divided by `len(marks_list)` and added a guard clause for empty lists.

### 3. Strict Inequality in Pass Mark Validation
* **Problem**: The condition `mark > PASS_MARK` required a score strictly greater than 40 to pass, causing a student with exactly 40 to fail.
* **Fix**: Updated the comparison to `student_mark >= MINIMUM_PASS_MARK`.

### 4. Shadowed Condition in Grade Classification
* **Problem**: In `get_grade()`, the branch `average >= 60` was checked before `average >= 90`. Because 90+ is also $\ge 60$, any score above 90 returned `"First"` instead of `"Distinction"`.
* **Fix**: Reordered condition checks from highest threshold to lowest (`>= 90` first, then `>= 60`, then `>= 45`).

### 5. Broken Module Import
* **Problem**: The test suite attempted to import functions using `from student_utils import ...`, raising a `ModuleNotFoundError` because no separate `student_utils.py` file existed on disk.
* **Fix**: Made `fixed-code.py` self-contained so that unit tests test the functions directly within the same module.

---

## ✨ Readability & Code Quality Improvements

In [`fixed-code.py`](fixed-code.py), several refactoring best practices were applied:

- **Descriptive Variable Names**:
  - `m` $\rightarrow$ `score`
  - `marks` $\rightarrow$ `marks_list`
  - `total` $\rightarrow$ `total_sum`
  - `mark` $\rightarrow$ `student_mark`
  - `average` $\rightarrow$ `average_score`
- **Named Constants**: Hardcoded numbers were replaced with clear constants (`MINIMUM_PASS_MARK`, `DISTINCTION_THRESHOLD`, `FIRST_CLASS_THRESHOLD`, `SECOND_CLASS_THRESHOLD`).
- **Type Annotations & Docstrings**: Added PEP 484 type hints (`list[float]`, `float`, `bool`, `str`) and Google-style docstrings for full self-documentation.
- **Idiomatic Assertions**: Converted `assertEqual(..., True/False)` in unit tests to idiomatic `assertTrue()` and `assertFalse()`.

---

## 🚀 How to Run the Tests

Execute the fixed script directly using Python 3:

```bash
python3 fixed-code.py
```

### Expected Output

```text
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```
