#Queue as a class.
class QueueForPalindrome: # pragma: no cover
    """ From the provided Que_List.py file """
    def __init__(self):
        self.__elements = []
        
     # Return true if queue is empty 
    def is_empty(self):
        return len(self.__elements) == 0

    def isEmpty(self): # pragma: no cover
        return self.is_empty()

    # Adds an element to this queue
    def enqueue(self, e):
        self.__elements.append(e)

    def enque(self, e): # pragma: no cover
        return self.enqueue(e)
    
    # Removes an element from this queue
    def dequeue(self):
        if self.getSize() == 0:
            return None
        else:
            return self.__elements.remove(self.__elements[0])

    def deque(self): # pragma: no cover
        return self.dequeue()

    def get_size(self):
        return len(self.__elements)
    
    # Return the size of the queue
    def getSize(self):
        return self.get_size()
    
    # Returns a string representation of the queue
    def __str__(self):
        ret_str = " "
        for i in range( len(self.__elements) ):
             ret_str += str(self.__elements[i]) + " "
        ret_str +="\n"
        return ret_str

    
#Stack as a class.
class StackForPalindrome: # pragma: no cover
    """ From the provided Stack_List.py file """
    def __init__(self):
        self.__elements = []

    # Return true if the stack is empty
    def is_empty(self):
        return len(self.__elements) == 0

    def isEmpty(self):
        return self.is_empty()
    
    # Returns the element at the top of the stack 
    # without removing it from the stack.
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.__elements[len(self.__elements) - 1]

    # Stores an element into the top of the stack
    def push(self, value):
        self.__elements.append(value)

    # Removes the element at the top of the stack and returns it
    def pop(self):
        if self.isEmpty():
            return None
        else:
            del( self.__elements[len(self.__elements) - 1]) 
            return self.__elements
        
    # Old pop method, not used
    # def _pop(self): # pragma: no cover
    #     if self.isEmpty():
    #         return None
    #     else:
    #         return self.__elements.remove(self.__elements[len(self.__elements) - 1])
    
    # Return the size of the stack
    def getSize(self):
        return len(self.__elements)

    def __str__( self ):
         ret_str = " "
         for i in range( len(self.__elements) ):
            ret_str += str(self.__elements[i]) + " "
         ret_str +="\n"
         return ret_str
