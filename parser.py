class Parser:
	commands_memory_size = 1000

	execute_direction = "right"

	def __init__(self, filename, code):
		self.filename = filename
		self.code = code

	def parse(self):
		code = self.code
		ip = 0
		allies = False
		allies_cmd = ""
		point_index = 0

		title = [{
			"ENTRY_POINT" : 0
		},
		{
			"POINTS" : []
		}]

		commands_memory = [0] * Parser.commands_memory_size

		for command in code:
			if command == "$":
				table = {
					"ENTRY_POINT" : ip
				}

				title[0].update(table)
				continue
			elif command == "[":
				allies = True
				continue
			elif command != "]" and allies == True:
				allies_cmd += command
				continue
			elif command == "]" and allies == True:
				allies = False
				commands_memory[ip] = allies_cmd
				allies_cmd = ""
			elif command == "_":
				table = {
					"INDEX" : point_index,
					"POSITION" : ip
				}

				title[1]["POINTS"].append(table)
				point_index += 1
				continue
			else:
				commands_memory[ip] = command

			ip += 1

		return title, commands_memory
