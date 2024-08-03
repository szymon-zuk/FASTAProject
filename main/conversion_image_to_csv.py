import pytesseract
from PIL import Image
import pandas as pd
import os


def main():
    # Path to the file with the image
    image_path = '/home/szymon/Desktop/FASTAProject/input/tabelka.png'

    # Reading text on image using Tesseract OCR
    text = pytesseract.image_to_string(Image.open(image_path))
    print("Extracted text:\n", text)

    # Splitting text into lines
    lines = text.split('\n')

    # Dividing lines into cells
    data = []
    for line in lines:
        # Deleting empty lines
        if line.strip():
            # Dividing lines into columns
            # Adjusting split method to handle multi-word cells better
            columns = line.split()
            data.append(columns)

    # DataFrame conversion
    df = pd.DataFrame(data)

    # Defining path to CSV file
    csv_path = '/home/szymon/Desktop/FASTAProject/results/converted_table.csv'

    # Export to CSV
    df.to_csv(csv_path, index=False, header=False)

    # Displaying the path to the saved file
    print(f"Dane zostały zapisane do pliku CSV: {csv_path}")


if __name__ == "__main__":
    main()
