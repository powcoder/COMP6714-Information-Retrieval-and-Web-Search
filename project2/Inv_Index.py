https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
from math import log, ceil
from collections import Counter, defaultdict

class InvertedIndex:
    def __init__(self,documents):
        ## Parameters...
        self.documents = documents
        self.ndocs = len(self.documents.values())
        self.inverted_index = self.index_documents()

    def index_documents(self):
        Tokens_dict = defaultdict(list)
        tf_score = defaultdict(list)
        Posting_dict = defaultdict(list)

        for doc_id, doc in self.documents.items():
            tokens = doc.split()
            for tok in tokens:
                Tokens_dict[doc_id].append(tok)
        Tokens_counter = {doc_id: Counter(doc) for doc_id, doc in Tokens_dict.items()}

        for doc_id, counter in Tokens_counter.items():
            for token, tf in counter.items():
                tf_score[token].append((doc_id, tf))

        for token in tf_score.keys():
            df = len(tf_score[token])
            for doc_id, tf in tf_score[token]:
                tfidf_value = ceil((1.0 + log(1.0 + log(tf)))) * ceil((1.0 + log(self.ndocs / (1 + df))))
                Posting_dict[token].append((doc_id, tfidf_value))
                
        for token in tf_score:
            Posting_dict[token].sort()
            
        return Posting_dict

    def get_inverted_index(self):
        return self.inverted_index

