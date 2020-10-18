# github: ivanprfbs | ivanantonino.arena@studenti.unipd.it
# calculates memory address bits given memory size, cache size, block size, mapping

print("\nThis program will calculate the number of bits of some internal storage.")
print("All you need is to insert memory size, cache size and block size.\n")
print("!: Please be sure to format in powers of two (Es.: 64 = 2^6 => '6')\n")

# prompts for data
memsize = int(input('Memory size: 2^'))
cachesize = int(input('Cache size: 2^'))
blocksize = int(input('Block size: 2^'))

# calculate variables
words = blocksize
nlines = cachesize - blocksize

# prompts for mapping technique (case insensitive)
print("\nNow choose a mapping technique:")
print("D = Direct Mapping\nS = N-way Sets Associative\nF = Fully Associative")
while True:
    mapping = input()
    if mapping != 'D' or mapping != 'S' or mapping != 'F':
        break

# checks mapping technique and calculates address
if mapping.upper() == 'S':
    nways = int(input("\nNumber of ways: 2^"))
    nsets = nlines - nways  
    tag = memsize - nsets - words
elif mapping.upper() == 'F':
    tag = memsize - words
elif mapping.upper() == 'D':
    tag = memsize - nlines - words

# prints converted data
if memsize >= 30:
    print("\nMAIN MEMORY SIZE: " + str(2 ** (memsize % 30)) + "GB")
elif memsize >= 20:
    print("\nMAIN MEMORY SIZE: " + str(2 ** (memsize % 20)) + "MB")
elif memsize >= 10:
    print("\nMAIN MEMORY SIZE: " + str(2 ** (memsize % 10)) + "KB")
else:
    print("\nMAIN MEMORY SIZE: " + str(2 ** memsize) + "B")

if cachesize >= 30:
    print("CACHE MEMORY SIZE: " + str(2 ** (cachesize % 30)) + "GB")    
elif cachesize >= 20:
    print("CACHE MEMORY SIZE: " + str(2 ** (cachesize % 20)) + "MB")    
elif cachesize >= 10:
    print("CACHE MEMORY SIZE: " + str(2 ** (cachesize % 10)) + "KB")
else:
    print("CACHE MEMORY SIZE: " + str(2 ** cachesize) + "B")

if blocksize >= 30:
    print("BLOCK SIZE: " + str(2 ** (blocksize % 30)) + "GB")
elif blocksize >= 20:
    print("BLOCK SIZE: " + str(2 ** (blocksize % 20)) + "MB")
elif blocksize >= 10:
    print("BLOCK SIZE: " + str(2 ** (blocksize % 10)) + "KB")
else:
    print("BLOCK SIZE: " + str(2 ** blocksize) + "B\n")

# prints data
if mapping.upper() == 'S':
    print(str(2 ** nways) + "-WAY SETS ASSOCIATIVE MAPPING\n")
    print("MEMORY ADDRESS SIZE: " + str(memsize) + " bits")
    print("From " + '0' * memsize + " to " + '1' * memsize)
    print("\nADDRESS (TAG-SET-WORD):")
    print('0' * tag + '-' + '0' * nsets + '-' + '0' * words)
elif mapping.upper() == 'F':
    print("FULLY ASSOCIATIVE MAPPING\n")
    print("MEMORY ADDRESS SIZE: " + str(memsize) + " bits")
    print("From " + '0' * memsize + " to " + '1' * memsize)
    print("\nADDRESS (TAG-WORD):")
    print('0' * tag + '-' + '0' * words)
elif mapping.upper() == 'D':
    print("DIRECT MAPPING\n")
    print("MEMORY ADDRESS SIZE: " + str(memsize) + " bits")
    print("From " + '0' * memsize + " to " + '1' * memsize)
    print("\nADDRESS (TAG-LINE-WORD):")
    print('0' * tag + '-' + '0' * nlines + '-' + '0' * words)

print("")
input()