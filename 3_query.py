from openai import OpenAI
from groundx import GroundX 


GROUNDX_API_KEY = "686611fd-cbd4-4dc0-a157-18ded2d62462" 
BUCKET_ID = 23605

LLM_MODEL_NAME = "inference-llama4-maverick"
LLM_API_BASE = "https://maas.ai-2.kvant.cloud"
LLM_API_KEY = "sk-myRxTMEUhSEoWzV5v8uqAQ"

# ----------------------------------------------

SYSTEM_PROMPT = """
You are a helpful and highly knowledgeable assistant. 
Your primary role is to assist the user by answering questions 
related to the documents they have uploaded and that have been 
processed by the GroundX ingestion pipeline in md format. 
Your answers must be based **ONLY** on the provided context, 
which follows the '===' separator. 
Be precise and detailed. Provide the link to the source of the exact answer. 
===
"""
# ----------------------------------------------

def run_rag_pipeline(query: str):
    try:
        groundx = GroundX(api_key=GROUNDX_API_KEY)
        openai_client = OpenAI(
            base_url=LLM_API_BASE,
            api_key=LLM_API_KEY
        )
    except Exception as e:
        print("Error in initializing clients:", e)
        return

    try:
        print("Searching in database...")
        groundx_response = groundx.search.content(
            id=BUCKET_ID,
            query=query,
        )
        
        context_text = groundx_response.search.text 

    except Exception as e:
        print("Retrieval Error", e)
        return

    if context_text:

        full_system_prompt = f"{SYSTEM_PROMPT}CONTEXT ONLY WITH INFORMATION FROM: {context_text}"
        
        try:
            completion = openai_client.chat.completions.create(
                model=LLM_MODEL_NAME,
                messages=[
                    {"role": "system", "content": full_system_prompt},
                    {"role": "user", "content": query},
                ],                
                temperature=0.2,
            )
            
            rag_answer = completion.choices[0].message.content
            
            print(rag_answer)
            print("--------------------------------------------------")

        except Exception as e:
            print("Error with API key,", e)
    else:
        print("I do not have that information in my database.")


def main():

    print("--------------------")
    print("   ITNB CHATBOT")
    print("--------------------")
    
    while True:
        try:
            query = input("Ask something: ")
            run_rag_pipeline(query)

        except KeyboardInterrupt:
            print("\nEND.")
            break

if __name__ == "__main__":
    main()
