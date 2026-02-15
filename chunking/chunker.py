import tiktoken
from config.config_loader import load_config


class TextChunker:
    def __init__(self, model_name="gpt-3.5-turbo"):
        self.config = load_config()
        self.chunk_token_limit = self.config["context"]["chunk_token_limit"]
        
        # 15% overlap default
        self.overlap_tokens = int(self.chunk_token_limit * 0.15)

        self.tokenizer = tiktoken.encoding_for_model(model_name)

    def tokenize(self, text):
        return self.tokenizer.encode(text)

    def detokenize(self, tokens):
        return self.tokenizer.decode(tokens)

    def chunk_document(self, document):
        """
        Takes a document dict:
        {
            "paper_id": "...",
            "text": "...",
            "metadata": {...}
        }

        Returns list of chunk dicts.
        """

        tokens = self.tokenize(document["text"])
        chunks = []

        start = 0
        chunk_id = 0

        while start < len(tokens):
            end = start + self.chunk_token_limit
            chunk_tokens = tokens[start:end]

            chunk_text = self.detokenize(chunk_tokens)

            chunk = {
                "chunk_id": f"{document['paper_id']}_chunk_{chunk_id}",
                "paper_id": document["paper_id"],
                "text": chunk_text,
                "metadata": document["metadata"]
            }

            chunks.append(chunk)

            # Move window forward with overlap
            start += self.chunk_token_limit - self.overlap_tokens
            chunk_id += 1

        return chunks

    def chunk_documents(self, documents):
        """
        Takes list of document dicts.
        Returns flattened list of chunk dicts.
        """
        all_chunks = []

        for doc in documents:
            doc_chunks = self.chunk_document(doc)
            all_chunks.extend(doc_chunks)

        return all_chunks
