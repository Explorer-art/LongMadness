class Decoder:
	def __init__(self, filename, data):
		self.filename = filename
		self.data = data

	def decode(self):
		data = self.data
		code = ""

		for line in data:
			for char in line:
				if char == ";":
					break
				elif char == " ":
					continue
				elif char == "\t":
					continue
				elif char == "\n":
					continue

				code += char

		return code
