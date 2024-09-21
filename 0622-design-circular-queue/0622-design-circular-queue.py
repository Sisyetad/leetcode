class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = []
        self.count = 0
        

    def enQueue(self, value: int) -> bool:
        if self.count <self.k:
            self.count += 1
            self.queue.append(value)
            return True

    def deQueue(self) -> bool:
        if self.count > 0:
            self.count-=1
            self.queue.pop(0)
            return True
        
    def Front(self) -> int:
        if self.count!=0:
            return self.queue[0]
        return -1

    def Rear(self) -> int:
        if self.count!=0:
            return self.queue[self.count-1]
        return -1
        

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        return False
        

    def isFull(self) -> bool:
        if self.count == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
