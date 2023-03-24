# Implement Queue using Array DS.
"""
class Queue:
	def __init__(self):
		self.container = []

	def enqueue(self, val):
		self.container.insert(0, val)
		return 

	def dequeue(self):
		if self.container: 
			return self.container.pop()

	def front(self):
		if self.container:
			return self.container[-1]

	def get_lenght(self):
		return len(self.container)


q = Queue()
q.enqueue(3)
q.enqueue(90)
q.enqueue('A')
print(q.get_lenght())
print(q.front())
print(q.dequeue())
print(q.get_lenght())
print(q.front())
"""

# Implementing Queue using deque container.
from collections import deque

class Queue:
	def __init__(self):
		self.container = deque()

	def enqueue(self, val):
		self.container.appendleft(val)
		return 

	def dequeue(self):
		if self.container:
			return self.container.pop()

	def front(self):
		if self.container:
			return self.container[-1]

	def get_lenght(self):
		return len(self.container)


que = Queue()
que.enqueue(8)
que.enqueue(40)
que.enqueue('A')
print(que.get_lenght())
que.dequeue()
print(que.front())
print(que.get_lenght())