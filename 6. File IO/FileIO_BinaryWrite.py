
with open("FileIO_BinaryWrite_Sample", "bw") as binaryWrite:
    for i in range(17):
        binaryWrite.write(bytes([i]))

with open("FileIO_BinaryWrite_Sample", "br") as binaryRead:
    # print(binaryRead.read())
    for data in binaryRead:
        print(data)

print("="*30)

with open("FileIO_BinaryWrite_Sample2", "bw") as binaryWrite:
    for i in range(17):
        binaryWrite.write(i.to_bytes(2, 'big'))

with open("FileIO_BinaryWrite_Sample", "br") as binaryRead:
    # print(binaryRead.read())
    for data in binaryRead.read(2):
        print(int.from_bytes(data, 'big'))

