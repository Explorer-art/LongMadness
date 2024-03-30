class Decoder:
	def __init__(self, filename, data):
		self.filename = filename
		self.data = data

	def decode(self):
		string = ""
		code = []

		for line in self.data:
			for char in line:
				if char == ";":
					break
				else:
					string += char

			code.append(string)
			string = ""

		return code