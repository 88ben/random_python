# %%
import numpy as np
from pprint import pprint

from dnaParser import *
from constants import *

raw_dna = generate(50000)
dna, codons, aminos, proteins = process(raw_dna)

frequency(aminos)

raw_dna = clean("data/dna", DNA_CHARS)
protein = clean("data/amino", AMINO_CHARS)
dna, codons, aminos, proteins = process(raw_dna)
assert(protein == proteins[0])