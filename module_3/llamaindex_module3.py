#Import Library
from llama_index.core import SimpleDirectoryReader

#Instantiate Reader
reader = SimpleDirectoryReader(input_dir="module_3",
                               exclude = ["readme.txt",
                                          "llamaindex_module3.py"])
documents = reader.load_data()

#Ensure data for loaded documents
for doc in documents:
    print(f"Document Name: {doc.metadata.get('file_name', 'Unknown')}")
    print(f"Document Text: {doc.text[:500]}")
    print("="*80)

reader = SimpleDirectoryReader(input_dir="module_3",
                               input_files = ["Lesson_three_example.ipynb"])
documents = reader.load_data()

for doc in documents:
    print(f"Document Name: {doc.metadata.get('file_name', 'Unknown')}")
    print(f"Document Text: {doc.text[:500]}")
    print("="*80)