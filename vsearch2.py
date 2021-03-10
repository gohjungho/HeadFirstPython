def search4letters(phrase:str, letters:str='aeiou') -> set:
    # 두 번째 인자가 없는 경우 'aeiou'를 기본값으로 한다.
    '''Return a set of the 'letters' found in 'phrase'.'''
    return set(letters).intersection(set(phrase))


search4letters('hitch-hiker')

search4letters(letters='xyz',phrase='galaxy')
# 변수가 지정되어 있으면 순서가 뒤바뀌어도 상관없다. 

search4letters('life, the universe, and everything','o')
