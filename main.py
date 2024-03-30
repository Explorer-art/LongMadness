import os
import sys
from basic import *
from decoder import *
from parser import *
from interpreter import *

debug = False

def main():
	filename = sys.argv[1]
	file = open(filename, "r")
	data = file.readlines()
	file.close()

	decoder = Decoder(filename, data)
	code = decoder.decode()

	parser = Parser(filename, code)
	title, commands_memory = parser.parse()

	interpreter = Interpreter(filename, title, commands_memory, debug)

	ok, err = interpreter.execute()

if __name__ == "__main__":
	main()