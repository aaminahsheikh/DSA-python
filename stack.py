# Stack using Arrays.
"""
class Stack:
	def __init__(self):
		self.st = []

	def push(self, val):
		self.st.append(val)
		return 

	def pop(self):
		if self.st:
			return self.st.pop()

	def peak(self):
		if self.st:
			return self.st[-1]

	def get_lenght(self):
		return len(self.st)


stack = Stack()
print(stack.peak())
stack.push(3)
stack.push(67)
stack.push('A')
print(stack.get_lenght())
print(stack.pop())
print(stack.peak())
"""


# Implementing Stack Using Deque Container
from collections import deque

class Stack:
	def __init__(self):
		self.container = deque()

	def push(self, val):
		self.container.appendleft(val)
		return 

	def pop(self):
		if self.container:
			return self.container.popleft()

	def peak(self):
		if self.container:
			return self.container[0]

	def get_length(self):
		return len(self.container)


st = Stack()
st.push(4)
st.push(9)
print(st.peak())
st.pop()
print(st.get_length())
