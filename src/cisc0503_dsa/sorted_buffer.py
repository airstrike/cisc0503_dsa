try:
    from .buffer import BufferArray
    from .buffer_ext import BufferArrayNoDups, BufferArrayWithDups
except ImportError: # pragma: no cover
    from buffer import BufferArray
    from buffer_ext import BufferArrayNoDups, BufferArrayWithDups

class SortedBufferArrayNoDups(BufferArrayNoDups):
    def locationOf(self, target: int) -> int:
        """Returns the index of a value in the sorted buffer.

        Args:
            target (int): The value to find in the sorted buffer.
        Returns:
            int: The index of target in the buffer, or -1 if not found.
        
        """
        for i in range(self._BufferArray__numberOfElements):
            if self._BufferArray__intArray[i] == target:
                return i
            if self._BufferArray__intArray[i] > target:
                return -1
        return -1

    def insert(self, value: int) -> bool:
        """Inserts a value into the right place in the buffer only if it's not a duplicate.

        Args:
            value (int): The value to insert into the buffer.
        Returns:
            bool: False if we're already at capacity or it's a duplicate, True otherwise.

        """
        # If we're already at capacity, return False.
        if self._BufferArray__numberOfElements == self._BufferArray__BUFFER_SIZE:
            return False

        # If the value is already in the buffer, return False.
        if self.locationOf(value) != -1:
            return False

        # Otherwise, insert the value into the buffer into the right position.
        # Use binary search to find the right place to insert the value.
        low, high = 0, self._BufferArray__numberOfElements - 1
        while low <= high:
            mid = (low + high) // 2
            if self._BufferArray__intArray[mid] < value:
                low = mid + 1
            else:
                high = mid - 1

        # At this point, 'low' is the right position to insert the new value.
        # Shift all elements from 'low' to the right by one position.
        for i in range(self._BufferArray__numberOfElements, low, -1):
            self._BufferArray__intArray[i] = self._BufferArray__intArray[i-1]

        # Insert the new value.
        self._BufferArray__intArray[low] = value
        self._BufferArray__numberOfElements += 1
        return True

    def fastRemove(self, value):
        raise NotImplementedError("Cannot use fastRemove on a sorted buffer.")

    def stableRemove(self, value: int) -> bool:
        """
        Removes the target from the buffer if present, maintaining the order of the buffer.

        Args:
            target (int): The value to remove from the buffer.
        Returns:
            bool: True if target was found and removed, False otherwise.

        """
        # There is no need to reimplement this method since the parent class's behavior
        # already leverages .locationOf(), which we have implemented above to behave
        # as needed for a sorted buffer.
        return super().stableRemove(value)

class SortedBufferArrayWithDups(SortedBufferArrayNoDups):
    def insert(self, value: int) -> bool:
        """Inserts a value into the right place in the buffer.

        Args:
            value (int): The value to insert into the buffer.
        Returns:
            bool: False if we're already at capacity, True otherwise.

        """
        # If we're already at capacity, return False.
        if self._BufferArray__numberOfElements == self._BufferArray__BUFFER_SIZE:
            return False

        # Use binary search to find the right place to insert the value.
        low, high = 0, self._BufferArray__numberOfElements - 1
        while low <= high:
            mid = (low + high) // 2
            if self._BufferArray__intArray[mid] < value:
                low = mid + 1
            else:
                high = mid - 1

        # At this point, 'low' is the right position to insert the new value.
        # Shift all elements from 'low' to the right by one position.
        for i in range(self._BufferArray__numberOfElements, low, -1):
            self._BufferArray__intArray[i] = self._BufferArray__intArray[i-1]

        # Insert the new value.
        self._BufferArray__intArray[low] = value
        self._BufferArray__numberOfElements += 1
        return True

    def findAll(self, target: int) -> int:
        """Returns the number of occurrences of the target value."""
        count = 0
        for i in range(self._BufferArray__numberOfElements):
            if self._BufferArray__intArray[i] == target:
                count += 1
            elif self._BufferArray__intArray[i] > target:
                break
        return count

    def stableRemoveAll(self, target: int) -> int:
        """Removes all occurrences of the target value and returns the number of values removed."""
        start_index = self.locationOf(target)
        if start_index == -1:
            return 0

        count = self.findAll(target)
        for i in range(start_index, self._BufferArray__numberOfElements - count):
            self._BufferArray__intArray[i] = self._BufferArray__intArray[i + count]

        self._BufferArray__numberOfElements -= count
        return count
