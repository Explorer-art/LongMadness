class Parser:
	number_cols = 1000
	number_rows = 10

	execute_direction = "right"

	def __init__(self, filename, code):
		self.filename = filename
		self.code = code

	def parse(self):
		code = self.code
		x = 0
		y = 0
		allies = False
		allies_cmd = ""
		point_index = 0

		title = [{
			"ENTRY_POINT" : []
		},
		{
			"EXECUTE_DIRECTION" : ""
		},
		{
			"POINTS" : []
		}]

		commands_memory = [[0] * Parser.number_cols for i in range(Parser.number_rows)]

		for commands in code:
			for command in commands:
				if command == "$":
					table = {
						"ENTRY_POINT" : [x, y]
					}

					title[0].update(table)

					table = {
						"EXECUTE_DIRECTION" : Parser.execute_direction
					}

					title[1].update(table)
				
				if command == "[":
					allies = True
					continue
				elif command != "]" and allies == True:
					allies_cmd += command
					continue
				elif command == "]" and allies == True:
					allies = False
					commands_memory[y][x] = allies_cmd
					allies_cmd = ""
				elif command == "_":
					table = {
						"INDEX" : point_index,
						"POSITION" : [x, y]
					}

					title[2]["POINTS"].append(table)
					point_index += 1
					continue
				else:
					commands_memory[y][x] = command

				x += 1
			y += 1

		return title, commands_memory