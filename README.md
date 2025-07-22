# PDF Annotation Remover

PDF Annotation Remover is a simple Python command-line tool that removes annotations (comments) from PDF files. Instead of having to use expensive software like Adobe Acrobat Pro, this script lets you quickly anonymise your PDFs by replacing annotation author fields with "Anonymous".

## Features

- Remove annotations from PDF files.
- Replace annotation author (“/T”) with "Anonymous".
- Easy command-line interface with customisable input and output file options.

## Requirements

- Python 3.6 or higher
- [PyPDF2](https://pypi.org/project/PyPDF2/)

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/pdf-annotation-remover.git

2. Navigate to the project directory:

   cd pdf-annotation-remover

3. Install the required dependency:

   pip install PyPDF2

## Usage

The script is a standalone Python file (`rmannot.py`). It accepts an input PDF file and an optional output PDF file argument.

### Command-Line Arguments

- `-i` or `--input`: Path to the input PDF file.
- `-o` or `--output`: Path to the output PDF file. If not provided, the script will generate a default name based on the input file (e.g., if the input is `example.pdf`, the output will be named `example_anonymised.pdf`).

### Example

To remove annotations from a PDF named `sample.pdf`:

   python rmannot.py -i sample.pdf

To specify a custom name for the output file:

   python rmannot.py -i sample.pdf -o output.pdf

## Testing

In the `test` folder, you will find:
- An example input file.
- The intended output file after processing.

To test the script with the provided files, run:

   python rmannot.py -i test/test.pdf -o test/your_output_file.pdf

You can then open `your_output_file.pdf` to verify that annotations have been anonymised which should be identical to `test/test_anonymised.pdf`.

## How It Works

1. The script uses PyPDF2 to read the input PDF file.
2. It iterates through each page and checks for annotations via the `/Annots` key.
3. For any annotation found, if it contains an author field (`/T`), the script replaces its value with "Anonymous".
4. The updated pages are written into a new PDF file specified by the output argument.

## Author

Masoud Ghaderi Zefreh

## License

This project is provided for personal use. Feel free to fork and modify the code according to your needs.

---

Enjoy using PDF Annotation Remover! If you have any questions, issues, or suggestions, please open an issue or submit a pull request.
