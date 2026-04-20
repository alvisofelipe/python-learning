"""
Student Grade Tracker
CS 1300 — Lecture 5 Mini-Project

A modular, well-tested program that collects exam scores,
calculates a letter grade and academic standing, and
displays a formatted report.

Functions:
    get_student_name         — Prompt for and return student name
    is_valid_score           — Helper: validate a single score
    get_validated_score      — Helper: retry loop for score entry
    get_exam_scores          — Collect exam scores with validation
    calculate_average        — Compute mean of a scores list
    determine_letter_grade   — Map average to letter grade
    determine_standing       — Map average to academic standing
    print_divider            — Helper: print a decorative line
    display_report           — Print the formatted grade report
    test_grade_tracker       — Run unit tests
    main                     — Orchestrate the full program
"""


def get_student_name():
    """
    Prompt the user for a student's name.

    Returns:
        str: The student's name.
    """
    # Keep asking until the user enters a non-empty name
    while True:
        name = input("Student name: ").strip()
        if name != "":
            return name
        print("Name cannot be empty. Please try again.")


def is_valid_score(score):
    """
    Check whether a score is valid.

    A valid score must be between 0 and 100 inclusive.

    Args:
        score (int): The score to validate.

    Returns:
        bool: True if the score is valid, False otherwise.
    """
    return 0 <= score <= 100


def get_validated_score(exam_number):
    """
    Prompt the user for one exam score and validate it.

    This function keeps asking until the user enters
    a whole number between 0 and 100.

    Args:
        exam_number (int): The exam number being entered.

    Returns:
        int: A valid exam score.
    """
    while True:
        score_text = input(f"Exam {exam_number} score: ")

        # Check if the input can be converted to an integer
        try:
            score = int(score_text)

            # Check if the score is within the allowed range
            if is_valid_score(score):
                return score
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_exam_scores(num_exams=3):
    """
    Collect a list of validated exam scores from the user.

    Args:
        num_exams (int): Number of exam scores to collect.
                         Defaults to 3.

    Returns:
        list[int]: A list of valid exam scores.
    """
    scores = []

    # Collect one validated score at a time
    for exam_number in range(1, num_exams + 1):
        score = get_validated_score(exam_number)
        scores.append(score)

    return scores


def calculate_average(scores):
    """
    Calculate the average of a list of scores.

    Args:
        scores (list[int]): A list of numeric scores.

    Returns:
        float: The average score. Returns 0.0 if the list is empty.
    """
    # Handle the edge case of an empty list
    if len(scores) == 0:
        return 0.0

    return sum(scores) / len(scores)


def determine_letter_grade(average):
    """
    Determine the letter grade based on the average.

    Args:
        average (float): The student's average score.

    Returns:
        str: The letter grade.
    """
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def determine_standing(average):
    """
    Determine the academic standing based on the average.

    Args:
        average (float): The student's average score.

    Returns:
        str: The academic standing.
    """
    if average >= 90:
        return "Dean's List"
    elif average >= 70:
        return "Good Standing"
    elif average >= 60:
        return "Academic Probation"
    else:
        return "Academic Warning"


def print_divider(character="=", length=30):
    """
    Print a decorative divider line.

    Args:
        character (str): The character to repeat.
        length (int): The number of times to repeat it.

    Returns:
        None
    """
    print(character * length)


def display_report(name, scores, average, grade, standing):
    """
    Display the formatted student grade report.

    Args:
        name (str): Student name.
        scores (list[int]): List of exam scores.
        average (float): Calculated average.
        grade (str): Letter grade.
        standing (str): Academic standing.

    Returns:
        None
    """
    print_divider("=", 30)
    print("STUDENT GRADE REPORT")
    print_divider("=", 30)

    print(f"Student: {name}")

    # Print each exam score on its own line
    for i, score in enumerate(scores, start=1):
        print(f"Exam {i}: {score}")

    print_divider("-", 30)
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")
    print(f"Standing: {standing}")
    print_divider("=", 30)


def test_grade_tracker():
    """
    Run tests for the calculation and classification functions.

    This function uses simple print-based tests for:
    - normal cases
    - edge cases
    - boundary cases

    Returns:
        None
    """
    print("\nRunning tests...")
    print_divider("-", 40)

    # -------------------------------
    # Tests for calculate_average()
    # -------------------------------
    print("Testing calculate_average()")

    # Normal case
    result = calculate_average([90, 80, 70])
    expected = 80.0
    print("Test 1:", "PASS" if result == expected else f"FAIL (got {result}, expected {expected})")

    # Perfect scores
    result = calculate_average([100, 100, 100])
    expected = 100.0
    print("Test 2:", "PASS" if result == expected else f"FAIL (got {result}, expected {expected})")

    # Empty list edge case
    result = calculate_average([])
    expected = 0.0
    print("Test 3:", "PASS" if result == expected else f"FAIL (got {result}, expected {expected})")

    print()

    # -----------------------------------
    # Tests for determine_letter_grade()
    # -----------------------------------
    print("Testing determine_letter_grade()")

    # Boundary tests
    tests = [
        (90, "A"),
        (89.99, "B"),
        (80, "B"),
        (79.99, "C"),
        (70, "C"),
        (69.99, "D"),
        (60, "D"),
        (59.99, "F"),
    ]

    for i, (avg, expected) in enumerate(tests, start=1):
        result = determine_letter_grade(avg)
        print(f"Test {i}:", "PASS" if result == expected else f"FAIL (got {result}, expected {expected})")

    print()

    # --------------------------------
    # Tests for determine_standing()
    # --------------------------------
    print("Testing determine_standing()")

    standing_tests = [
        (95, "Dean's List"),
        (90, "Dean's List"),
        (85, "Good Standing"),
        (70, "Good Standing"),
        (65, "Academic Probation"),
        (60, "Academic Probation"),
        (59, "Academic Warning"),
    ]

    for i, (avg, expected) in enumerate(standing_tests, start=1):
        result = determine_standing(avg)
        print(f"Test {i}:", "PASS" if result == expected else f"FAIL (got {result}, expected {expected})")

    print()

    # -------------------------
    # Tests for is_valid_score()
    # -------------------------
    print("Testing is_valid_score()")

    validity_tests = [
        (0, True),
        (100, True),
        (50, True),
        (-1, False),
        (101, False),
    ]

    for i, (score, expected) in enumerate(validity_tests, start=1):
        result = is_valid_score(score)
        print(f"Test {i}:", "PASS" if result == expected else f"FAIL (got {result}, expected {expected})")

    print_divider("-", 40)
    print("Tests complete.\n")


def main():
    """
    Run the full Student Grade Tracker program.

    Returns:
        None
    """
    print("Welcome to the Student Grade Tracker!")

    # Step 1: Get student information
    name = get_student_name()

    # Step 2: Get exam scores
    scores = get_exam_scores(3)

    # Step 3: Calculate results
    average = calculate_average(scores)
    grade = determine_letter_grade(average)
    standing = determine_standing(average)

    # Step 4: Display final report
    display_report(name, scores, average, grade, standing)


# Run the program only if this file is executed directly
if __name__ == "__main__":
    # Uncomment the next line if your instructor wants tests shown first
    test_grade_tracker()

    # Run the actual program
    main()