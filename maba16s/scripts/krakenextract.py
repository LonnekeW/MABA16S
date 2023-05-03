import pandas as pd
import os
import sys


def extract_reads(speciesID, name, krakenfile, genusID, fastqin, outdir):
    os.system('mkdir -p {}'.format(outdir))
    os.system('extract_kraken_reads.py -k {} -o {} -s {} -t {}'.format(krakenfile, os.path.join(outdir, name + ".fastq.gz"), fastqin, genusID))


def read_krakenreport(file, krakenfile, fastqin, outdir):
    df = pd.read_csv(file, sep = '\t', header = None)
    print(df)
    for i in df.iterrows():
        print(i)
        info = i[1]
        name = info[5].strip()
        genusID = info[4]
        extract_reads(genusID, name, krakenfile, genusID, fastqin, outdir)



def main():
    read_krakenreport(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])


if __name__ == "__main__":
    main()
