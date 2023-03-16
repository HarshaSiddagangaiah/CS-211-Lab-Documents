""" Lab 06 BinaryNumbers
    Harsha Siddagangaiah
"""


class BinaryNumber:

    def __init__(self, bits:list[int]):
        self.bits = bits

    def __str__(self):
        return f"{self.bits}"

    def __or__(self, other):
        bitArray = []
        for i in range(0, len(self.bits)):
            if self.bits[i] == 0 and other.bits[i] == 0:
                bitArray.append(0)
            else:
                bitArray.append(1)
        return BinaryNumber(bitArray)

    def __and__(self, other):
        bitArray = []
        for i in range(0, len(self.bits)):
            if self.bits[i] == 1 and other.bits[i] == 1:
                bitArray.append(1)
            else:
                bitArray.append(0)
        return BinaryNumber(bitArray)

    def left_shift(self):
        self.bits[:-1] = self.bits[1:]
        self.bits[-1] = 0

    def right_shift(self):
        self.bits[1:] = self.bits[:-1]
        self.bits[0] = 0

    def extract(self, start: int, end: int):

        assert 0 <= start < end
        assert start < end <= len(self.bits)

        bitArray = [0] * len(self.bits)
        left = (len(self.bits) - 1) - end
        right = (len(self.bits) - 1) - start

        for i in range(left,right+1):
            bitArray[i] = 1

        b1 = BinaryNumber(bitArray)

        b2 = b1 & self

        for i in range(start):
            b2.right_shift()
        return b2


if __name__ == "__main__":

    bn = BinaryNumber([1, 0, 1, 0, 1])
    bn2 = BinaryNumber([1, 1, 1, 0, 0])
    print("1st binary number =", bn)

    print("2nd binary number =", bn2)

    print("AND", bn & bn2)
    print("OR", bn | bn2)

    bn.right_shift()
    print("1st number right-shifted =", bn)

    bn.left_shift()
    print("1st number left-shifted =", bn)

    bn = BinaryNumber([1, 0, 0, 1, 0, 1, 1, 1])
    extracted = bn.extract(2, 4)
    print(extracted)