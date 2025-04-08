languages = ['Python', 'Java', 'JavaScript']

# enumerate the list
enumerated_languages = enumerate(languages)

# convert enumerate object to list
print(list(enumerated_languages))

languages.sort(key=lambda x: x[1])
