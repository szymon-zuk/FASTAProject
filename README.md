# FASTA Sequence Downloader

## Overview

This project provides a set of scripts to process an image of a table, convert the extracted data into a CSV format, and then use the CSV to download FASTA sequences from NCBI. The workflow consists of two main steps:
1. **Convert Table Image to CSV**: Use OCR (Optical Character Recognition) to extract text from an image and save it as a CSV file.
2. **Download FASTA Sequences**: Parse the CSV file and download nucleotide sequences from NCBI based on the accession numbers listed in the CSV.

## Project Structure
```
FASTAProject/
│
├── input/
│ └── tabelka.png # Image file containing the table
│
├── results/
│ └── converted_table.csv # Output CSV file after conversion
│
├── fasta_results/ # Directory for FASTA files
│
├── convert_image_to_csv.py # Script to convert table image to CSV
├── download_fasta_files.py # Script to download FASTA sequences
└── run_all.py # Master script to run both steps
```

## Prerequisites

- Python 3.x
- Tesseract OCR

### Installing Dependencies

Install the required Python libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
Installing Tesseract OCR
Ubuntu: sudo apt-get install tesseract-ocr
macOS: brew install tesseract
Windows: Download the installer from the official repository and follow the installation instructions.

### Usage
#### Convert Table Image to CSV

Run the conversion_image_to_csv.py script to convert the table image to a CSV file:

```bash
python3 conversion_image_to_csv.py
```
This script reads the table from `input/tabelka.png` and saves the extracted data to `results/converted_table.csv`.

#### Download FASTA Sequences

Run the `download_fasta_files.py` script to download FASTA sequences based on the CSV file:

```bash
python3 download_fasta_files.py
```
This script reads the accession numbers from `results/converted_table.csv` and downloads the corresponding FASTA sequences to the `fasta_results/` directory.

#### Run All Steps

Alternatively, you can run both steps sequentially using the `run_all.py` master script:

```bash
python3 run_all.py
```
This script will first execute the image-to-CSV conversion and then download the FASTA sequences.

### Configuration
Update the paths in the scripts if necessary:
convert_image_to_csv.py: Path to the input image and output CSV file. \
download_fasta_files.py: Path to the input CSV file and output directory for FASTA files. \
Ensure Entrez.email in download_fasta_files.py is set to a valid email address.

### Troubleshooting
OCR Accuracy: If the text extraction from the image is inaccurate, consider preprocessing the image (e.g., increasing contrast or resizing) to improve OCR results. \
Missing Files: Ensure that the paths to the image, CSV file, and output directories are correctly specified in the scripts.

### License
This project is licensed under the MIT License.

### Acknowledgements
Tesseract OCR for text extraction.
Biopython for handling biological sequence data.
