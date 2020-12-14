class myStack:
	def create_stack():
		s = []
		return s

	def __init__(self):
		self.elements = []

	def push(self, element):
		self.elements.append(element)

	def remove(self):
		return self.elements.pop()

	def is_empty(self):
		if not self.elements:
			return True
		else:
			return False

