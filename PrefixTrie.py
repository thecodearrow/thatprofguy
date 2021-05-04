
class PrefixTrie:
	def __init__(self):
		self.rootTrieNode={} 

	def insert(self,word):
		#O(l))
		trie=self.rootTrieNode
		for c in word:
			if(c not in trie):
				trie[c]={"count":0}
			trie=trie[c]
			trie["count"]+=1

		trie["#"]=True #end of word

	def search(self,word):
		#O(l)
		trie=self.rootTrieNode
		for c in word:
			if(c not in trie):
				return False
			trie=trie[c]

		return "#" in trie 

	def getCountStartsWith(self,prefix):
		trie=self.rootTrieNode
		for c in prefix:
			if(c not in trie):
				return 0
			trie=trie[c]

		return trie["count"]


words=["hello","help","hell","helen","try","trie","tree","trip"]

t=PrefixTrie()

for word in words:
#O(N*l) to build trie
	t.insert(word) #inserting word into trie 



print("Is helen present? ",t.search("helen"))
print("Is henry present? ",t.search("helen"))
print(t.getCountStartsWith("tri"))




