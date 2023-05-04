from proj_classes import word
from os import path, listdir


# store all the contents of text files in dictionary
def read_data(fname):
    with open("txts/new_style/" + fname) as f:
        lines = f.read().splitlines()
    return lines

def populate_dict():
    dir_list = listdir("txts/new_style/")
    lexicon = {}
    for fname in dir_list:
        data = read_data(fname) # list of strings ["text,tag1,tag2"]
        lexemes = []
        for line in data:
            splits = line.split(',')
            if len(splits) > 1:
                if splits[-1] in ["ay", "aw", "en", "an", "nan"]:
                    if len(splits) == 2: # the mood one is just different
                        lexeme = word(tags = [splits[0]], suffix = splits[-1])
                    else:
                        lexeme = word(splits[0],splits[1:-1],splits[-1])
                else:
                    lexeme = word(splits[0],splits[1:])
            else:
                lexeme = word(splits[0])
            lexemes.append(lexeme)
        lexicon[path.splitext(fname)[0]] = lexemes
    return lexicon

def make_verbs(lexicon):
    # pattern:
    # Negative?(1) Voice?(1) Causative?(1) VerbApplicatives?(1) VerbRoot [<v>:]
    # Negative?(2) Voice?(2) Causative?(2) VerbApplicatives?(2) AlsoVoice? Mood?
    verbs = [word(lexeme.text, ["v"], root = lexeme.text)
    for lexeme in lexicon["VerbRoot"]]
    opts = ["Negative","Voice","Causative","VerbApplicatives","AlsoVoice",
    "Mood"]
    for opt in opts:
        n = len(verbs)
        for i in range(n):
            verb = verbs[i]
            for lexeme in lexicon[opt]:
                verbs.append(word(lexeme.text + verb.text,
                verb.tags + lexeme.tags,
                lexeme.suffix,
                verb.root))
    return verbs

def make_pronouns(lexicon):
    # PosessionPrefixes?(1) PronounRoot(1) [<prn>:]
    # Dative(1) PronounRoot(1) [<prn>:]
    pronouns = [word(lexeme.text, ["prn"] + lexeme.tags, root = lexeme.text)
    for lexeme in lexicon["PronounRoots"]]
    n = len(pronouns)
    for i in range(n):
        pronoun = pronouns[i]
        for lexeme in lexicon["PosessionPrefixes"]:
            pronouns.append(word(lexeme.text + pronoun.text,
            pronoun.tags + lexeme.tags,
            lexeme.suffix,
            pronoun.root))
        for lexeme in lexicon["Dative"]:
            pronouns.append(word(lexeme.text + pronoun.text,
            pronoun.tags + lexeme.tags,
            lexeme.suffix,
            pronoun.root))
    return pronouns

def make_adj(lexicon):
    # AdjectiveRoot [<adj>:] Mood?
    adjs = [word(lexeme.text, ["adj"], root = lexeme.text)
    for lexeme in lexicon["AdjectiveRoot"]]
    n = len(adjs)
    for i in range(n):
        adj = adjs[i]
        for lexeme in lexicon["Mood"]:
            adjs.append(word(lexeme.text + adj.text,
            adj.tags + lexeme.tags,
            lexeme.suffix,
            adj.root))
    return adjs

def make_numbers(lexicon):
    # Numb?(1) NumberRoot [<numb>:] Numb?(2) Mood?
    numbers = [word(lexeme.text, ["numb"], root = lexeme.text)
    for lexeme in lexicon["NumberRoot"]]
    opts = ["Numb","Mood"]
    for opt in opts:
        n = len(numbers)
        for i in range(n):
            number = numbers[i]
            for lexeme in lexicon[opt]:
                numbers.append(word(lexeme.text + number.text,
                number.tags + lexeme.tags,
                lexeme.suffix,
                number.root))
    return numbers

def make_conjunctions(lexicon):
    # Conjunction [<conj>:]
    conjunctions = [word(lexeme.text, ["conj"], root = lexeme.text)
    for lexeme in lexicon["Conjunction"]]
    return conjunctions

def make_nouns(lexicon):
    # NounRoot [<n>:] Voice?(2) Causative?(2) Mood?
    nouns = [word(lexeme.text, ["n"], root = lexeme.text)
    for lexeme in lexicon["NounRoot"]]
    opts = ["Voice","Causative","Mood"]
    for opt in opts:
        n = len(nouns)
        for i in range(n):
            noun = nouns[i]
            for lexeme in lexicon[opt]:
                nouns.append(word(lexeme.text + noun.text,
                noun.tags + lexeme.tags,
                lexeme.suffix,
                noun.root))
    return nouns

def make_nounmarkers(lexicon):
    # MarkerCase?(1) NounMarkStem(1) [<nm>:] NounMarkStem(2) MarkerCase?(2)
    nounmarkers = [word(lexeme.text, ["nm"] + lexeme.tags, root = lexeme.text)
    for lexeme in lexicon["NounMarkStem"]]
    opts = ["MarkerCase"]
    for opt in opts:
        n = len(nounmarkers)
        for i in range(n):
            nounmarker = nounmarkers[i]
            for lexeme in lexicon[opt]:
                nounmarkers.append(word(lexeme.text + nounmarker.text,
                nounmarker.tags + lexeme.tags,
                lexeme.suffix,
                nounmarker.root))
    return nounmarkers

def make_aspectmarkers(lexicon):
    # AspectMark(1) [<asp>:] AspectMark(2)
    aspectmarks = [word(lexeme.text, ["asp"] + lexeme.tags, root = lexeme.text)
    for lexeme in lexicon["AspectMark"]]
    return aspectmarks

def make_propernouns(lexicon):
    # ProperNounRoot(1) [<np>:] ProperNounRoot(2)
    propers = [word(lexeme.text, ["np"] + lexeme.tags, root = lexeme.text)
    for lexeme in lexicon["ProperNounRoot"]]
    return propers

def make_dempronouns(lexicon): # demonstrative pronouns
    # [<prn>:] DemPronounStem(2) NounMarkStem?(2) MarkerCase?(2)
    dempros = [word(lexeme.text, ["prn"] + lexeme.tags, root = lexeme.text)
    for lexeme in lexicon["DemPronounStem"]]
    opts = ["NounMarkStem","MarkerCase"]
    for opt in opts:
        n = len(dempros)
        for i in range(n):
            dempro = dempros[i]
            for lexeme in lexicon[opt]:
                dempros.append(word(lexeme.text + dempro.text,
                dempro.tags + lexeme.tags,
                lexeme.suffix,
                dempro.root))
    return dempros

def make_prepositions(lexicon):
    # PrepositionRoot [<pr>:]
    prepositions = [word(lexeme.text, ["pr"], root = lexeme.text)
    for lexeme in lexicon["PrepositionRoot"]]
    return prepositions

def make_adverbs(lexicon):
    # AdverbRoot [<adv>:]
    adverbs = [word(lexeme.text, ["adv"], root = lexeme.text)
    for lexeme in lexicon["AdverbRoot"]]
    return adverbs

def write_out(forms):
    with open('output/output.txt', 'w') as f:
        for form in forms:
            formatted_tags = ""
            for tag in form.tags:
                formatted_tags += f'<{tag}>'
            f.write(form.root+formatted_tags+':'+form.text+form.suffix)
            f.write('\n')

def main():
    # read all the text files
    lexicon = populate_dict()
    # make all the different types of forms
    verbs = make_verbs(lexicon)
    pronouns = make_pronouns(lexicon)
    adjs = make_adj(lexicon)
    numbers = make_numbers(lexicon)
    conjunctions = make_conjunctions(lexicon)
    nouns = make_nouns(lexicon)
    nounmarkers = make_nounmarkers(lexicon)
    aspectmarkers = make_aspectmarkers(lexicon)
    propernouns = make_propernouns(lexicon)
    dempronouns = make_dempronouns(lexicon)
    prepositions = make_prepositions(lexicon)
    adverbs = make_adverbs(lexicon)
    # compile them all together
    forms = (verbs+pronouns+adjs+numbers+conjunctions+nouns+nounmarkers+
    aspectmarkers+propernouns+dempronouns+prepositions+adverbs)
    # write to an output txt
    write_out(forms)

    #print([(con.text+con.suffix, con.tags) for con in conjunctions])
    #print(len(conjunctions))



main()
