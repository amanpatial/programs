from collections.abc import Sequence
from typing import Self

class SparseVector:
    """Sparse vector.

    Args:
    values: A sequence with the values in this vector.

    Methods:
    get_values: Get a list with the values in this vector.
    dot_product: Get the dot product of this vector and other vector.
    """
    
    def __init__(self, values: Sequence[int]):
        self._values = list(values)

    def get_values(self) -> list[int]:
        """Get the values of this vector."""
        return self._values

    def dot_product(self, other: 'SparseVector') -> int:
        """Get the dot product of this vector and other vector.
  
        Args:
         other: A SparseVector.
      
        Returns:
         The dot product of this vector and other vector.
    
        Raises:
         ValueError: If `other` is not a SparseVector or if the two vectors do not
           have the same length.
        """

        if not isinstance(other, SparseVector):
            raise ValueError(f"`other` must be a SparseVector (got {type(other)} instead).")

        other_values = other.get_values()
        if len(other_values) != len(self._values):
            raise ValueError(f"Vectors do not have the same length {len(self._values)} != {len(other_values)}")

        result = 0
        for v1, v2 in zip(self._values, other_values):
            result += v1 * v2
        return result

# Example usage
v1 = SparseVector([1, 2, 3])
v2 = SparseVector([1, 2, 5])

print(v1.dot_product(v2))  # Output: 1*1 + 2*2 + 3*5 = 1 + 4 + 15 = 20