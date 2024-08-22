def findComplement(self, num: int) -> int:
    # Convert the number to binary and remove the '0b' prefix
    binary_num = bin(num)[2:]
    
    # Swap the 0s to 1s and 1s to 0s
    complement = ''.join('1' if bit == '0' else '0' for bit in binary_num)
    
    # Convert the complement binary string back to a decimal integer
    return int(complement, 2)
