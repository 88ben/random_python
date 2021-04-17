# %%
import re
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
from collections import Counter

from constants import *


def plot_histogram(freq):
	plt.bar(freq.keys(), freq.values())
	plt.show()


def clean_sequence(file, chars):
	with open(file, "r") as f:
		seq = f.read().upper()
	return re.sub(f"[^{chars}]+", "", seq)


def extract_proteins(dna, num=1):

	if len(dna) == 0: return

	start = len(dna)
	for i in range(0, len(dna)):
		if dna[i:i+3] == START_CODON:
			start = i
			break

	protein = ""
	for i in range(start, len(dna), 3):
		codon = dna[i:i+3]
		if len(codon) < 3: break
		if codon in STOP_CODONS:
			proteins.append(protein)
			if num > 1:
				extract_proteins(dna[i+3:], num - 1)
			return
		protein += CODONS[codon]


# %%
proteins = []
dna = ''.join(np.random.choice(['A','C','G','T'], 5000))
extract_proteins(dna, 100)
print(proteins)
plot_histogram(Counter(''.join(proteins)))


# %%
proteins = []
dna = clean_sequence("dna", DNA_CHARS)
protein = clean_sequence("amino", AMINO_CHARS)
extract_proteins(dna)
assert(protein == proteins[0])

plot_histogram(Counter(dna))
plot_histogram(Counter(protein))