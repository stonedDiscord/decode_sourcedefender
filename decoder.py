import sys
from base64 import a85decode
from zlib import decompress
from tgcrypto import ctr256_decrypt


infile = sys.argv[1]
f = open(infile, 'r', encoding='utf-8')
encrypted = f.read()
f.close()
encrypted = encrypted.replace("-----BEGIN SOURCEDEFENDER FILE-----","")
encrypted = encrypted.replace("------END SOURCEDEFENDER FILE------","")
stripped = encrypted.replace(" ","")
stripped = stripped.replace("\n","")
stripped = stripped.replace("\n","")

decoded = a85decode(stripped)
print(decoded)

key = bytes(32)
iv = bytes(16)
state = bytes(1)

#decoded= ctr256_decrypt(decoded, key, iv, state)
#print(decrypted)

nf = open(infile + ".bin", "wb")
nf.write(decoded)
nf.close()

#decompressed = decompress(decoded)
#print(decompressed)