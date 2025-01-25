"""
"""
class BaseArray:
    """
    """
    def __init__(self, size):
        self.size = size
        self.data_type = None
        self.array = [None] * size

    def set(self, index, value):
        if index > self.size - 1:
            raise IndexError('Out of Bounds: Index larger than array')
        if index < 0:
            raise IndexError('Out of Bounds: Index must be greater than 0')

        if self.data_type is not None and self.data_type is not type(value):
            raise TypeError(
                f'Arrays can only hold data of the same type \
                    ({self.data_type})'
            )

        if self.data_type is None:
            self.data_type = type(value)
        self.array[index] = value

        return self

    def index_of(self, value):
        if self.data_type is not None and self.data_type is not type(value):
            raise TypeError(
                f'Arrays can only hold data of the same type \
                    ({self.data_type})'
            )

        for index, element in enumerate(self.array):
            if element == value:
                return index

        return None

    def __getitem__(self, index):
        if index > self.size - 1:
            raise IndexError('Out of Bounds: Index larger than array')
        if index < 0:
            raise IndexError('Out of Bounds: Index must be greater than 0')

        return self.array[index]

    def __setitem__(self, index, value):
        if index > self.size - 1:
            raise IndexError('Out of Bounds: Index larger than array')
        if index < 0:
            raise IndexError('Out of Bounds: Index must be greater than 0')

        if self.data_type is not None and self.data_type is not type(value):
            raise TypeError(
                f'Arrays can only hold data of the same type \
                    ({self.data_type})'
            )

        if self.data_type is None:
            self.data_type = type(value)
        self.array[index] = value

        return self

    def __str__(self):
        return str(self.array)


class StaticArray(BaseArray):
    """
    Mostly here as a educational example of how these tend to be
    different irl. No practical point in implementing this in Python...
    """


class DynamicArray(BaseArray):
    """
    """


arr = BaseArray(10)

arr[3] = 5

print(arr[3])
print(arr[6])