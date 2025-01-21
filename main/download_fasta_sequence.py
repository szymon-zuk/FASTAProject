import csv
import os
from Bio import Entrez, SeqIO


# Function for downloading and saving sequences
def fetch_and_save_sequences(gene, accessions, output_dir):
    Entrez.email = "szymon.p.zuk@gmail.com"  # Enter your email (required by NCBI)
    sequences = []
    for acc in accessions:
        try:
            handle = Entrez.efetch(db="nucleotide", id=acc, rettype="fasta", retmode="text")
            seq_record = SeqIO.read(handle, "fasta")
            handle.close()
            sequences.append(seq_record)
        except Exception as e:
            print(f"Error downloading {acc}: {e}")

    if sequences:
        output_file = os.path.join(output_dir, f"{gene}.fasta")
        SeqIO.write(sequences, output_file, "fasta")
        print(f"Saved {output_file}")


def main():
    csv_path = '/home/szymon/Desktop/FASTAProject/results/converted_table.csv'  # Provide path to your CSV file

    # Provide path to the folder in which you want FASTA results
    output_dir = '/home/szymon/Desktop/FASTAProject/fasta_results/'

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loading data from CSV file
    gene_dict = {}

    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)[1:]  # Skip the first header row and get the gene names
        for header in headers:
            gene_dict[header] = []

        for row in reader:
            for idx, acc in enumerate(row[1:]):  # Skip the first column which is 'No.'
                gene_dict[headers[idx]].append(acc)

    # Downloading and saving the sequence for every gene
    for gene, accessions in gene_dict.items():
        fetch_and_save_sequences(gene, accessions, output_dir)


if __name__ == "__main__":
    main()
