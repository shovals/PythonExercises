# a game where each name starts with the last letter of the current name
from random import randint

shouldRestart = True
arrNames =[]
names = ['audino', 'bagon', 'baltoy', 'banette', 'bidoof', 'braviary', 'bronzor', 'carracosta', 'charmeleon',
'cresselia', 'croagunk', 'darmanitan', 'deino', 'emboar', 'emolga', 'exeggcute', 'gabite',
'girafarig', 'gulpin', 'haxorus', 'heatmor', 'heatran', 'ivysaur', 'jellicent', 'jumpluff', 'kangaskhan',
'kricketune', 'landorus', 'ledyba', 'loudred', 'lumineon', 'lunatone', 'machamp', 'magnezone', 'mamoswine',
'nosepass', 'petilil', 'pidgeotto', 'pikachu', 'pinsir', 'poliwrath', 'poochyena', 'porygon2',
'porygonz', 'registeel', 'relicanth', 'remoraid', 'rufflet', 'sableye', 'scolipede', 'scrafty', 'seaking',
'sealeo', 'silcoon', 'simisear', 'snivy', 'snorlax', 'spoink', 'starly', 'tirtouga', 'trapinch', 'treecko',
'tyrogue', 'vigoroth', 'vulpix', 'wailord', 'wartortle', 'whismur', 'wingull', 'yamask']

First = names[randint(1, 70)]
SearchLetter = First[-1]

print 'First name is: {0}'.format(First)
print 'Looking for names that start in: {0}'.format(SearchLetter)

for word in names:
    if word not in arrNames:
        if word[0] == SearchLetter:
            arrNames.append(word)
            SearchLetter = word[-1]

print arrNames