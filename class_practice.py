class Vehicle:
	#attributes
	name = ""
	kind = ""
	color = ""

	#init automatically runs every time 
	# def __init__(self, name, kind, color):
	# 	self.name = name
	# 	self.kind = kind
	# 	self.color = color

	#method
	def description(self):
		print("My name:", self.name)
		print("My kind:", self.kind)
		print("My color:", self.color)


#slow way: 

toyota = Vehicle()
toyota.name = "Pet Toyota"
toyota.kind = "4 wheel drive"
toyota.color = "Magenta"

# toyota.description()


#better way to instantiate: 

# toyota = Vehicle("Pet Toyota", "4 wheel drive", "Magenta")
# toyota.description()

#create another instance of a Vehicle here: 