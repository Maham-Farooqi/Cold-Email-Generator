import pandas as pd
import faiss
import numpy as np
from langchain_community.embeddings import HuggingFaceEmbeddings
class FaissDb:
    def __init__(self, file):
        self.file = file
        self.data = pd.read_csv(file)  
        self.dimension = 384  
        self.index = faiss.IndexFlatL2(self.dimension)  
        self.metadata = []  
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def get_embedding(self, text):
        embedding = self.embeddings.embed_query(text)
        return np.array(embedding, dtype='float32')

    def store_data(self):
        if len(self.metadata) == 0: 
            for _, row in self.data.iterrows():
                embedding = self.get_embedding(row["Techstack"])
                self.index.add(np.expand_dims(embedding, axis=0))
                self.metadata.append(row["Links"])

    def query_db(self, skills, n_results=2):
        if isinstance(skills, str): 
            skills = [skills]
        
        query_embedding = self.get_embedding(" ".join(skills))
        query_embedding = np.expand_dims(query_embedding, axis=0)  
        distances, indices = self.index.search(query_embedding, n_results)
        print(indices)
        results = [self.metadata[idx] for idx in indices[0] if idx >= 0 and idx < len(self.metadata)]
        print('k3',results)
        return results
if __name__ == "__main__":
    faiss_db = FaissDb(r'C:\Users\Lenovo\Desktop\python\coldEmailGenerator\resource\my_portfolio.csv')
    faiss_db.store_data()

    # Query the FAISS database
    skills_to_search = ["Python", "Machine Learning"]  # Example skills
    results = faiss_db.query_db(skills_to_search, n_results=2)

    # Output the matching links
    print("Matching Links:", results)
