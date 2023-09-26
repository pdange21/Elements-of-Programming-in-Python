#program to count the number of bits in an integer

def count_bits(num):
    num_bits = 0
    while num:
        num_bits += num & 1
        num >>= 1
    return num_bits

output = count_bits(7)
print(output)
