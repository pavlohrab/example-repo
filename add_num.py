import sys

def main(a : int, b : int) -> int:
	summed_ints = a + b
	print("Ints sum up to a total of:", summed_ints, sep="\t")
	return summed_ints


args = [ int(arg) for arg in sys.argv[1:] ]
if len(args) >= 2:
	result = main(args[0], args[1])

