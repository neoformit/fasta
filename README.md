# fasta
A simple parser and writer for FASTA files


```python
import fasta

# Read a FASTA file into a dictionary of {sid <str>: sequence <str>}
fas = fasta.read('sequences.fas')

# Get a sequence
seq = fas['contig_23']

# Loop over sequences
for k, seq in fas.items():
    print(f"Sequence name: {k}")
    print(f"    - {len(seq)}bp")

# Write a fasta dictionary back to file
filename = "myfile.fas"
fasta.write(fas, filename)
```
