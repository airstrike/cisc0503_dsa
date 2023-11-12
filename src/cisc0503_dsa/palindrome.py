#Queue as a class.

class Queue:
    def __init__(self):
        self.__elements = []
        
     # Return true if queue is empty 
    def isEmpty(self):
        return len(self.__elements) == 0

    # Adds an element to this queue
    def enque(self, e):
        self.__elements.append(e)
    
    # Removes an element from this queue
    def deque(self):
        if self.getSize() == 0:
            return None
        else:
            return self.__elements.remove( self.__elements[0] )
    
    # Return the size of the queue
    def getSize(self):
        return len(self.__elements) 
    
    # Returns a string representation of the queue
    def __str__(self):
        ret_str = " "
        for i in range( len(self.__elements) ):
             ret_str += str(self.__elements[i]) + " "
        ret_str +="\n"
        return ret_str

    
#Stack as a class.

class Stack:
    def __init__(self):
        self.__elements = []

    # Return true if the stack is empty
    def isEmpty(self):
        return len(self.__elements) == 0
    
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
    
    # Return the size of the stack
    def getSize(self):
        return len(self.__elements)

    def __str__( self ):
         ret_str = " "
         for i in range( len(self.__elements) ):
            ret_str += str(self.__elements[i]) + " "
         ret_str +="\n"
         return ret_str
