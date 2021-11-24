class OutOfIndex(IndexError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Stack:
    def __init__(self) -> None:
        self.__stack_list = []

    def push(self, val)->None:
        """
        Adds new value to the stack
        """
        self.__stack_list.append(val)

    def pop(self)-> None:
        """
        Removes and returns top one value from the stack
        """
        try:
            return self.__delete()
        except IndexError:
            raise OutOfIndex("Stack empty")


    def getActual(self)->any:
        """
        Returns last added value
        """
        return self.__getAny(-1)

    # PRIVATE #

    def __getAny(self, index):
        return self.__stack_list[index]
    
    def __delete(self, index = -1):
        """
        Takes specified index (default last [-1]), removes and returns it
        """
        tmp = self.__stack_list[index]
        del self.__stack_list[index]

        return tmp

class CountingStack(Stack):
    """
    Stack modifier that counts number of pops
    """

    def __init__(self) -> None:
        Stack.__init__(self)
        self.__counter = 0
    
    def get_counter(self):
        """
        Returns number of pops
        """
        return self.__counter

    def pop(self):
        """
        Modified POP function of stack
        raises counter value by each pop
        """
        tmp = Stack.pop(self)
        self.__counter += 1
        return tmp

    

stack1 = CountingStack()

stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)

try:
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
    print(stack1.pop())
except AttributeError:
    print("You've probably used wrong stack class")
except OutOfIndex:
    print("There are no elements in the stack that could be removed.")

print("Totally poped:", stack1.get_counter())