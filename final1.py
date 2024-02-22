import os
import pandas as pd
import pytesseract
from pdf2image import convert_from_path
import openai
import re

data = []
api ="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"
def chat_with_gpt(prompt):
        openai.api_key =  api # Replace with your OpenAI API key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "Please provide  information in the form of separate  Python dictionaries.Each entry should include the exact name, husband/father name, age, and gender. For example: {name:'John Doe', husband_or_father_name:'Doe Sr.', age:30, gender:'Male'} ,add comma after every disctionary"},
            {"role": "user", "content": prompt}
           ], temperature=0.2,
           )

        return response['choices'][0]['message']['content'].strip()


def save_to_excel(data,output_folder, excel_filename):
    os.makedirs(output_folder, exist_ok=True) 
    excel_filepath = os.path.join(output_folder, excel_filename)
    df = pd.DataFrame(data=data)
    df.to_excel(excel_filepath, index=False)
    print(f"Data saved to {excel_filename}")

def pdf_image_to_text_in_chunks(pdf_path,chunk_size=10):
    text_lists = [] 
    images = convert_from_path(pdf_path)

    for i, img in enumerate(images):
        text = pytesseract.image_to_string(img, lang='eng')
        lines = text.split('\n')

        page_text_list = []
        for j in range(0, len(lines), chunk_size):
            chunk = lines[j:j + chunk_size]
            modified_text = '\n'.join(chunk)
            page_text_list.append(modified_text)

        text_lists.append(page_text_list)
        prompt = (f"{page_text_list}")
        response = chat_with_gpt(prompt)
        try:
            pattern = r'\{([^}]*)\}'
            matches = re.findall(pattern, response)
            for match in matches:
                key_value_pairs = re.split(r',\s*', match)
                dictionary = {}
                for pair in key_value_pairs:
                    key, value = re.split(r':\s*', pair, maxsplit=1)
                    dictionary[key] = eval(value)  # Using eval to handle both strings and numbers

                data.append(dictionary)
        except:
            print('Sorry')

    return text_lists

# Function to process all PDFs in a folder
def process_pdfs_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_file_path = os.path.join(folder_path, filename)
            print(f"Processing PDF: {pdf_file_path}")
            pdf_image_to_text_in_chunks(pdf_file_path, chunk_size=10)
            save_to_excel(data,"Excel_file" ,f"{os.path.splitext(filename)[0]}.xlsx")


# Specify the folder containing the PDFs
pdf_folder_path = input("Specify the folders for input and output")
process_pdfs_in_folder(pdf_folder_path)


