import random
import math

# ===========================================
# Load ciphertext
# ===========================================
cipher = """EGIWLUQ DUOHGKODG RIKTAWTWRDUSERKBDZERNOIRA CQUIOIWAHHNNMIWDGRKRLCQPGOIUICRKVPG ...""".replace(" ", "").replace("\n", "")
cipher = ''.join([c for c in cipher.upper() if c.isalpha()])

# Two-square alphabet (I/J merged)
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

# ===========================================
# Build square from a key ordering
# ===========================================
def square_from_key(key):
    s = []
    for c in key:
        if c == "J": c = "I"
        if c not in s and c in alphabet: s.append(c)
    for c in alphabet:
        if c not in s: s.append(c)
    return s

def pos(square, ch):
    idx = square.index(ch)
    return idx // 5, idx % 5

def decrypt_pair(a, b, sq1, sq2):
    r1, c1 = pos(sq1, a)
    r2, c2 = pos(sq2, b)
    return sq1[r1*5 + c2] + sq2[r2*5 + c1]

def decrypt(cipher, sq1, sq2):
    out = []
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        out.append(decrypt_pair(a,b,sq1,sq2))
    return "".join(out)

# ===========================================
# Fitness scoring (quadgram statistics)
# ===========================================
import urllib.request

try:
    # download quadgrams if missing
    data = urllib.request.urlopen("https://practicalcryptography.com/media/cryptanalysis/files/quadgrams.txt")
    quad = data.read().decode()
except:
    print("Download quadgrams manually if needed")
    quad = ""

qgrams = {}
for line in quad.splitlines():
    parts = line.split()
    if len(parts)==2:
        qgrams[parts[0]] = math.log10(float(parts[1]))

floor = math.log10(0.01/10**8)

def fitness(text):
    score = 0
    for i in range(len(text)-3):
        gram = text[i:i+4]
        score += qgrams.get(gram, floor)
    return score

# ===========================================
# Random key generator
# ===========================================
def random_key():
    s = list(alphabet)
    random.shuffle(s)
    return "".join(s)

# ===========================================
# Hillclimb Two-Square
# ===========================================
def climb():
    key1 = random_key()
    key2 = random_key()
    sq1 = square_from_key(key1)
    sq2 = square_from_key(key2)
    best_plain = decrypt(cipher, sq1, sq2)
    best_score = fitness(best_plain)

    for step in range(200000):
        # mutate one square
        k1 = list(key1)
        k2 = list(key2)

        if random.random() < 0.5:
            i, j = random.sample(range(25), 2)
            k1[i], k1[j] = k1[j], k1[i]
        else:
            i, j = random.sample(range(25), 2)
            k2[i], k2[j] = k2[j], k2[i]

        sq1r = square_from_key(k1)
        sq2r = square_from_key(k2)
        pt = decrypt(cipher, sq1r, sq2r)
        sc = fitness(pt)

        if sc > best_score:
            best_score = sc
            best_plain = pt
            key1, key2 = "".join(k1), "".join(k2)
            print("\nImproved score", best_score)
            print(best_plain[:200], "...")
    return best_plain

print("Starting…")
plaintext = climb()
print("\nFinal plaintext:\n")
print(plaintext)
