arr = bytearray([1,2,5])
b_arr = bytes(arr)

with open("test.bin", "wb") as f:
    f.write(b_arr)