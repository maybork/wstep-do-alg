import random
import numpy as np


STUDENTS = 10
COURSES = 5
POSSIBLE_GRADES = (2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5)


def create_matrix() -> np.ndarray:
    return np.random.choice(POSSIBLE_GRADES, (STUDENTS, COURSES))


def failed_students(matrix: np.ndarray, n: int) -> int:
    count = 0
    fails = matrix < 3.0
    for rows in fails:
        print(rows)
        if np.count_nonzero(rows) > n:
            count += 1
            print("added fail to total")
    print(count)
    return count


def students_with_highest_averages(matrix: np.ndarray) -> np.ndarray:
    avgs = np.average(matrix, axis=1)
    max_index = np.argmax(avgs)
    return matrix[max_index]


def students_with_lowest_averages(matrix: np.ndarray) -> np.ndarray:
    avgs = np.average(matrix, axis=1)
    min_index = np.argmin(avgs)
    return matrix[min_index]


def student_with_most_hi_grades(matrix: np.ndarray) -> int:
    maxgrade = matrix.max()
    maxgrades = matrix == maxgrade
    topno = 0
    topi = -1
    for i, row in enumerate(maxgrades):
        matching = np.count_nonzero(row)
        if matching > topno:
            topno, topi = matching, i
    return topi


def create_histogram(matrix: np.ndarray) -> list[np.ndarray]:
    result = []
    for row in matrix.T:
        hist, _ = np.histogram(row, bins=POSSIBLE_GRADES)
        result.append(hist)
    return result


def students_with_averages_ht(matrix: np.ndarray, treshold: float = 4.5):
    result = []
    avgs = np.average(matrix, axis=1)
    for i, avg in enumerate(avgs):
        if avg >= treshold:
            result.append(matrix[i].tolist())
    return result


edukacja_cl = create_matrix()
failed_students(edukacja_cl, 2)
# print(students_with_highest_averages(edukacja_cl))
# print(create_histogram(edukacja_cl))
# print(edukacja_cl)
# print(students_with_averages_ht(edukacja_cl))
# print(student_with_most_hi_grades(edukacja_cl))
