import sys

def add_up_2_ints(a : int, b : int) -> int:
	summed_ints = a + b
	print("Ints sum up to a total of:", summed_ints, sep="\t")
	return summed_ints

def main(arg_list : list):
	args = [ int(arg) for arg in arg_list ]
	if len(args) >= 2:
		result = add_up_2_ints(args[0], args[1])


if __name__ == "__main__":
	main(sys.argv[1:])
