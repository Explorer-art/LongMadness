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

		x = 0
		y = 0

		ip = 0
		bp = 0
		zf = 0
		cx = 0

		buffer = []
		stack = []
		memory = []

		for i in range(Interpreter.stack_size):
			stack.append(0)

		for i in range(Interpreter.memory_size):
			memory.append(0)

		x = title[0]["ENTRY_POINT"][0]
		y = title[0]["ENTRY_POINT"][1]

		while y < 1000 and x < 1000:
			if self.debug == True:
				print(f"[DEBUG] Command: {commands_memory[y][x]}")

			if commands_memory[y][x] == "+":
				memory[ip] += 1
			elif commands_memory[y][x] == "+!":
				memory[ip] += memory[stack.pop()]
			elif commands_memory[y][x] == "-":
				memory[ip] -= 1
			elif commands_memory[y][x] == "-!":
				memory[ip] -= memory[stack.pop()]
			elif commands_memory[y][x] == "*":
				memory[ip] = memory[ip] * memory[ip-1]
			elif commands_memory[y][x] == "*!":
				memory[ip] = memory[ip] * memory[stack.pop()]
			elif commands_memory[y][x] == "/":
				memory[ip] = memory[ip] / memory[ip-1]
			elif commands_memory[y][x] == "/!":
				memory[ip] = memory[ip] / memory[stack.pop()]
			elif commands_memory[y][x] == "^":
				memory[ip] = memory[ip] ^ memory[ip-1]
			elif commands_memory[y][x] == "^!":
				memory[ip] = memory[ip] ^ memory[stack.pop()]
			elif commands_memory[y][x] == "?":
				if memory[ip] == memory[ip-1]:
					zf = 1
				else:
					zf = 0
			elif commands_memory[y][x] == "?!":
				if memory[ip] == memory[stack.pop()]:
					zf = 1
				else:
					zf = 0
			elif commands_memory[y][x] == ">":
				ip += 1
			elif commands_memory[y][x] == "<":
				ip -= 1
			elif commands_memory[y][x] == "=":
				memory[ip] = memory[ip-1]
			elif commands_memory[y][x] == "=!":
				memory[stack.pop()] = memory[ip]
			elif commands_memory[y][x] == "!=":
				memory[ip] = memory[stack.pop()]
			elif commands_memory[y][x] == "->":
				title[1]["EXECUTE_DIRECTION"] = "right"
				continue
			elif commands_memory[y][x] == "<-":
				title[1]["EXECUTE_DIRECTION"] = "left"
				continue
			elif commands_memory[y][x] == "^-":
				title[1]["EXECUTE_DIRECTION"] = "top"
				continue
			elif commands_memory[y][x] == "v-":
				title[1]["EXECUTE_DIRECTION"] = "down"
				continue
			elif commands_memory[y][x] == "\\":
				x = 0
				y += 1
				continue
			elif commands_memory[y][x] == "|":
				if cx != 0:
					cx -= 1

					point_index = memory[ip-1]

					x = title[2]["POINTS"][point_index]["POSITION"][0]
					y = title[2]["POINTS"][point_index]["POSITION"][1]
					continue
			elif commands_memory[y][x] == "{":
				if zf == 0:
					point_index = memory[ip-1]

					x = title[2]["POINTS"][point_index]["POSITION"][0]
					y = title[2]["POINTS"][point_index]["POSITION"][1]
					continue
			elif commands_memory[y][x] == "}":
				if zf == 1:
					point_index = memory[ip-1]

					x = title[2]["POINTS"][point_index]["POSITION"][0]
					y = title[2]["POINTS"][point_index]["POSITION"][1]
					continue
			elif commands_memory[y][x] == "!!":
				string = stack.pop()

				print(string)
			elif commands_memory[y][x] == "??":
				string = input()

				for char in string:
					buffer.append(char)
			elif commands_memory[y][x] == ",":
				memory[ip] = buffer[bp]
				bp += 1
			elif commands_memory[y][x] == ".":
				char = memory[ip]

				print(char, end="")
			elif commands_memory[y][x] == "!>":
				memory[ip] = chr(memory[ip])
			elif commands_memory[y][x] == "+>":
				memory[ip] = ord(memory[ip])
			elif commands_memory[y][x] == "!":
				point_index = memory[ip-1]

				x = title[2]["POINTS"][point_index]["POSITION"][0]
				y = title[2]["POINTS"][point_index]["POSITION"][1]
				continue
			elif commands_memory[y][x] == "@":
				stack.append(memory[ip])
			elif commands_memory == ":":
				commands_memory[y][x][ip] = stack.pop()
			elif commands_memory[y][x] == ",?":
				memory[ip] = len(buffer)
			elif commands_memory[y][x] == ":?":
				buffer = []
			elif commands_memory[y][x] == "::":
				bp = 0
			elif commands_memory[y][x] == "!@":
				cx = memory[ip]
			elif commands_memory[y][x] == "#":
				exit()

			if title[1]["EXECUTE_DIRECTION"] == "right":
				x += 1
			elif title[1]["EXECUTE_DIRECTION"] == "left":
				x -= 1
			elif title[1]["EXECUTE_DIRECTION"] == "top":
				y -= 1
			elif title[1]["EXECUTE_DIRECTION"] == "down":
				y += 1

		return True, None