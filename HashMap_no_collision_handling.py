# HashMap implementation in Python without collision handling.

class HashMap:
	def __init__(self):
		self.MAX = 100
		self.arr = [None for i in range(self.MAX)]


	def get_hash(self, key):
		h = 0
		key = str(key)
		for char in key:
			h += ord(char)

		return h%100

	def __setitem__(self, key, val):
		h = self.get_hash(key)
		self.arr[h] = val

	def __getitem__(self, key):
		h = self.get_hash(key)
		return self.arr[h]

	def __delitem__(self, key):
		h = self.get_hash(key)
		self.arr[h] = None


h = HashMap()
h["march 9"] = 123
h["march 6"] = 66
h[1] = 12
del h["march 6"]
print(h["march 6"])
print(h.arr[49])

