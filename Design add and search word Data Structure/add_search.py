import string
class WordDictionary:

    def __init__(self):
        self.val = ""
        self.children = {}
        self.end = False
        

    def addWord(self, word: str) -> None:
        if word:
            if word[0] in self.children:
                pass
            else:
                self.children[word[0]] = WordDictionary()
            self.children[word[0]].addWord(word[1:])
        else:
            self.end = True

    def search(self, word: str) -> bool:
        if word:
            if word[0] in self.children:
                return self.children[word[0]].search(word[1:])
            elif word[0] == ".":
                for c in string.ascii_lowercase:
                    if c in self.children:
                        if self.children[c].search(word[1:]):
                            return True
                        else:
                            continue
                return False
            else:
                return False
        else:
            # end of the search term
            return self.end
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
methods = ["addWord","addWord","addWord","addWord","search","search",
 "addWord","search","search","search","search","search","search"]
data = [["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]

for m, w in zip(methods, data):
    print(getattr(obj, m)(w[0]))

# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# param_2 = obj.search("pad")
# param_2 = obj.search("bad")
# param_2 = obj.search(".ad")
# param_2 = obj.search("b..")