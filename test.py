WORDS = set(line.strip() for line in open('words.txt'))

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + replaces + inserts)


def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

if __name__ == "__main__":
    edit2_words = set(edits2('challenge'))
    print ([w for w in edit2_words if w in WORDS])
    print (len([w for w in edit2_words if w in WORDS]))