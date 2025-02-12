# Vector Class

The **Vector** class represents an n-dimensional mathematical vector with extensive operator overloading and standard vector-like operations. It is designed to mimic many of the features of C++'s `std::vector` while providing a Pythonic API.

## Features

### Size and Capacity Management

- **Size (`size`)** – Returns the number of elements in the vector.
- **Max Size (`max_size`)** – Represents the theoretical maximum number of elements the vector can hold.
- **Resize (`resize`)** – Changes the size of the vector by either truncating elements or appending new ones (with default values).
- **Capacity (`capacity`)** – Returns the allocated storage capacity (note: in Python, lists dynamically resize, but capacity can be simulated).
- **Empty (`is_empty`)** – Checks if the vector contains any elements.
- **Reserve (`reserve`)** – Reserves capacity for future elements (not strictly needed in Python but can be simulated).
- **Shrink to Fit (`shrink_to_fit`)** – Reduces the allocated capacity to match the actual size (this feature can be added as needed).

### Element Access

- **Back (`back`)** – Returns the last element. (You can implement this as `vector[-1]` or add a dedicated method.)
- **Data (`data`)** – Provides direct access to the underlying data structure.

### Modifiers

- **Push Back (`push_back`)** – Appends an element to the end of the vector.
- **Pop Back (`pop_back`)** – Removes the last element.
- **Insert (`insert`)** – Inserts elements at a specific position.
- **Erase (`erase`)** – Removes elements from a specific position.
- **Swap (`swap`)** – Swaps contents with another vector.
- **Clear (`clear`)** – Removes all elements from the vector.

### Operator Overloading

- **Addition (`+`)** – Adds two vectors element-wise.
- **Subtraction (`-`)** – Subtracts one vector from another element-wise.
- **Scalar Multiplication (`*`)** – Multiplies the vector by a scalar.
- **Dot Product (`*`)** – When multiplied with another vector (or iterable) of the same dimension, computes the dot product.
- **Division (`/` and `//`)** – Divides a vector by a scalar.
- **Equality (`==`)** & **Inequality (`!=`)** – Compares two vectors.
- **Indexing (`[]`)** – Accesses elements by index.
- **Length (`len`)** – Returns the number of elements in the vector.
- **String Representation (`__str__` and `__repr__`)** – Provides readable representations of the vector.
- **Boolean Conversion (`__bool__`)** – Returns `True` if the vector is non-empty.
- **Negation (`-`)** – Negates all elements of the vector.
- **Magnitude (`abs`)** – Returns the magnitude (Euclidean norm) of the vector.

## Installation

No special installation is needed. Simply clone this repository or copy the `vector.py` file into your project directory.

```bash
git clone https://github.com/yourusername/your-vector-repository.git
```

## Usage Example

Below is a basic example of how to use the Vector class:

```python
from vector import Vector

# Creating vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Vector addition (element-wise)
v3 = v1 + v2
print("v1 + v2 =", v3)  # Expected: (5, 7, 9)

# Scalar multiplication
v4 = v1 * 2
print("v1 * 2 =", v4)  # Expected: (2, 4, 6)

# Dot product
dot_product = v1 * v2
print("v1 * v2 =", dot_product)  # Expected: 32

# Indexing
print("v1[1] =", v1[1])  # Expected: 2

# Swapping vectors
v1.swap(v2)
print("Swapped v1 =", v1)  # Expected: (4, 5, 6)
print("Swapped v2 =", v2)  # Expected: (1, 2, 3)

# Clearing a vector
v1.clear()
print("v1 is empty:", v1.is_empty())  # Expected: True
```

## Contributing

Contributions, suggestions, and bug reports are welcome. Please feel free to open an issue or submit a pull request.

## License

[MIT License](LICENSE)