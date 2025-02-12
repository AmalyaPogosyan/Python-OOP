import sys
from typing import Iterable, Union, Any

class VectorOverflowError(Exception):
    """Raised when more elements are added than the vector's maximum allowed size."""
    pass

class DimensionalError(Exception):
    """Raised when two vectors have different dimensions."""
    pass

class Vector:
    """
    An n-dimensional vector class that supports element-wise operations, operator overloading,
    and standard vector-like functionalities.
    """
    
    def __init__(self, *args: Union[int, float]) -> None:
        """
        Constructs a vector with the provided elements.
        
        :param args: The initial elements of the vector.
        """
        self._max_size: int = sys.maxsize
        self._size: int = len(args)
        self._capacity: int = self._size * 2 + 1
        self._data: list[Union[int, float]] = list(args)
        
    @property
    def size(self) -> int:
        """Returns the current size (number of elements) of the vector."""
        return self._size
    
    @size.setter
    def size(self, new_size: int) -> None:
        if new_size > self._max_size:
            raise VectorOverflowError(f"Cannot add more elements: max size {self._max_size} exceeded.")
        self._size = new_size

    @property
    def capacity(self) -> int:
        """Returns the current capacity of the vector."""
        return self._capacity
    
    def _adjust_capacity(self, new_capacity: int = 0) -> None:
        """
        Adjusts the vector's capacity to be at least new_capacity.
        
        :param new_capacity: The required minimum capacity.
        """
        while self._capacity < new_capacity:
            self._capacity *= 2
            
    def resize(self, new_size: int, *args: Union[int, float]) -> None:
        """
        Resizes the vector. If new_size is less than the current size, truncates the vector.
        If new_size is greater than the current size, appends new elements.
        
        :param new_size: The desired new size of the vector.
        :param args: The new elements to add (must be enough to reach new_size).
        """
        if new_size < self.size:
            self._data = self._data[:new_size]
        else:
            if new_size > self.capacity:
                self._adjust_capacity(new_size)
            additional_elements = list(args)[:new_size - self.size]
            if len(additional_elements) < (new_size - self.size):
                raise IndexError('Not enough default values provided to extend the vector.')
            self._data.extend(additional_elements)
        self.size = new_size
        
    def is_empty(self) -> bool:
        """Returns True if the vector is empty."""
        return self.size == 0
    
    def clear(self) -> None:
        """Clears all elements from the vector and resets its capacity."""
        self._data.clear()
        self.size = 0
        self._capacity = 1
        
    def push_back(self, elem: Union[int, float]) -> None:
        """Appends an element to the end of the vector."""
        self.resize(self.size + 1, elem)
        
    def pop_back(self) -> None:
        """Removes the last element of the vector."""
        if self.is_empty():
            raise IndexError('Cannot pop from an empty vector.')
        self._data.pop()
        self.size -= 1
        
    def insert(self, index: int, elem: Union[int, float]) -> None:
        """
        Inserts an element at the specified index.
        
        :param index: The index at which to insert the element.
        :param elem: The element to insert.
        """
        if index < 0 or index > self.size:
            raise IndexError('Index out of range.')
        self._data.insert(index, elem)
        self.size += 1
        
    def erase(self, index: int) -> None:
        """
        Erases the element at the specified index.
        
        :param index: The index of the element to erase.
        """
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range.')
        del self._data[index]
        self.size -= 1
        
    def swap(self, other: 'Vector') -> None:
        """
        Swaps the contents of this vector with another.
        
        :param other: The other Vector to swap with.
        """
        if not isinstance(other, Vector):
            raise TypeError('Swap operation requires another Vector.')
        self._data, other._data = other._data, self._data
        self.size, other.size = other.size, self.size
        self._capacity, other._capacity = other._capacity, self._capacity
        
    def __str__(self) -> str:
        """Returns a human-readable string representation of the vector."""
        return str(tuple(self._data))
    
    def __repr__(self) -> str:
        """Returns an unambiguous string representation of the vector."""
        return f"Vector({', '.join(map(str, self._data))})"
    
    def _validate_operands(self, other: Union['Vector', Iterable]) -> None:
        """
        Validates that the operand has the same dimensions as this vector.
        
        :param other: A Vector or Iterable to validate against.
        """
        if not isinstance(other, (Vector, Iterable)):
            raise TypeError('Operand must be a Vector or Iterable.')
        if isinstance(other, Vector) and self.size != other.size:
            raise DimensionalError('Vectors have different dimensions.')
        if isinstance(other, Iterable) and self.size != len(other):
            raise DimensionalError('Vectors have different dimensions.')
    
    def __add__(self, other: Union['Vector', Iterable]) -> 'Vector':
        """
        Returns a new vector that is the element-wise sum of this vector and another.
        
        :param other: A Vector or Iterable to add.
        """
        self._validate_operands(other)
        if isinstance(other, Vector):
            return Vector(*[a + b for a, b in zip(self._data, other._data)])
        return Vector(*[a + b for a, b in zip(self._data, other)])
    
    def __iadd__(self, other: Union['Vector', Iterable]) -> 'Vector':
        """
        Performs in-place element-wise addition.
        
        :param other: A Vector or Iterable to add.
        """
        self._validate_operands(other)
        if isinstance(other, Vector):
            self._data = [a + b for a, b in zip(self._data, other._data)]
        else:
            self._data = [a + b for a, b in zip(self._data, other)]
        return self
    
    def __sub__(self, other: Union['Vector', Iterable]) -> 'Vector':
        """
        Returns a new vector that is the element-wise difference of this vector and another.
        
        :param other: A Vector or Iterable to subtract.
        """
        self._validate_operands(other)
        if isinstance(other, Vector):
            return Vector(*[a - b for a, b in zip(self._data, other._data)])
        return Vector(*[a - b for a, b in zip(self._data, other)])
    
    def __isub__(self, other: Union['Vector', Iterable]) -> 'Vector':
        """
        Performs in-place element-wise subtraction.
        
        :param other: A Vector or Iterable to subtract.
        """
        self._validate_operands(other)
        if isinstance(other, Vector):
            self._data = [a - b for a, b in zip(self._data, other._data)]
        else:
            self._data = [a - b for a, b in zip(self._data, other)]
        return self
    
    def __mul__(self, other: Union[int, float, 'Vector', Iterable]) -> Union['Vector', Union[int, float]]:
        """
        If 'other' is a number, returns a new vector that is the result of scalar multiplication.
        If 'other' is a Vector or Iterable, returns the dot product.
        
        :param other: A number, Vector, or Iterable.
        """
        if isinstance(other, (int, float)):
            return Vector(*[a * other for a in self._data])
        self._validate_operands(other)
        if isinstance(other, Vector):
            return sum(a * b for a, b in zip(self._data, other._data))
        return sum(a * b for a, b in zip(self._data, other))
    
    def __rmul__(self, other: Union[int, float]) -> 'Vector':
        """Supports scalar multiplication from the left-hand side."""
        return self.__mul__(other)
    
    def __truediv__(self, scalar: Union[int, float]) -> 'Vector':
        """
        Returns a new vector that is the result of dividing this vector by a scalar.
        
        :param scalar: A number to divide by.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError('Division requires a numeric scalar.')
        return Vector(*[a / scalar for a in self._data])
    
    def __floordiv__(self, scalar: Union[int, float]) -> 'Vector':
        """
        Returns a new vector that is the result of floor dividing this vector by a scalar.
        
        :param scalar: A number to divide by.
        """
        if not isinstance(scalar, (int, float)):
            raise TypeError('Division requires a numeric scalar.')
        return Vector(*[a // scalar for a in self._data])
    
    def __eq__(self, other: Any) -> bool:
        """Checks whether two vectors are equal."""
        if not isinstance(other, Vector):
            return False
        return self._data == other._data
    
    def __getitem__(self, index: int) -> Union[int, float]:
        """
        Returns the element at the given index.
        
        :param index: The index of the element.
        """
        if index < 0 or index >= self.size:
            raise IndexError('Index out of range.')
        return self._data[index]
    
    def __len__(self) -> int:
        """Returns the number of elements in the vector."""
        return self.size
    
    def __bool__(self) -> bool:
        """Returns True if the vector is not empty."""
        return not self.is_empty()
    
    def __neg__(self) -> 'Vector':
        """Returns a new vector that is the negation of this vector."""
        return Vector(*[-a for a in self._data])
    
    def __abs__(self) -> float:
        """
        Returns the Euclidean norm of the vector.
        
        :return: sqrt(a1^2 + a2^2 + ... + an^2)
        """
        return sum(a ** 2 for a in self._data) ** 0.5

# Example usage
if __name__ == '__main__':
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    # Vector addition
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
    print("v1 is empty:", v1.is_empty())
