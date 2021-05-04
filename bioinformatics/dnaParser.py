import re
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

from constants import *

"""
Generate single strand of random DNA sequence

@param n: number of nucleotides in sequence
@return: randomly generated DNA sequence
"""
def generate(n):
  return ''.join(np.random.choice(list(DNA_CHARS), n))

"""
Removes unwanted chars from file
FASTA compatible (ignore lines that start with ';' and '>')

@param file: name of file
@param chars: valid characters (not removed from sequence)
@return: cleaned sequence (DNA or aminos)
"""
def clean(file, chars):
  with open(file, "r") as f:
    seq = "".join([line.upper() for line in f if line.strip()[0] not in FASTA_TAGS])
  return re.sub(f"[^{chars}]+", "", seq)

"""
Remove nucleotides preceeding the first start codon (ATG)

@param dna: DNA sequence
@return: DNA sequence, starting with ATG codon
"""
def crop(dna):
  start = dna.find(START_CODON)
  return "" if start == -1 else dna[start:]

"""
Convert DNA sequence string into list of codons

@param dna: DNA sequence string
@return: codon list
"""
def codons(dna):
  return [dna[i:i+3] for i in range(0, len(dna), 3) if len(dna[i:i+3]) == 3]

"""
Convert codon list to string of corresponding aminos

@param codons: codon list
@return: string of aminos
"""
def aminos(codons):
  return "".join(np.vectorize(CODONS.get)(codons))

"""
Convert aminos string to list of proteins, discarding invalid aminos between each start/stop amino

@param aminos: string of amino chars
@return: list of proteins, discarding terminating codon
"""
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

"""
Convert DNA directly to proteins and return each intermediate step

@param dna: DNA sequence string
@return: DNA cropped, codon list, amino string, protein list
"""
def process(dna):
  dna = crop(dna)
  c = codons(dna)
  a = aminos(c)
  p = proteins(a)
  return dna, c, a, p

"""
Plots frequency of elements in string, dictionary, or list

@param seq: string or dictionary
"""
def frequency(seq):
  freq = Counter(seq)
  plt.bar(freq.keys(), freq.values())
  plt.show()



