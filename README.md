Certainly! Below is a template for a README file for your script. Make sure to customize it according to your specific requirements.

```markdown
# PDF Data Extraction and Conversion to Excel

This script processes PDF files, extracts text using OCR (Optical Character Recognition), and utilizes GPT-3.5 Turbo for generating Python dictionaries based on the extracted text. The extracted data is then saved into individual Excel files.

## Requirements

Ensure you have the following packages installed:

 Python 3.x
- pip install pandas
- pip install pytesseract
- pip install pdf2image
- pip install openai

For mac user , install the required packages using the following command:

```bash
pip install pandas pytesseract pdf2image openai
```

Additionally, you need Tesseract OCR installed on your machine. Follow the installation instructions for your operating system: [Tesseract Installation Guide](https://github.com/tesseract-ocr/tesseract)

## Usage

1. **OpenAI API Key**: Replace the `api` variable in the script with your OpenAI API key.

2. **Specify Input and Output Folders**: Modify the `pdf_folder_path` variable to the path where your PDF files are located. The script will create an "Excel_files" folder in the same directory to store the output Excel files.

3. **Run the Script**: Execute the script by running the following command in your terminal or command prompt:

```bash
python your_script_name.py
```

Replace `your_script_name.py` with the actual name of your script.

4. **Check Output**: The script will process each PDF, generate Python dictionaries using GPT-3.5 Turbo, and save the data into individual Excel files. Check the "Excel_files" folder for the output.

## Note

- The script uses OCR to extract text from PDF images, which may not be 100% accurate.
- Ensure proper installation of Tesseract OCR and required Python packages.

Feel free to customize the script according to your specific use case or requirements.
```

Replace placeholders like `your_script_name.py` with the actual name of your Python script. This README provides information about required packages, OpenAI API key, usage instructions, and additional notes.
