# Assign foobar which gives the output shown in the last example.
# Hint: Use the triple quote as the outermost quote
def underline(title):
    length = len(title)
    print title + '\n' + '_' * length

underline('hello')