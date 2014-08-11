#!/usr/bin/env python

def PrintUsage(quitwith=-1): 
    from sys import stderr
    stderr.write("""\
Calculates the SHA-1 sum of a given file (optionally with custom constants)
Usage: 
       ./sha1mod.py <filename> [<K0> <K1> <K2> <K3>]
Examples:
       ./sha1mod.py file0.bin
       ./sha1mod.py file0.bin 5A827999 6ED9EBA1 8F1BBCDC CA62C1D6
""")
    quit(quitwith)

########################################################################

SHA1IV  = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]

SHA1K = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6]


def rotl(word, offset):
    return ((word << offset) | (word >> (32 - offset))) & 0xffffffff

def int2bytes(data, length=1):
    return bytes(bytearray(reversed([(data >> i*8) % 256 for i in range(length)])))

def bytes2int(data):
    return sum([ord(bi) << ((len(data) - 1 - i)*8) for i, bi in enumerate(data)])


def SHA1(filename, IV = SHA1IV, K = SHA1K):
    with open(filename, "rb") as f:
        message = f.read()

        # message padding
        # append 0x8000...00 and the msg bitlen (as 8 big-endian bytes) to fill up to a multiple of 512 bits
        message += b"\x80" + b"\x00" * ((56 - len(message) - 1) % 64) + int2bytes(len(message)*8, length=8)

        # initialize chaining value
        h0, h1, h2, h3, h4 = IV
        
        # process message in blocks of 64 bytes (or 16 words a 32 bits)
        for i in range(0, len(message), 64):
            # extend 16 message words to 80 words, one for each round
            w = [None] * 80
            for j in range(16):
                w[j] = bytes2int(message[i+4*j:i+4*(j+1)])
            for j in range(16, 80):
                w[j] = rotl(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)
        
            # initialize state to chaining value
            a, b, c, d, e = h0, h1, h2, h3, h4
        
            # update state in 80 rounds
            for j in range(80):
                if 0 <= j < 20:
                    f = d ^ (b & (c ^ d))
                    k = K[0]
                elif 20 <= j < 40:
                    f = b ^ c ^ d
                    k = K[1]
                elif 40 <= j < 60:
                    f = (b & c) | (b & d) | (c & d)
                    k = K[2]
                elif 60 <= j < 80:
                    f = b ^ c ^ d
                    k = K[3]
       
                a, b, c, d, e = (rotl(a, 5) + f + e + k + w[j]) & 0xffffffff, a, rotl(b, 30), c, d
        
            # update chaining value with state
            h0 = (h0 + a) & 0xffffffff
            h1 = (h1 + b) & 0xffffffff
            h2 = (h2 + c) & 0xffffffff
            h3 = (h3 + d) & 0xffffffff
            h4 = (h4 + e) & 0xffffffff
    
    # return last chaining value as hash
    return "{h0:08X} {h1:08X} {h2:08X} {h3:08X} {h4:08X}".format(**locals())

########################################################################

if __name__ == "__main__":
    from sys import argv
    import math

    if len(argv) == 2:
        print SHA1(argv[1])
    elif len(argv) == 6:
        print SHA1(argv[1], K=[int(argv[i],16) for i in range(2,6)])
    else:
        PrintUsage()
