# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# Ryan Earl
class LinkedList:
    def __init__(self, value=None):
        self.value = value
        self.next= self
        self.prev = self
        
    
    def is_sentinel(self):
        if self.value == None:
            return True

    def is_empty(self):
        return self.prev == self and self.next == self
            

    def is_last(self): 
        return self.next.value is None

    def last(self):
        return self.prev

    def append(self, appends): 
        self.prev.next = appends
        appends.prev = self.prev
        self.prev = appends
        appends.next = self

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev

    def insert (self, inserts): 
        inserts.prev  = self
        inserts.next = self.next
        self.next.prev = inserts
        self.next = inserts

    def at(self, N): 
        if (N==0): 
            return self
        return self.next.at(N-1)

    def search(self, value): 
        if self.value == value: 
            return self
        elif self.next.value is None: 
            return None
        return self.next.search(value) 

    def insert_in_order(self, inserts): 