import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0
        
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"
    
    def build_vocab(self, texts: List[str]) -> None:
        spe = [self.pad_token, self.unk_token, self.bos_token, self.eos_token]
        for s in spe:
            if s not in self.word_to_id:
                self.word_to_id[s] = self.vocab_size
                self.id_to_word[self.vocab_size] = s
                self.vocab_size += 1

        for text in texts:
            words = text.split()
            for w in words:
                if w not in self.word_to_id:
                    self.word_to_id[w] = self.vocab_size
                    self.id_to_word[self.vocab_size] = w
                    self.vocab_size += 1
    
    def encode(self, text: str) -> List[int]:
        enclist = []
        words = text.split()
        for w in words:
            if w not in self.word_to_id:
                enclist.append(self.word_to_id[self.unk_token])
            else:
                enclist.append(self.word_to_id[w])
        return enclist
    
    def decode(self, ids: List[int]) -> str:
        declist = []
        for i in ids:
            declist.append(self.id_to_word[i])
        return " ".join(declist)
