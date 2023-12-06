class Trie:

    def __init__(self):
        self.val = ""
        self.preds = {}
        self.end_of_word = False        

    def insert(self, word: str) -> None:
        if word[0] not in self.preds:
            self.preds[word[0]] = [{}, False]
        childs = self.preds[word[0]]

        for c in word[1:]:
            if c in childs[0]:
                pass
            else:
                childs[0][c] = [{}, False]
            childs = childs[0][c]
        childs[1] = True

    def search(self, word: str) -> bool:
        if word[0] in self.preds:
            childs = self.preds[word[0]]
        else:
            return False
        
        for c in word[1:]:
            if c in childs[0]:
                childs = childs[0][c]
            else:
                return False
        
        if childs[1]:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        if prefix[0] in self.preds:
            childs = self.preds[prefix[0]]
        else:
            return False
        
        for c in prefix[1:]:
            if c in childs[0]:
                childs = childs[0][c]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)