def words_with_letters(words: list, letters: str) -> list:
    """
       Given a list of words sorted in alphabetical order, and a string
    of required letters, 5ind and return the list of words that contain letters as a subsequence.
    """
    def is_subseq(word: str, letters: str):
        last_idx = -1
        for i in range(len(letters)):
            new_idx = word.find(letters[i], last_idx+1)
            if new_idx == -1:
                return False 
            last_idx = new_idx
        return True

    output = []
    for word in words:
        if is_subseq(word, letters):
            output.append(word)

    return output

word_list = ['booklore', 'booklores', 'folklore', 'folklores',
'kaliborite', 'kenlore', 'kiloampere', 'kilocalorie',
'kilocurie', 'kilogramme', 'kilogrammetre', 'kilolitre',
'kilometrage', 'kilometre', 'kilooersted', 'kiloparsec',
'kilostere', 'kiloware', 'bronchiectatic', 'bronchiogenic', 'bronchitic',
'ombrophilic', 'timbrophilic', 'azazel', 'azotetrazole', 'azoxazole',
'diazoaminobenzene', 'hazardize', 'razzmatazz']

print(words_with_letters(word_list, 'klore'))
print(words_with_letters(word_list, 'brohiic'))
print(words_with_letters(word_list, 'azaz'))
            
    
