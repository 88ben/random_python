# %%
import re
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

from constants import *


def generate(n):
	return ''.join(np.random.choice(list(DNA_CHARS), n))

def clean(file, chars):
	with open(file, "r") as f:
		seq = f.read().upper()
	return re.sub(f"[^{chars}]+", "", seq)

def crop(dna):
	start = dna.find(START_CODON)
	return "" if start == -1 else dna[start:]

def codons(dna):
	return [dna[i:i+3] for i in range(0, len(dna), 3) if len(dna[i:i+3]) == 3]

def aminos(codons):
	return ''.join(np.vectorize(CODONS.get)(codons))

def proteins(aminos):
	record = False
	proteins = []
	p = ""
	for amino in aminos:
		if amino == START_AMINO: record = True
		elif amino == STOP_AMINO:
			if p: proteins.append(p)
			record = False
			p = ""
		if record: p += amino
	return proteins

def process(dna):
	dna = crop(dna)
	c = codons(dna)
	a = aminos(c)
	p = proteins(a)
	return dna, c, a, p

def frequency(seq):
	freq = Counter(seq)
	plt.bar(freq.keys(), freq.values())
	plt.show()



