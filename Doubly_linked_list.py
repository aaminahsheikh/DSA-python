# Doubly linked list in Python.

class Node:
	def __init__(self, val, next=None, prev=None):
		self.val = val
		self.next = next
		self.prev = prev

class DLL:
	def __init__(self, data):
		self.head = Node(data)

	def at_tail(self, data):
		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next = Node(data)
		itr.next.prev = itr
		return

	def print_list(self):
		itr = self.head
		res1 = ''

		while itr.next:
			res1 += str(itr.val)
			res1 += '-->'
			itr = itr.next
		res1 += str(itr.val)
		res1 += 'None'

		res2 = str(itr.val)
		while itr.prev:
			res2 += '<--'
			res2 += str(itr.prev.val)
			itr = itr.prev
		
		res2 += '<--' + 'None'
		print(res1)
		print(res2)

	def del_node_val(self, data):
		if self.head.val == data:
			self.head = self.head.next
			self.head.prev = None
			return

		itr = self.head
		while itr.next:
			if itr.next.val == data:
				itr.next = itr.next.next
				if itr.next:
					itr.next.prev = itr
				return
			itr = itr.next
		return

dll = DLL(1)
dll.at_tail(2)
dll.at_tail(3)
dll.at_tail(4)

dll.print_list()


dll.del_node_val(3)
dll.del_node_val(2)
dll.print_list()

