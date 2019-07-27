#swap 8 bit integer
def swap_bits(x):
	EVEN =0b10101010
	ODD = 0b01010101

	return (x & EVEN) >> 1 | (x & ODD) << 1


print swap_bits(1)
print swap_bits(2)
print swap_bits(3)
print swap_bits(4)
print swap_bits(8)
print swap_bits(9)

