"""Read and write fasta files.

Fasta files read into a Python dictionary as <sequence_id>: <sequence>.
"""


def read(filename):
    """Read in a fasta-formatted sequence file.

    Returns a dictionary of sequences, indexed by sequence title.

    Arguments:
    ---------
    filename: a string of the filename to be read or an open file handle

    """
    if isinstance(filename, str):
        handle = open(filename, 'r')
    else:
        handle = filename

    seq = ""
    title = ""
    seqData = {}
    copy = False

    for line in handle:
        if line[0] == '>':
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

    if isinstance(filename, str):
        handle.close()
    return seqData


def write(data, filename):
    """Write a dictionary of FASTA sequences to file.

    Arguments:
    ---------
    data: dict Dictionary of {sid: sequence}
    filename: str Filename to write

    """
    w = open(filename, 'w')
    write_list = []

    for title, sequence in data.items():

        sequence_list = []
        while True:
            if len(sequence) >= 80:
                sequence_list.append(sequence[0:80])
                sequence = sequence[80:]
            else:
                sequence_list.append(sequence)
                break
        write_list.append('>' + title + '\n' + '\n'.join(sequence_list))

    w.write('\n'.join(write_list))
    w.close()
