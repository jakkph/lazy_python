import os
import subprocess
from PyPDF2 import PdfMerger

# Step 1: Identify MDX Files
def find_mdx_files(directory):
    mdx_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mdx'):
                mdx_files.append(os.path.join(root, file))
    return mdx_files

# Step 2: Convert MDX to PDF
def convert_mdx_to_pdf(mdx_file):
    pdf_file = mdx_file[:-4] + '.pdf'
    subprocess.run(['mdx2pdf', mdx_file, pdf_file])  # Use mdx2pdf tool
    return pdf_file

# Step 3: Combine PDFs
def combine_pdfs(pdf_files, output_pdf):
    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    merger.write(output_pdf)
    merger.close()

if __name__ == "__main__":
    input_directory = "path/to/mdx/files"
    output_pdf = "output.pdf"

    mdx_files = find_mdx_files(input_directory)
    pdf_files = [convert_mdx_to_pdf(mdx_file) for mdx_file in mdx_files]
    
    combine_pdfs(pdf_files, output_pdf)

    print("Conversion and combination completed!")
