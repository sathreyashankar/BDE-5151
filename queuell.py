class Node:
    def __init__(self,id,name,desc):
        self.id = id
        self.name = name
        self.desc = desc
        self.next = None
    
    
class LL:
    def __init__(self):
        self.head = None
    
    def insert_end(self,id,name,desc):
        n = Node(id,name,desc)
        if not self.head:
            self.head = n
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = n
        
    def delete_front(self):
        if not self.head:
            print("issues empty")
            return
        self.head = self.head.next
        cur = self.head
        while cur:
            print(f"{cur.id} | {cur.name} | {cur.desc}")
            
    def display(self):
         if not self.head:
                    print("issues empty")
                    return
         cur = self.head
         while cur:
             print(f"{cur.id} | {cur.name} | {cur.desc}")
             cur = cur.next
        
        
    def search(self, id):
        if not self.head:
            print("empty")
            return
        cur = self.head
        while cur and cur.id != id :
            cur = cur.next
        if not cur:
            print("not found")
            return
        print(f"{cur.id} | {cur.name} | {cur.desc}")  
        
    def delete(self,id):
        if not self.head:
            print("empty")
            return
        cur, prev= self.head, None
        while cur.id != id and cur:
            prev = cur
            cur = cur.next
        if not cur:
            print("not found")
            return
        if prev:
            prev.next = cur
        else:
            self.head = cur.next
        print("deleted")
        
        
        
ll = LL()
while True:
    ch = input("1 2 3 4 5")
    if ch == "1":
        id = int(input("id:"))
        name = input("name:")
        desc = input("desc:")
        ll.insert_end(id,name,desc)
        
    if ch == "2":
        ll.delete_front() 
    if ch =="3":
        ll.display()
    if ch == "4":
        ll.search(int(input("id:")))
    if ch == "5":
        ll.delete(int(input("id:")))
    if ch == "6":
        break
        