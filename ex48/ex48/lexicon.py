def scan(input):
	words = input.split()
	lexicon = {'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
		'verb': ['go', 'stop', 'kill', 'eat'],
		'stop_word': ['the', 'in', 'of', 'from', 'at', 'it'],
		'noun': ['door', 'bear', 'princess', 'cabinet']}
	result = []
	for test_word in words:
		lower_word = test_word.lower()
		if lower_word in lexicon['direction']:
			result.append(('direction', test_word))
		elif lower_word in lexicon['verb']:
			result.append(('verb', test_word))
		elif lower_word in lexicon['stop_word']:
			result.append(('stop', test_word))
		elif lower_word in lexicon['noun']:
			result.append(('noun', test_word))
		elif lower_word.isnumeric():
			result.append(('number', int(test_word)))
		else:
			result.append(('error', test_word))
	return result		
