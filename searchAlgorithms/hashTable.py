# This is supposed to be a hash table

import time

start_time = time.time()

class HashMap:
	def __init__(self):
		self.size = 10000
		self.map = [None] * self.size
		
	def _get_hash(self, key):
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash % self.size
		
	def add(self, key, value):
		key_hash = self._get_hash(key)
		key_value = [key, value]
		
		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True
		else:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] = value
					return True
			self.map[key_hash].append(key_value)
			return True
			
	def get(self, key):
		key_hash = self._get_hash(key)
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None
			
	def delete(self, key):
		key_hash = self._get_hash(key)
		
		if self.map[key_hash] is None:
			return False
		for i in range (0, len(self.map[key_hash])):
			if self.map[key_hash][i][0] == key:
				self.map[key_hash].pop(i)
				return True
		return False
			
	def print(self):
		for item in self.map:
			if item is not None:
				print(str(item))
				
h = HashMap()
h.add(99, "ninty nine")
h.add(320, "three hundred twenty")
h.add(51, "fifty one")
h.add(827, "eight hundred twenty seven")
h.add(4, "four")
h.add(121, "one hundred twenty one")

h.print()
print(h.get(320))

print((time.time() - start_time))



