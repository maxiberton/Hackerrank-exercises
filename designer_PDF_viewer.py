def designerPdfViewer(h, word):

	return max(h["abcdefghijklmnopqrstuvwxyz".index(c)] for c in word) * len(word)


