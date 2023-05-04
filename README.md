# chien-ami-analysis

This is an analyzer for Amis, built on python. Python code was written to mimic the behavior of https://github.swarthmore.edu/Ling073-sp23/ling073-ami which was built on Apertium tools. Instead of a lexd file, lexicons are written as txt files and patterns are implemented in python code (ami_analyser.py).

Usage: Download the new style txts and the code. Type "python ami_analyser.py" in a terminal.

Key for what the tags mean:
```
Morphological Transducer for Amis

Part of speech categories
<n>      Noun
<v>      Verb
<adj>    Adjective
<numb>   Number
<num>    Numeral
<prn>    Pronoun
<nm>     Noun Marker
<asp>    Aspect Marker
<np>     Proper Noun
<pr>     Preposition
<adv>    Adverb

<sent>   Sentence-ending punctuation
<guio>   Hyphen
<cm>     Comma
<apos>   Apostrophe
<quot>   Quotation mark
<lquot>  Left quotation mark
<rquot>  Right quotation mark
<lpar>   Left parenthesis
<rpar>   Right parenthesis

Number morphology
<pl>     Plural
<sg>     Singular

Pronoun
<pers>   Personal
<p1>     First person
<p2>     Second person
<p3>     Third person
<incl>   Inclusive
<excl>   Exclusive
<nom>    Nominative
<gen>    Genitive
<dat>    Dative
<pos>    Posessive
<dem>    Demonstrative
<prx>    proximal
<dst>    distal
<vis>    visible
<invs>   invisible

Voice
<av>     Actor voice
<uv>     Undergoer voice

Our Tags
<neg>    Negative
<impf>   imperfect
<perf>   perfect
<ant>    Anthroponym
<top>    Toponym
<al>     other Proper Names

Verb Tense
<prst>   perfective/stative tense
<will>   will (of the actor)
<futi>   future/imperative
<past>   past tense
<caus>   causative

<ins1>   Insturmental applicative 1
<ins2>   Insturmental applicative 2
<pat>    Patient Locative Applicative prefix
<loca>   location locative applicative prefix
<loc>    Locative applicative
<fact>   Factual Mood suffix
<um>     Commom Noun Marker
```

Link to the wiki page: https://wikis.swarthmore.edu/ling073/User:Lchien1/Final_project
