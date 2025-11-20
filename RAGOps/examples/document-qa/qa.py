"""
Document Q&A with RAG
Demonstrates: Document loading, chunking, embedding, retrieval, answer generation
"""

from pathlib import Path
from typing import List, Dict
import chromadb
from chromadb.config import Settings
import requests
import json

# Service endpoints
OLLAMA_URL = "http://localhost:11434"
CHROMA_URL = "http://localhost:8000"

class DocumentQA:
    def __init__(self):
        """Initialize RAG pipeline components"""
        # ChromaDB client
        self.chroma_client = chromadb.HttpClient(
            host="localhost",
            port=8000
        )

        # Create or get collection
        self.collection = self.chroma_client.get_or_create_collection(
            name="documents",
            metadata={"description": "Document Q&A collection"}
        )

    def load_documents(self, directory: str) -> List[Dict]:
        """Load documents from directory"""
        docs = []

        for file_path in Path(directory).glob("*.txt"):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                docs.append({
                    'content': content,
                    'source': str(file_path),
                    'filename': file_path.name
                })

        return docs

    def chunk_text(self, text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
        """Split text into overlapping chunks"""
        chunks = []
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start = end - overlap

        return chunks

    def embed_documents(self, docs: List[Dict]):
        """Chunk and embed documents into vector DB"""

        all_chunks = []
        all_metadatas = []
        all_ids = []

        for doc_id, doc in enumerate(docs):
            # Chunk document
            chunks = self.chunk_text(doc['content'])

            for chunk_id, chunk in enumerate(chunks):
                all_chunks.append(chunk)
                all_metadatas.append({
                    'source': doc['source'],
                    'filename': doc['filename'],
                    'chunk_id': chunk_id
                })
                all_ids.append(f"doc{doc_id}_chunk{chunk_id}")

        # Add to ChromaDB
        self.collection.add(
            documents=all_chunks,
            metadatas=all_metadatas,
            ids=all_ids
        )

        print(f"✅ Embedded {len(all_chunks)} chunks from {len(docs)} documents")

    def retrieve_context(self, query: str, n_results: int = 3) -> List[Dict]:
        """Retrieve relevant context for query"""

        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )

        contexts = []
        for i in range(len(results['documents'][0])):
            contexts.append({
                'text': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i] if 'distances' in results else None
            })

        return contexts

    def generate_answer(self, query: str, contexts: List[Dict]) -> str:
        """Generate answer using LLM with retrieved context"""

        # Construct prompt
        context_text = "\n\n".join([
            f"Source: {ctx['metadata']['filename']}\n{ctx['text']}"
            for ctx in contexts
        ])

        prompt = f"""Use the following context to answer the question. If you cannot answer based on the context, say so.

Context:
{context_text}

Question: {query}

Answer:"""

        # Call Ollama
        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": "llama2",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()['response']

    def ask(self, question: str, show_sources: bool = True) -> Dict:
        """Ask a question and get answer with sources"""

        # Retrieve relevant context
        contexts = self.retrieve_context(question, n_results=3)

        # Generate answer
        answer = self.generate_answer(question, contexts)

        result = {
            'question': question,
            'answer': answer,
            'sources': contexts if show_sources else None
        }

        return result

def create_sample_documents():
    """Create sample documents for testing"""

    docs_dir = Path("sample_docs")
    docs_dir.mkdir(exist_ok=True)

    documents = {
        "machine_learning.txt": """
        Machine Learning is a subset of artificial intelligence that focuses on
        building systems that learn from data. It involves training algorithms
        on datasets to make predictions or decisions without being explicitly
        programmed. Common types include supervised learning, unsupervised learning,
        and reinforcement learning. Popular frameworks include TensorFlow, PyTorch,
        and Scikit-learn.
        """,

        "docker.txt": """
        Docker is a platform for developing, shipping, and running applications
        in containers. Containers package software with all its dependencies,
        ensuring consistency across environments. Docker uses images as templates
        for containers. The docker-compose tool helps manage multi-container
        applications. Docker Hub is a registry for sharing container images.
        """,

        "python.txt": """
        Python is a high-level programming language known for its simplicity
        and readability. It supports multiple programming paradigms including
        procedural, object-oriented, and functional programming. Python has a
        rich ecosystem of libraries for web development (Django, Flask),
        data science (NumPy, Pandas), and machine learning (TensorFlow, PyTorch).
        The language uses indentation for code blocks.
        """
    }

    for filename, content in documents.items():
        (docs_dir / filename).write_text(content.strip())

    return str(docs_dir)

def main():
    """Demo RAG pipeline"""

    print("🔍 Document Q&A with RAG")
    print("=" * 60)

    # Create sample documents
    print("\n📝 Creating sample documents...")
    docs_dir = create_sample_documents()
    print(f"✅ Documents created in {docs_dir}/")

    # Initialize Q&A system
    print("\n🔧 Initializing RAG pipeline...")
    qa = DocumentQA()

    # Load and embed documents
    print("\n📚 Loading documents...")
    docs = qa.load_documents(docs_dir)
    print(f"  Found {len(docs)} documents")

    print("\n🔢 Embedding documents...")
    qa.embed_documents(docs)

    # Example questions
    questions = [
        "What is machine learning?",
        "How does Docker work?",
        "What programming paradigms does Python support?",
        "What are popular machine learning frameworks?",
        "What is docker-compose used for?"
    ]

    print("\n" + "=" * 60)
    print("💬 Asking Questions")
    print("=" * 60)

    for question in questions:
        print(f"\n❓ Question: {question}")
        print("-" * 60)

        result = qa.ask(question, show_sources=True)

        print(f"\n✅ Answer:\n{result['answer']}\n")

        print("📖 Sources:")
        for i, source in enumerate(result['sources'], 1):
            print(f"  {i}. {source['metadata']['filename']} "
                  f"(relevance: {1 - source['distance']:.2f})")

    print("\n" + "=" * 60)
    print("✨ Demo complete!")
    print("=" * 60)

def interactive_mode():
    """Interactive Q&A session"""

    print("🔍 Interactive Document Q&A")
    print("=" * 60)

    # Setup
    docs_dir = create_sample_documents()
    qa = DocumentQA()
    docs = qa.load_documents(docs_dir)
    qa.embed_documents(docs)

    print("\n✅ System ready! Ask questions about the documents.")
    print("Type 'quit' to exit\n")

    while True:
        question = input("\n❓ Your question: ").strip()

        if question.lower() in ['quit', 'exit', 'q']:
            print("Goodbye! 👋")
            break

        if not question:
            continue

        result = qa.ask(question)
        print(f"\n✅ Answer:\n{result['answer']}\n")

if __name__ == "__main__":
    # Install: pip install chromadb requests

    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'interactive':
        interactive_mode()
    else:
        main()
