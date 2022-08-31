# mad libs from Chapter 8 of Automate the Boring Stuff


import re, os
#regexes needed 

wordregex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

#establishing the text for the madlib
text = 'The ADJECTIVE panda walked to the NOUN and then VERB ADVERB. A nearby NOUN was unaffected by these events.'
textlist = wordregex.findall(text)

print('')
print(text)
print(' ')

#Loop over the text to find the regexes and then replace them

for groups in textlist:
    entry = input('Please input a ' + groups +' to mad lib.\n')
    text = text.replace(groups, entry, 1)


print(text)

pandalibs = open('madlibs.txt', 'w')
pandalibs.write(text)
pandalibs.close()