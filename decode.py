morsetab = {
					'a': '.-',
					'b': '-...',
					'c': '-.-.',
					'd': '-..',
					'e': '.',
					'f': '..-.',
					'g': '--.',
					'h': '....',
					'i': '..',
					'j': '.---',
					'k': '-.-',
					'l': '.-..',
					'm': '--',
					'n': '-.',
					'o': '---',
					'p': '.--.',
					'q': '--.-',
					'r': '.-.',
					's': '...',
					't': '-',
					'u': '..-',
					'v': '...-',
					'w': '.--',
					'x': '-..-',
					'y': '-.--',
					'z': '--..',
		'0': '-----',           ',': '--..--',
		'1': '.----',           '.': '.-.-.-',
		'2': '..---',           '?': '..--..',
		'3': '...--',           ';': '-.-.-.',
		'4': '....-',           ':': '---...',
		'5': '.....',           "'": '.----.',
		'6': '-....',           '-': '-....-',
		'7': '--...',           '/': '-..-.',
		'8': '---..',           '(': '-.--.-',
		'9': '----.',           ')': '-.--.-',
			 '_': '..--.-',
}

def morse(code):
	"""Return a tree representing the code. Each non-root, non-leaf node is a
	signal. Each leaf node is a letter encoded by the path from the root.

	>>> morse(abcde).pretty_print()
	None
	  .
		-
		  a
		e
	  -
		.
		  .
			.
			  b
			d
		  -
			.
			  c
	"""
	root = Tree(None)
	for letter, signals in sorted(code.items()):
		tree = root
		for signal in signals:
			matches = [b for b in tree.branches if b.entry == signal]
			if matches:
				assert len(matches) == 1
				tree = matches[0]
			else:
				branch = Tree(signal)
				tree.branches.append(branch)
				tree = branch
		tree.branches.append(Tree(letter))
	return root

def decode(signals, tree):
	"""Decode signals into a letter.

	>>> t = morse(abcde)
	>>> [decode(s, t) for s in ['-..', '.', '-.-.', '.-', '-..', '.']]
	['d', 'e', 'c', 'a', 'd', 'e']
	"""
	try:
		for signal in signals:
			tree = [b for b in tree.branches if b.entry == signal][0]
		leaves = [b for b in tree.branches if not b.branches]
		
		return leaves[0].entry
	except IndexError:
		return "valid code!"



class Tree:
	"""A tree with entry as its root value."""
	def __init__(self, entry, branches=()):
		self.entry = entry
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = list(branches)
	def __repr__(self):
		if self.branches:
			branches_str = ', ' + repr(self.branches)
		else:
			branches_str = ''
		return 'Tree({0}{1})'.format(self.entry, branches_str)


moresetree = morse(morsetab)

def signal_split(morese_string):
	def inner(morese_string,result):
		if not morese_string:
			return 
		if morese_string[0]==" ":
			result.append([])
			inner(morese_string[1:],result)
		else:
			result[-1].append(morese_string[0])
			inner(morese_string[1:],result)
	result=[[]]
	inner(morese_string,result)
	return result

def main1():
	whattosay=input("what is the code(press q to exit): ")
	if whattosay=='q':
		print("exit")
		exit()
	listresult=[decode(element,morse(morsetab)) for element in signal_split(whattosay)]
	for word in listresult:
		print(word, end=' ')
	print("")
	
	