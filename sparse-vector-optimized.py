from typing import Sequence

class SparseVector:
    """Sparse vector.

    Args:
        values: A sequence with the values in this vector.

    Methods:
        get_non_zero_idxs: Get the indices where the vector is non zero.
        get_value_at_idx: Get the value at a given index.
        dot_product: Get the dot product of this vector and other vector.
        get_length: Get the length of this vector.
    """

    def __init__(self, values: Sequence[int]):
        self._length = len(values)

        self._idxs: set[int] = set()
        self._lookup_table: dict[int, int] = {}
        for idx, value in enumerate(values):
            if value != 0:
                self._idxs.add(idx)
                self._lookup_table[idx] = value

    def get_length(self) -> int:
        """Get the length of this vector."""
        return self._length

    def get_value_at_idx(self, idx: int) -> int:
        """Get the value of this vector at a given index."""
        return self._lookup_table.get(idx, 0)

    def get_non_zero_idxs(self) -> set[int]:
        """Get the indices where the vector is non zero."""
        return self._idxs

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

        this_length = self.get_length()
        other_length = other.get_length()
        if this_length != other_length:
            raise ValueError(f"Vectors do not have the same length {this_length} != {other_length}.")

        common_idxs = self.get_non_zero_idxs().intersection(other.get_non_zero_idxs())

        result = 0
        for idx in common_idxs:
            result += self.get_value_at_idx(idx) * other.get_value_at_idx(idx)
        return result

# Example usage
v1 = SparseVector([1, 0, 2, 0, 3, 1, 0, 2, 0, 3])
v2 = SparseVector([0, 2, 0, 4, 0,1, 0, 2, 0, 3])

print(v1.dot_product(v2))  # Output: 0*1 + 2*0 + 0*2 + 4*0 + 0*3 = 0