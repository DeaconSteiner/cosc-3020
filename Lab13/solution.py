"""
Lab Practice #13 — The Campus Cafe Problem
COSC 3020: Algorithms and Data Structures

The campus cafe prepares three items each morning:
  x1 = sandwiches   (profit $4 each)
  x2 = salads       (profit $5 each)
  x3 = smoothies    (profit $3 each)

Resource limits per day:
  Bread (slices):       2*x1                  <= 100
  Greens (oz):                   3*x2         <= 90
  Fruit (oz):           x1  +    x2  + 2*x3  <= 120
  Staff-minutes:        4*x1 +  5*x2  + 3*x3 <= 480
  x1, x2, x3 >= 0

Goal: maximize total daily profit.

---------------------------------------------------------------------------
Standard Form reminder (from lecture):
  All constraints are already in the form  A x <= b  with  x >= 0,
  so the problem is in standard LP form.

  We add slack variables s1, s2, s3, s4 to convert each inequality
  to an equality:
      2*x1                         + s1             = 100
               3*x2                     + s2        = 90
      x1   +   x2  + 2*x3                   + s3   = 120
      4*x1 +  5*x2 + 3*x3                       + s4 = 480

  Maximizing c^T x  is equivalent to minimizing  z = -c^T x.
  The objective row stores the POSITIVE coefficients of c; a column is
  an improvement candidate when its objective-row coefficient is > 0.

---------------------------------------------------------------------------
Your task:
  Implement the four functions below. Do NOT change simplex(),
  simplex_solution(), or the main block at the bottom.
---------------------------------------------------------------------------
"""

import numpy as np
from scipy.optimize import linprog  # used only for verification at the end


# ---------------------------------------------------------------------------
# TODO — Build the initial tableau
# ---------------------------------------------------------------------------
def build_tableau(c, A, b):
    """
    Build the initial simplex tableau for:
        maximize  c^T x   subject to   A x <= b,  x >= 0

    Return a 2-D numpy float array with this layout:

        Row 0       [ 1 | +c1  +c2 ... +cn | 0  0 ... 0 | 0 ]   objective row
        Row 1..m    [ 0 |        A          |     I      | b ]   constraints

    Columns:
      0          : z-column (1 in row 0, 0 elsewhere)
      1 .. n     : decision variables x1..xn
      n+1 .. n+m : slack variables s1..sm  (identity block)
      last       : right-hand side (0 in row 0, b elsewhere)

    The objective row stores the POSITIVE coefficients of c — not negated.
    This matches the lecture convention: a positive entry means "increasing
    this variable improves the objective."

    Parameters
    ----------
    c : list or array, length n       objective coefficients (to maximise)
    A : list of lists, shape (m, n)   constraint coefficient matrix
    b : list or array, length m       right-hand side values

    Returns
    -------
    tableau : np.ndarray, shape (m+1, n+m+2)
    """
    # TODO: implement this function
    c = np.array(c, dtype=float)
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    m, n = A.shape
    tableau = np.zeros((1 + m, n + m + 2))

    # Objective row: ROW 0
    tableau[0, 0] = 1  # z-column
    tableau[0, 1 : n + 1] = c  # decision variables (x1, x,2, x3)

    # Constraint rows: ROW 1..m
    tableau[1:, 1 : n + 1] = A  # Constraint matrix
    tableau[1:, n + 1 : n + 1 + m] = np.identity(m)  # Identity matrix (size m)
    tableau[1:, -1] = b  # RHS

    return tableau


# ---------------------------------------------------------------------------
# TODO — Choose the pivot column (entering variable)
# ---------------------------------------------------------------------------
def simplex_pivot_column(tableau):
    """
    Find the entering variable: the column (among columns 1 .. n+m, excluding
    the z-column and the RHS column) with the LARGEST POSITIVE coefficient in
    the objective row (row 0).

    If no such column exists, the current solution is already optimal.

    Parameters
    ----------
    tableau : np.ndarray   current tableau

    Returns
    -------
    col : int   column index in the full tableau, or None if optimal
    """
    # TODO: implement this function
    col = tableau[0, 1:-1]

    max_val = np.max(col)
    if max_val <= 0:
        return None  # Already optimal

    return 1 + np.argmax(col)


# ---------------------------------------------------------------------------
# TODO — Choose the pivot row (leaving variable)
# ---------------------------------------------------------------------------
def simplex_pivot_row(tableau, col):
    """
    Find the leaving variable using the MINIMUM RATIO TEST.

    For each constraint row i (rows 1 .. m):
      - Only consider rows where  tableau[i, col] > 0
      - Compute the ratio  tableau[i, -1] / tableau[i, col]
      - Choose the row with the smallest ratio

    If no row has a positive entry in col, the problem is unbounded.

    Parameters
    ----------
    tableau : np.ndarray   current tableau
    col     : int          pivot column index

    Returns
    -------
    row : int   row index in the full tableau, or None if unbounded
    """
    # TODO: implement this function
    min_ratio = np.inf
    row = None
    for i in range(1, tableau.shape[0]):
        if tableau[i, col] <= 0:
            continue
        ratio = tableau[i, -1] / tableau[i, col]
        if ratio < min_ratio:
            min_ratio = ratio
            row = i

    return row


# ---------------------------------------------------------------------------
# TODO — Perform the Gauss-Jordan pivot
# ---------------------------------------------------------------------------
def simplex_pivot(tableau, row, col):
    """
    Perform one Gauss-Jordan elimination step (modify tableau IN PLACE):

      1. Divide pivot row by  tableau[row, col]  so the pivot element becomes 1.
      2. For every OTHER row i, subtract  tableau[i, col] * tableau[row]
         so that column col contains 0 in all rows except the pivot row.

    Parameters
    ----------
    tableau : np.ndarray   current tableau (modified in place)
    row     : int          pivot row index
    col     : int          pivot column index
    """
    # TODO: implement this function
    pivot = tableau[row, col]
    tableau[row] = tableau[row] / pivot

    for i in range(tableau.shape[0]):
        if i == row:
            continue
        factor = tableau[i, col]
        tableau[i] = tableau[i] - factor * tableau[row]


# ---------------------------------------------------------------------------
# DO NOT MODIFY BELOW THIS LINE
# ---------------------------------------------------------------------------


def simplex_solution(tableau, n_vars):
    """
    Read the variable values from the final tableau.

    A variable x_j is basic if its column is a unit vector (exactly one 1,
    all other entries 0). Its value equals the RHS entry of the row containing
    the 1. Non-basic variables are 0.
    """
    solution = np.zeros(n_vars)
    for j in range(1, n_vars + 1):
        col = tableau[:, j]
        ones = np.where(col == 1)[0]
        if len(ones) == 1 and np.count_nonzero(col) == 1:
            solution[j - 1] = tableau[ones[0], -1]
    return solution


def simplex(c, A, b):
    """
    Solve:  maximize  c^T x   subject to   A x <= b,  x >= 0.

    Returns (optimal_value, solution_vector).
    Returns (inf, None) if the problem is unbounded.
    """
    n_vars = len(c)
    tableau = build_tableau(c, A, b)

    while True:
        col = simplex_pivot_column(tableau)
        if col is None:
            break  # no improving direction: optimal
        row = simplex_pivot_row(tableau, col)
        if row is None:
            return float("inf"), None  # unbounded
        simplex_pivot(tableau, row, col)

    opt_value = -tableau[0, -1]  # negate: we stored +c, minimised z
    solution = simplex_solution(tableau, n_vars)
    return opt_value, solution


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    c = [4, 5, 3]  # profit per sandwich, salad, smoothie
    A = [
        [2, 0, 0],  # bread constraint
        [0, 3, 0],  # greens constraint
        [1, 1, 2],  # fruit constraint
        [4, 5, 3],  # staff-minutes constraint
    ]
    b = [100, 90, 120, 480]

    opt_val, sol = simplex(c, A, b)

    print("=== Campus Cafe — Optimal Daily Plan ===")
    print(f"  Sandwiches (x1) : {sol[0]:.2f}")
    print(f"  Salads     (x2) : {sol[1]:.2f}")
    print(f"  Smoothies  (x3) : {sol[2]:.2f}")
    print(f"  Max profit      : ${opt_val:.2f}")

    # Verification using scipy — do not use this as your solver
    print("\n--- Verification (scipy.optimize.linprog) ---")
    res = linprog(
        [-c_i for c_i in c], A_ub=A, b_ub=b, bounds=[(0, None)] * len(c), method="highs"
    )
    print(f"  scipy optimal   : ${-res.fun:.2f}")
    if abs(opt_val - (-res.fun)) < 1e-4:
        print("  Results match. \u2713")
    else:
        print("  WARNING: results do not match — check your implementation.")
