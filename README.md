# MatrixForge

A simple Python package for matrix operations.

## Features

* Matrix Addition
* Matrix Subtraction
* Matrix Multiplication
* Matrix Transpose
* Scalar Multiplication
* Identity Matrix Generation

## Installation

### Method 1: Clone Repository

```bash
git clone https://github.com/Priyanshu-Mishra0930/MatrixForge.git
cd MatrixForge
pip install -e .
```

### Method 2: Download ZIP

1. Click **Code → Download ZIP**
2. Extract the ZIP file
3. Open a terminal in the project folder
4. Run:

```bash
pip install -e .
```

## Usage

```python
from matrixcalc import m_add, m_s_mul, identity

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print(m_add(A, B))

print(m_s_mul(A, 2))

print(identity(3))
```

Output:

```python
[[6, 8], [10, 12]]

[[2, 4], [6, 8]]

[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]
```

## Available Functions

| Function   | Description                 |
| ---------- | --------------------------- |
| m_add()    | Matrix Addition             |
| m_sub()    | Matrix Subtraction          |
| m_mul()    | Matrix Multiplication       |
| m_trans()  | Matrix Transpose            |
| m_s_mul()  | Scalar Multiplication       |
| identity() | Generate an Identity Matrix |

## Requirements

* Python 3.10 or higher

## Project Status

Current Version: **v1.1.0**

## Author

Prince
