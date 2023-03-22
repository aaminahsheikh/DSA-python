class  Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LL:
    def __init__(self, data):
        self.head = Node(data)

    def at_head(self, data):
        if not self.head: return Node(data)

        self.head = Node(data, self.head)

    def at_tail(self, data):
        if not self.head: return Node(data)

        itr = self.head 
        while itr.next:
            itr = itr.next

        itr.next = Node(data)
        return 

    def get_len(self):
        if not self.head: return 0

        itr = self.head 
        cnt = 0
        while itr:
            cnt += 1
            itr = itr.next

        return cnt

    def delete_node(self, data):
        if not self.head: return

        if self.head.val == data:
            self.head = self.head.next
            return

        itr = self.head 
        while itr.next:
            if itr.next.val == data:
                itr.next = itr.next.next
                return
            itr = itr.next

    def search_by_val(self, data):
        if self.head is None: return 

        itr = self.head 
        while itr:
            if itr.val == data:
                return True
            itr = itr.next

        return False

    def reverse(self):
        if not self.head: return

        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev


    def print_ll(self):
        if not self.head: return
        nodes = ''
        itr = self.head
        while itr:
            nodes += str(itr.val)
            nodes += '-->'
            itr = itr.next

        print(nodes)

ll = LL(2)
ll.at_head(5)
ll.at_tail(8)
ll.at_head('A')
ll.delete_node(2)
ll.delete_node('A')
ll.print_ll()
ll.reverse()
ll.print_ll()
print(ll.search_by_val(82))
print(ll.get_len())