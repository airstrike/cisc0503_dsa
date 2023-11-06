try:
    from .buffer import BufferArray
except ImportError:
    from buffer import BufferArray

class BufferArrayNoDups(BufferArray):
    def insert(self, value: int) -> bool:
        """Inserts a value into the end of the buffer only if it's not a duplicate.

        Args:
            value (int): The value to insert into the buffer.
        Returns:
            bool: False if we're already at capacity or it's a duplicate, True otherwise.

        """
        if self.locationOf(value) == -1:  # If value already exists, return False.
            return super().insert(value)
        return False


class BufferArrayWithDups(BufferArray):
    def findAll(self, target: int) -> int:
        """Returns the count of occurrences of a value in the buffer.

        Args:
            target (int): The value to find in the buffer.
        Returns:
            int: The number of occurrences of target in the buffer.
        
        """
        count = 0
        for value in self.__intArray:
            if value == target:
                count += 1
        return count

    def fastRemoveAll(self, target: int) -> int:
        """Removes all instances of target from the buffer, replacing them with the last element(s) in the buffer.

        Args:
            target (int): The value to remove from the buffer.
        Returns:
            int: The number of occurrences of target that were removed.

        """
        count = 0
        while self.fastRemove(target):
            count += 1
        return count

    def stableRemoveAll(self, target: int) -> int:
        """Removes all instances of target from the buffer, maintaining the order of the buffer.

        Args:
            target (int): The value to remove from the buffer.
        Returns:
            int: The number of occurrences of target that were removed.

        """
        count = 0
        while self.stableRemove(target):
            count += 1
        return count
