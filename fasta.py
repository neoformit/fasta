def read(fName):
        
    """Reads in a fasta-formatted sequence file.
    
    Returns a dictionary of sequences, indexed by sequence title.

    Arguments
    ---------
    filename: a string of the filename to be read or an open file handle
    """

    if isinstance(fName, str):
        handle = open(fName,'r')
    else: handle = fName
    
    seq = ""
    title = ""
    seqData = {}
    copy = False
    
    for line in handle:
        if line[0]=='>':
            if copy is True:
                seqData[title] = seq
            title = line.strip(">\n\r ")
            copy = True
            seq = ""
        else:
            seq += line.strip("\n\r ")
    if title in seqData.keys():
        raise KeyError('Fasta file contains duplicate contig ids.')
    seqData[title] = seq

    if isinstance(fName, str):
        handle.close()
    return seqData



def write(data, filename):
        
    """
    Writes a dictionary of DNA or Protein sequences to the given file name
    in fasta format.
    
    Requires two positional arguments: fas (dict), fname (str)
    """
    
    w = open(filename,'w')
    writeList = []
    
    for title, sequence in data.items():
        
        seqList = []
        while True:
            if len(sequence) >= 80:
                seqList.append(sequence[0:80])
                sequence = sequence[80:]
            else:
                seqList.append(sequence)
                break
        writeList.append('>' + title + '\n' + '\n'.join(seqList))
    
    w.write('\n'.join(writeList))
    w.close()
