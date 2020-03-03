#Yanira Manzano
#3/3/2020

def remove_head(self):
        self.head = self.head.next
        self.head.previous = None

    def remove_end(self):
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        remove = self.head
        while current.next:
            current = current.next
            remove.next = None
