'''
"There are only two hard things in Computer Science: cache invalidation and 
naming things." - Phil Karlton
'''

'''
"There are only two hard things in Computer Science: cache invalidation, naming 
things, and off-by-1 errors." - Leon Bambrick
'''


### Don't use single-letter variable names ###

def f(t):
    c = dict()
    for i in t.split():
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    return c


def count_words(text):
    word_counts = dict()
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


### Don't use abbreviations ###

def movie_relation_score(m1, m2):
    GW = 0.4
    YW = 0.1
    DW = 0.2
    WW = 0.3

    s = 0
    if m1.gen == m2.gen:
        s += GW
    if m1.yr == m2.yr:
        s += YW
    if m1.dir == m2.dir:
        s += DW
    for w in m1.writers:
        if w in m2.writers:
            s += WW
            break
    return s

def movie_relation_score(movie_1, movie_2):
    GENRE_WEIGHT = 0.4
    YEAR_WEIGHT = 0.1
    DIRECTOR_WEIGHT = 0.2
    WRITER_WEIGHT = 0.3

    score = 0
    if movie_1.genre == movie_2.genre:
        score += GENRE_WEIGHT
    if movie_1.year == movie_2.year:
        score += YEAR_WEIGHT
    if movie_1.director == movie_2.director:
        score += DIRECTOR_WEIGHT
    for writer in movie_1.writers:
        if writer in movie_2.writers:
            score += WRITER_WEIGHT
            break
    return score

### Descriptive names ###

def get_user(user_id):
    pass

def is_active(user):
    pass