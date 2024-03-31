class Interpreter:
	stack_size = 100
	memory_size = 1000

	def __init__(self, filename, title, commands_memory, debug):
		self.filename = filename
		self.title = title
		self.commands_memory = commands_memory
		self.debug = debug

	def execute(self):
		title = self.title
		commands_memory = self.commands_memory

		ip = 0

		i = 0
		bp = 0
		cx = 0

		buffer = []
		stack = []
		memory = []

		stack = [0] * Interpreter.stack_size
		memory = [0] * Interpreter.memory_size

		ip = title[0]["ENTRY_POINT"]

		while ip < 1000:
			if self.debug == True:
				print(f"[DEBUG] Command: {commands_memory[ip]}")

			if commands_memory[ip] == "+":
				memory[i] += 1
			elif commands_memory[ip] == "+!":
				memory[i] += memory[stack.pop()]
			elif commands_memory[ip] == "-":
				memory[i] -= 1
			elif commands_memory[ip] == "-!":
				memory[i] -= memory[stack.pop()]
			elif commands_memory[ip] == "*":
				memory[i] = memory[i] * memory[i-1]
			elif commands_memory[ip] == "*!":
				memory[i] = memory[i] * memory[stack.pop()]
			elif commands_memory[ip] == "/":
				memory[i] = memory[i] / memory[i-1]
			elif commands_memory[ip] == "/!":
				memory[i] = memory[i] / memory[stack.pop()]
			elif commands_memory[ip] == "^":
				memory[i] = memory[i] ^ memory[i-1]
			elif commands_memory[ip] == "^!":
				memory[i] = memory[i] ^ memory[stack.pop()]
			elif commands_memory[ip] == "?":
				if memory[i] == memory[i-1]:
					memory[i] = 1
				else:
					memory[i] = 0
			elif commands_memory[ip] == "?!":
				if memory[i] == memory[stack.pop()]:
					memory[i] = 1
				else:
					memory[i] = 0
			elif commands_memory[ip] == ">":
				i += 1
			elif commands_memory[ip] == "<":
				i -= 1
			elif commands_memory[ip] == "{":
				if memory[i] == 0:
					count = 1

					while count > 0:
						ip += 1

						if commands_memory[ip] == "{":
							count += 1
						elif commands_memory[ip] == "}":
							count -= 1
					continue
			elif commands_memory[ip] == "}":
				if memory[i] != 0:
					count = 1

					while count > 0:
						ip -= 1

						if commands_memory[ip] == "{":
							count -= 1
						elif commands_memory[ip] == "}":
							count += 1
					continue
			elif commands_memory[ip] == "=":
				memory[i] = memory[i-1]
			elif commands_memory[ip] == "=!":
				memory[stack.pop()] = memory[i]
			elif commands_memory[ip] == "!=":
				memory[i] = memory[stack.pop()]
			elif commands_memory[ip] == "??":
				string = input()

				for char in string:
					buffer.append(char)
			elif commands_memory[ip] == ",":
				memory[i] = buffer[bp]
				bp += 1
			elif commands_memory[ip] == ".":
				char = memory[i]

				print(char, end="")
			elif commands_memory[ip] == "~":
				memory[i] = chr(memory[i])
			elif commands_memory[ip] == "&":
				memory[i] = ord(memory[i])
			elif commands_memory[ip] == "!":
				point_index = memory[i-1]

				ip = title[1]["POINTS"][point_index]["POSITION"]
				continue
			elif commands_memory[ip] == "@":
				stack.append(memory[i])
			elif commands_memory == ":":
				commands_memory[ip][i] = stack.pop()
			elif commands_memory[ip] == ",?":
				memory[i] = len(buffer)
			elif commands_memory[ip] == ":?":
				buffer = []
			elif commands_memory[ip] == "::":
				bp = 0
			elif commands_memory[ip] == "!@":
				cx = memory[i]
			elif commands_memory[ip] == "`":
				memory[i] = 0
			elif commands_memory[ip] == "#":
				exit()

			ip += 1

		return True, None
