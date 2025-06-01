"""
This script prepares a corpus in Vertex AI RAG by downloading a PDF document from a URL,
uploading it to the corpus, and updating the .env file with the corpus name.
It uses the Vertex AI Python SDK to interact with the RAG service.
"""

from google.auth import default
import vertexai
from vertexai.preview import rag
import os
from dotenv import load_dotenv, set_key
import requests
import tempfile

# Load environment variables from .env file
load_dotenv()

# --- Please fill in your configurations ---
# Retrieve the PROJECT_ID from the environmental variables.
PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
if not PROJECT_ID:
    raise ValueError(
        "GOOGLE_CLOUD_PROJECT environment variable not set. Please set it in your .env file."
    )
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
if not LOCATION:
    raise ValueError(
        "GOOGLE_CLOUD_LOCATION environment variable not set. Please set it in your .env file."
    )
GOOGLE_CLOUD_STORAGE_BUCKET = os.getenv("GOOGLE_CLOUD_STORAGE_BUCKET")
if not GOOGLE_CLOUD_STORAGE_BUCKET:
    raise ValueError(
        "GOOGLE_CLOUD_STORAGE_BUCKET environment variable not set. Please set it in your .env file."
    )
CORPUS_DISPLAY_NAME = "test_corpus_rag"
CORPUS_DESCRIPTION = "Corpus for testing RAG"
PDF_URL = "https://abc.xyz/assets/77/51/9841ad5c4fbe85b4440c47a4df8d/goog-10-k-2024.pdf"
PDF_FILENAME = "goog-10-k-2024.pdf"
ENV_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
PDF_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "resources", "SMA-EAD.pdf"))


# --- Start of the script ---
def initialize_vertex_ai():
  credentials, _ = default()
  vertexai.init(
    project=PROJECT_ID, 
    location=LOCATION, 
    credentials=credentials
  )


def create_or_get_corpus():
  """Creates a new corpus or retrieves an existing one."""
  embedding_model_config = rag.EmbeddingModelConfig(
    publisher_model="publishers/google/models/text-embedding-004"
  )
  existing_corpora = rag.list_corpora()
  corpus = None
  for existing_corpus in existing_corpora:
    if existing_corpus.display_name == CORPUS_DISPLAY_NAME:
      corpus = existing_corpus
      print(f"Found existing corpus with display name '{CORPUS_DISPLAY_NAME}'")
      break
  if corpus is None:
    corpus = rag.create_corpus(
        display_name=CORPUS_DISPLAY_NAME,
        description=CORPUS_DESCRIPTION,
        embedding_model_config=embedding_model_config,
    )
    print(f"Created new corpus with display name '{CORPUS_DISPLAY_NAME}'")
  return corpus

def import_files_to_corpus(corpus):
  """Imports files to the specified corpus."""
  print(f"Importing files to corpus {CORPUS_DISPLAY_NAME}...")

  paths = [f"gs://{GOOGLE_CLOUD_STORAGE_BUCKET}/rag_files"]  # Supports Google Cloud Storage and Google Drive Links ["https://drive.google.com/file/d/123", "gs://my_bucket/my_files_dir"]
  try:
    response = rag.import_files(
    corpus_name=corpus.name,
    paths=paths,
    transformation_config=rag.TransformationConfig(
      rag.ChunkingConfig(chunk_size=512, chunk_overlap=100)
    ),
    #import_result_sink="gs://academic_research/rag_import_results/sample_import_result_unique.ndjson",  # Optional, this has to be an existing storage bucket folder, and file name has to be unique (non-existent).
    max_embedding_requests_per_min=900,  # Optional
    )
    print(f"Imported {response.imported_rag_files_count} files.")
  except Exception as e:
    print(f"Error importing files: {e}")


def download_pdf_from_url(url, output_path):
  """Downloads a PDF file from the specified URL."""
  print(f"Downloading PDF from {url}...")
  response = requests.get(url, stream=True)
  response.raise_for_status()  # Raise an exception for HTTP errors
  
  with open(output_path, 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
      f.write(chunk)
  
  print(f"PDF downloaded successfully to {output_path}")
  return output_path


def upload_pdf_to_corpus(corpus_name, pdf_path, display_name, description):
  """Uploads a PDF file to the specified corpus."""
  print(f"Uploading {display_name} to corpus...")
  try:
    rag_file = rag.upload_file(
        corpus_name=corpus_name,
        path=pdf_path,
        display_name=display_name,
        description=description,
    )
    print(f"Successfully uploaded {display_name} to corpus")
    return rag_file
  except Exception as e:
    print(f"Error uploading file {display_name}: {e}")
    return None

def update_env_file(corpus_name, env_file_path):
    """Updates the .env file with the corpus name."""
    try:
        set_key(env_file_path, "RAG_CORPUS", corpus_name)
        print(f"Updated RAG_CORPUS in {env_file_path} to {corpus_name}")
    except Exception as e:
        print(f"Error updating .env file: {e}")

def list_corpus_files(corpus_name):
  """Lists files in the specified corpus."""
  files = list(rag.list_files(corpus_name=corpus_name))
  print(f"Total files in corpus: {len(files)}")
  for file in files:
    print(f"File: {file.display_name} - {file.name}")


def main():
  initialize_vertex_ai()
  corpus = create_or_get_corpus()
  #import_files_to_corpus(corpus)

  # Update the .env file with the corpus name
  #update_env_file(corpus.name, ENV_FILE_PATH)

  # Upload your local PDF to the corpus
  local_file_path = PDF_FILE_PATH # Set the correct path
  display_name = "SMA-EAD.pdf" # Set the desired display name
  description = "SMA - EAD File" # Set the description

  # Ensure the file exists before uploading
  if os.path.exists(local_file_path):
      upload_pdf_to_corpus(
          corpus_name=corpus.name,
          pdf_path=local_file_path,
          display_name=display_name,
          description=description
      )
  else:
      print(f"Error: Local file not found at {local_file_path}")

  # Create a temporary directory to store the downloaded PDF
  #with tempfile.TemporaryDirectory() as temp_dir:
  #  pdf_path = os.path.join(temp_dir, PDF_FILENAME)
  #  
  #  # Download the PDF from the URL
  #  download_pdf_from_url(PDF_URL, pdf_path)
  #  
  #  # Upload the PDF to the corpus
  #  upload_pdf_to_corpus(
  #      corpus_name=corpus.name,
  #      pdf_path=pdf_path,
  #      display_name=PDF_FILENAME,
  #      description="Alphabet's 10-K 2024 document"
  #  )
  
  # List all files in the corpus
  list_corpus_files(corpus_name=corpus.name)

if __name__ == "__main__":
  main()
