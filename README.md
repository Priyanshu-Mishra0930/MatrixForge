# MatrixForge

A lightweight Python package for performing common matrix operations.

## Features

* Matrix Addition
* Matrix Subtraction
* Matrix Multiplication
* Matrix Transpose
* Scalar Multiplication
* Identity Matrix Generation
* Determinant Calculation (Supports n × n matrices)

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Priyanshu-Mishra0930/MatrixForge.git
cd MatrixForge
pip install -e .
```

### Download ZIP

1. Click **Code → Download ZIP**
2. Extract the archive
3. Open a terminal in the project folder
4. Run:

```bash
pip install -e .
```

---

## Quick Start

```python
from matrixcalc import (
    m_add,
    m_sub,
    m_mul,
    m_trans,
    m_s_mul,
    identity,
    determinant
)

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print(m_add(A, B))
print(m_s_mul(A, 2))
print(identity(3))
print(determinant(A))
```

### Output

```python
[[6, 8], [10, 12]]

[[2, 4], [6, 8]]

[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]

-2
```

---

## Available Functions

| Function        | Description                              |
| --------------- | ---------------------------------------- |
| `m_add()`       | Matrix Addition                          |
| `m_sub()`       | Matrix Subtraction                       |
| `m_mul()`       | Matrix Multiplication                    |
| `m_trans()`     | Matrix Transpose                         |
| `m_s_mul()`     | Scalar Multiplication                    |
| `identity()`    | Generate an Identity Matrix              |
| `determinant()` | Calculate Determinant of an n × n Matrix |

---

## Example

```python
from matrixcalc import determinant

matrix = [
    [1, 2, 3],
    [0, 4, 5],
    [1, 0, 6]
]

print(determinant(matrix))
```

Output:

```python
22
```

---

## Requirements

* Python 3.10+

---

## Project Structure

```text
matrixcalc/
├── addition.py
├── subtraction.py
├── multiplication.py
├── transpose.py
├── scalar_multiplication.py
├── identity.py
├── determinant.py
└── __init__.py
```

---

## Version

Current Version: **v1.2.0**

---

## Author

**Prince**
