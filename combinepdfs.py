import os
import re
from PyPDF2 import PdfMerger

def sort_pdfs(directory):
    """Sorts PDF files in a directory based on natural sorting."""
    files = [f for f in os.listdir(directory) if f.lower().endswith(".pdf")]

    def natural_sort_key(s):
        """Key for natural sorting of strings with numbers."""
        return [int(text) if text.isdigit() else text.lower()
                for text in re.split(r'(\d+)', s)]

    files.sort(key=natural_sort_key)
    return files


def combine_pdfs(directory, sorted_files, output_name="merged.pdf"):
    """Combines sorted PDF files into a single PDF."""
    merger = PdfMerger()
    for file in sorted_files:
        merger.append(open(os.path.join(directory, file), 'rb'))
    with open(output_name, "wb") as fout:
        merger.write(fout)


if __name__ == "__main__":
    pdf_directory = "."  # Change to your directory path
    sorted_pdfs = sort_pdfs(pdf_directory)
    combine_pdfs(pdf_directory, sorted_pdfs)
    print("PDFs sorted and merged successfully into merged.pdf")