import sys
INITIAL_CAPACITY = 10**6 * 2
SEPARATOR = "\n"
UNICODE = "utf-8"

class Node(object):
	"""Simple node"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None
	def __str__(self):
		return str(self.value)
	def __repr__(self):
		return str(self)


class HashTable(object):
	"""
	Hash table
	Resolving collisions by separate chaining
	"""
	
	def __init__(self):
		self.capacity = INITIAL_CAPACITY
		self.size = 0
		self.buckets = [None]*self.capacity
	
	
	def hash(self, key):
		"""
		Generate a hash for a given key
		Input:  key - string
		Output: Index from 0 to self.capacity
		"""
		hashsum = 0
		
		for idx, c in enumerate(key):
			hashsum += (idx + len(key)) ** ord(c)
			hashsum = hashsum % self.capacity
		return hashsum

	
	def insert(self, key, value):
		"""
		Insert a key,value pair to the hashtable
		Input:  key - string, value - anything
		Output: void
		"""
		
		self.size += 1
		index = self.hash(key)
		node = self.buckets[index]
		
		if node is None:
			# Create node, add it, return
			self.buckets[index] = Node(key, value)
			return
		# Iterate to the end of the linked list at provided index
		# if already exists replace value
		prev = node
		while node is not None:
			if node.key == key:
				node.value = value
				return
			prev = node
			node = node.next
		# Add a new node at the end of the list with provided key/value
		prev.next = Node(key, value)

	
	def find(self, key):
		"""
		Find a data value based on key
		Input:  key - string
		Output: value stored under "key" or nothing if not found
		"""
		
		index = self.hash(key)
		
		node = self.buckets[index]
		
		while node is not None and node.key != key:
			node = node.next
		
		if node is None:
			# Not found
			return "none"
		else:
			# Found - return the data value
			return node.value

	
	def remove(self, key):
		"""
		Remove node stored at key
		Input:  key - string
		Output: removed data value or None if not found
		"""
		
		index = self.hash(key)
		node = self.buckets[index]
		prev = None
		
		while node is not None and node.key != key:
			prev = node
			node = node.next
		# Now, node is either the requested node or none
		if node is None:
			# 3. Key not found
			return None
		else:
			# 4. The key was found.
			self.size -= 1
			result = node.value
			# Delete this element in linked list
			if prev is None:
				self.buckets[index] = node.next # May be None, or the next match
			else:
				prev.next = prev.next.next # LinkedList delete by skipping over
			# Return the deleted result 
			return result


############ ---- Main Block ---- ############

def solve():
    map_object = HashTable()
    data = sys.stdin.buffer.readlines()
    result_exists = []
    n_operations = len(data)
    for i in range(n_operations):
        command = str(data[i].decode(UNICODE))[:-1].split()

        if command[0] == "put":
            map_object.insert(str(command[1]), str(command[2]))
        elif command[0] == "get":
            result_exists.append(map_object.find(str(command[1])))
        elif command[0] == "delete":
            map_object.remove(str(command[1]))

        

    encoded_array = (SEPARATOR.join(result_exists)).encode(UNICODE)
    sys.stdout.buffer.write(encoded_array)


if __name__ == "__main__":
    solve()