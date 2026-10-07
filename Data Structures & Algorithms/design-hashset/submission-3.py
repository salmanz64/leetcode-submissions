class MyHashSet:

    def __init__(self):
        self.val = []
        

    def add(self, key: int) -> None:
        if key in self.val:
            return
        else:
            self.val.append(key)
        

    def remove(self, key: int) -> None:
        if key not in self.val:
            return
        else:
            self.val.remove(key)
        

    def contains(self, key: int) -> bool:
        return ( key in self.val)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)