# NE PAS TOUCHER
originals = ['engagement', 'avenir', 'force', 'solidarite', 'unite', 'lumiere', 'identite', 'dialogue', 'crise', 'consensus', 'trajectoire', 'reconstruction', 'opinion', 'memoire', 'initiative', 'avenir', 'menace', 'refus', 'silence', 'affirmation', 'subversion', 'crise', 'stabilite', 'integrite', 'destin', 'proposition', 'cap', 'realite', 'territoire', 'cheminement', 'discipline', 'discipline', 'force', 'soutien', 'honneur', 'courage']
recording = ['engagement', 'affirmation', 'doute', 'solidarite', 'unite', 'realite', 'danger', 'dialogue', 'crise', 'consensus', 'trajectoire', 'reconstruction', 'opinion', 'memoire', 'initiative', 'avenir', 'menace', 'refus', 'realite', 'affirmation', 'subversion', 'crise', 'respect', 'integrite', 'nation', 'proposition', 'cap', 'appel', 'territoire', 'cheminement', 'loi', 'discipline', 'justice', 'crise', 'honneur', 'courage']
# NE PAS TOUCHER

result = ''


for i in range(len(originals)):
    
    if len(originals[i]) != len(recording[i]) :
        result = result + recording[i][0] + originals[i][0]
            
    elif originals[i] != recording[i] :
        result = result + recording[i][0] + originals[i][0]
    

print(result)