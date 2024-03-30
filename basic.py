class Error:
	def __inif__(self, error_name, details, filename, line):
		self.error_name = error_name
		self.details = details
		self.filename = filename
		self.line = line

	def get_string(self):
		result = f"{error_name}: {details}\n"
		result += f"File: {filename}, line: {line}"
		return result