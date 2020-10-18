"""
Project Euler Problem 104: https://projecteuler.net/problem=117

Using a combination of grey square tiles and oblong tiles chosen from: 
red tiles (measuring two units), 
green tiles (measuring three units), and 
blue tiles (measuring four units), 
it is possible to tile a row measuring five units in length in exactly fifteen different ways.


Que. How many ways can a row n units long be filled with:
	 
	 Compute n = 0 manually as a base case.
	 Now assume n >= 1. Look at the leftmost item and sum up the possibilities.
	 - Black square (n>=1): Rest of the row can be anything of length n-1. Add ways[n-1].
	 - Red tile     (n>=2): Rest of the row can be anything of length n-2. Add ways[n-2].
	 - Green tile   (n>=3): Rest of the row can be anything of length n-3. Add ways[n-3].
	 - Blue tile    (n>=4): Rest of the row can be anything of length n-4. Add ways[n-4].
"""

def solution() -> str:
	"""
	>>> solution()
	100808458960497
	"""
	length = 50
	ways = [1] + [0] * length
	for n in range(1, len(ways)):
		ways[n] += sum(ways[max(n - 4, 0) : n])
	return str(ways[-1])

if __name__ == "__main__":
	print(f"{solution()}")
