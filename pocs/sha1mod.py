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

def SHA1(filename, IV = SHA1IV, K = SHA1K):
  import struct
  with open(filename, "rb") as f:
    message = f.read()
    # SHA1 implementation adapted from https://github.com/ajalt/python-sha1/blob/master/sha1.py

    def _left_rotate(n, b):
      return ((n << b) | (n >> (32 - b))) & 0xffffffff
    # Initialize variables:
    h0, h1, h2, h3, h4 = IV
    # Pre-processing:
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    # append the bit '1' to the message
    message += b'\x80'
    
    # append 0 <= k < 512 bits '0', so that the resulting message length (in bits)
    # is congruent to 448 (mod 512)
    message += b'\x00' * ((56 - (original_byte_len + 1) % 64) % 64)
    
    # append length of message (before pre-processing), in bits, as 64-bit big-endian integer
    message += struct.pack(b'>Q', original_bit_len)
    # Process the message in successive 512-bit chunks:
    # break message into 512-bit chunks
    for i in range(0, len(message), 64):
        w = [0] * 80
        # break chunk into sixteen 32-bit big-endian words w[i]
        for j in range(16):
            w[j] = struct.unpack(b'>I', message[i + j*4:i + j*4 + 4])[0]
        # Extend the sixteen 32-bit words into eighty 32-bit words:
        for j in range(16, 80):
            w[j] = _left_rotate(w[j-3] ^ w[j-8] ^ w[j-14] ^ w[j-16], 1)
    
        # Initialize hash value for this chunk:
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
    
        for i in range(80):
            if 0 <= i <= 19:
                # Use alternative 1 for f from FIPS PB 180-1 to avoid ~
                f = d ^ (b & (c ^ d))
                k = K[0]
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = K[1]
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = K[2]
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = K[3]
   
            a, b, c, d, e = ((_left_rotate(a, 5) + f + e + k + w[i]) & 0xffffffff,
                            a, _left_rotate(b, 30), c, d)
    
        # sAdd this chunk's hash to result so far:
        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff
    
    # Produce the final hash value (big-endian):
    return '%08X %08X %08X %08X %08X' % (h0, h1, h2, h3, h4)

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
