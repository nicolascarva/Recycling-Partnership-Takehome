from classes import Pattern, Words



############# Testing
pattern = Pattern(['au', 'ou'])
words = Words('More results from stauckouverflow.com Is my pipfile suppoused to update if I do a pip insta')
pattern.match(words.my_words)
print(pattern.pattern_words, '/n', pattern.pattern_group)
############ Testing