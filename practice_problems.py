"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""
#Explanation: I used a set since it will remove all duplicates. Since only the existence of *any* duplicates is returned, and not what those duplicates are, I only compare the length of the original list and the set to avoid any unnecessary comparisons. The expected runtime depends on the size of the list [O(n)] and is bottlenecked by the "set" function.

def has_duplicates(product_ids):
    return len(set(product_ids)) < len(product_ids)#if all IDs are unique, then it will be equal and therefore False, if there are duplicates then the set will be smaller and True


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""
#Explanation: I used a linked list since values are only ever accessed at the ends. I made a simple node class with a value and a pointer to a next node to allow for the creation of a linked list. The list has a head and tail, can add values to the end, and remove values from the beginning. Both operations should function in O(1) time since they only ever swap around pointers.

class Node: #Not explicitly required by assignment but needed for linked list implemenation
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value

class TaskQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_task(self, task):
        new_task = Node(task)

        if self.head == None:
            self.head = new_task
            self.tail = new_task

        else:
            self.tail.next = new_task
            self.tail = new_task

    def remove_oldest_task(self):
        if self.head == None:
            return "No tasks in list"

        else:
            old_head = self.head
            self.head = self.head.next
            return old_head

    def print_list(self): #not required by assignment but useful for testing
        if self.head == None:
            print("Empty List")
        
        else:
            index = 1
            current_node = self.head
            while current_node != None:
                print(f'{index}. - {current_node}')
                current_node = current_node.next
                index = index + 1



"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""
#Explanation: The class essentailly exists as a facade around a normal set. Items are added to the set in O(1) time on average, except when there are hash collisions in which case it is O(n) time. The unique count is returned in O(1) time.
#https://pythoncomplexity.com/builtins/set/

class UniqueTracker:
    def __init__(self):
        self.value_set = set()

    def add(self, value):
        self.value_set.add(value)

    def get_unique_count(self):
        return len(self.value_set)





if __name__ == "__main__":
    Input1 = [10, 20, 30, 20, 40]
    Input2 = [1, 2, 3, 4, 5]
    print("Has duplicates test: ")
    print(f'{Input1} : {has_duplicates(Input1)}')
    print(f'{Input2} : {has_duplicates(Input2)}')
    print("")

    task1 = "Clean dishes"
    task2 = "Vaccum room"
    task3 = "Fold laundry"
    task4 = "Defrost fridge"
    task_test = TaskQueue()

    print("Task Queue tests:")
    task_test.print_list()#printing with 0 values, no previous values
    print("")

    print(task_test.remove_oldest_task())#removing with 0 values, no previous values
    print("")

    task_test.add_task(task1)
    task_test.print_list()#printing 1 value
    print(task_test.remove_oldest_task())#removing with 1 value
    print(task_test.remove_oldest_task())#removing with 0 values
    task_test.print_list()#printing with 0 values
    print("")

    task_test.add_task(task2)
    task_test.add_task(task3)
    task_test.add_task(task4)
    task_test.print_list()#printing 2+ values
    print(task_test.remove_oldest_task())
    print(task_test.remove_oldest_task())
    print(task_test.remove_oldest_task())
    print(task_test.remove_oldest_task())#removing 2+ values
    print("")


    items = [10, 20, 30, 20, 40, 40, 30] #7 items, 4 unique
    tracker = UniqueTracker()
    for item in items:
        tracker.add(item)
    print("Unique Tracker test:")
    print(f'{tracker.get_unique_count()} unique items')

    

