# Matrix Calculator

A simple Python package for matrix operations.

## Features

- Matrix Addition
- Matrix Subtraction
- Matrix Multiplication
- Matrix Transpose

## Installation

### Method 1: Clone Repository

```bash
git clone https://github.com/Priyanshu-Mishra0930/MatrixCalculator.git
cd MatrixCalculator
pip install -e .
```

### Method 2: Download ZIP

1. Click **Code → Download ZIP**
2. Extract the ZIP file
3. Open terminal in the project folder
4. Run:

```bash
pip install -e .
```

## Usage

```python
from matrixcalc import m_add

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = m_add(A, B)

print(result)
```

Output:

```python
[[6, 8],
 [10, 12]]
```

## Available Functions

| Function | Description |
|----------|-------------|
| m_add() | Matrix Addition |
| m_sub() | Matrix Subtraction |
| m_mul() | Matrix Multiplication |
| m_trans() | Matrix Transpose |

## Requirements

- Python 3.10 or higher

## Author

Prince