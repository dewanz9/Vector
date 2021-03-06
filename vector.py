from math import sqrt

class Vector(object):
	"""the vector class
	methods:
		getMagnitude()
		setMagnitude(value)
		getDirection()
		setDirection(value)
		__init__(self, x, y, z)
		cross(vector2)
		multiply(vector2)
		add(vector2)
		subtract(vector2)
		dot_product(vector2)
	variables:
		x_component
		y_component
		z_component"""
	def __init__(self, x, y, z):
		"""initializer function for the vector class
		inputs:
			x: x component
			y: y component
			z: z component"""
		self.x_component = x
		self.y_component = y
		self.z_component = z
	
	def getMagnitude(self):
		"""returns the magnitude of the vector
		outputs:
			magnitude: sqrt(x^2+y^2+z^2)"""
		sums = self.x_component**2+self.y_component**2+self.z_component**2
		return sqrt(sums)
	def getDirection(self):
		"""returns the unit vector of the direction of the vector
		outputs:
			direction"""
		return Vector(self.x_component/self.getMagnitude(), 
			      self.y_component/self.getMagnitude(),
			      self.z_component/self.getMagnitude())
	
	def setMagnitude(self, value):
		"""sets the vector to a given magnitude preserving direction
		inputs:
			value"""
		direction = self.getDirection()
		self.x_component = direction.x_component * value
		self.y_component = direction.y_component * value
		self.z_component = direction.z_component * value

	def show_values(self):
		"""prints the components"""
		print(self.x_component)
		print(self.y_component)
		print(self.z_component)
