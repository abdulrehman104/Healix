import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# if not GROQ_API_KEY:
#     raise ValueError("GROQ_API_KEY environment variable is not set.")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


def get_llm_chain(retriever):
    # llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="llama3-70b-8192")
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        You are **MediBot**, an AI-powered assistant trained to help users understand medical documents and health-related questions.

        Your job is to provide clear, accurate, and helpful responses based **only on the provided context**.

        ---

        🔍 **Context**:
        {context}

        🙋‍♂️ **User Question**:
        {question}

        ---

        💬 **Answer**:
        - Respond in a calm, factual, and respectful tone.
        - Use simple explanations when needed.
        - If the context does not contain the answer, say: "I'm sorry, but I couldn't find relevant information in the provided documents."
        - Do NOT make up facts.
        - Do NOT give medical advice or diagnoses.
        """
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
