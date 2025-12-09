from groundx import GroundX, Document
import os
from pprint import pprint

GROUNDX_API_KEY = "686611fd-cbd4-4dc0-a157-18ded2d62462" 
BUCKET_ID = 23605
FILE_PATH = "itnb_content3.md"

def ingest_content_with_sdk():

    if not os.path.exists(FILE_PATH):
        print("File path does not exist.")
        return

    groundx = GroundX(api_key=GROUNDX_API_KEY)
    
    print(f"Ingestion...")

    try:
        response = groundx.ingest(
            documents=[
                Document(
                    bucket_id=BUCKET_ID,
                    file_name=os.path.basename(FILE_PATH),
                    file_path=FILE_PATH, 
                    file_type="markdown",
                    search_data={"source": "itnb_web_scrape"} 
                )
            ]
        )
        
        process_id = response.ingest.process_id
        
        if process_id:
            print("\n Ingest successful.")
            print(f"   ID: **{process_id}**")
            return process_id
        else:
            print("Ingest Error.")
            pprint(response.dict())
            return None
            
    except Exception as e:
        print(f"Exception during ingestion: {e}")
        return None

if __name__ == "__main__":
    process_id = ingest_content_with_sdk()
