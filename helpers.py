
def getMoviesString(movies):

    # Get the most popular movies
    movieCounts = dict()
    for movie in movies:
        movieCounts[movie] = movieCounts.get(movie, 0) + 1
    bestMovies = set()
    bestCount = 0
    for movie in movieCounts:
        if movieCounts[movie] > bestCount:
            bestCount = movieCounts[movie]
            bestMovies = {movie}
        elif movieCounts[movie] == bestCount:
            bestMovies.add(movie)
    
    # Process the movies
    processedMovies = []
    for movie in movies:
        movie = movie.strip()
        movie = movie.replace('_', ' ')
        movie = movie.title()
        processedMovies.append(movie)
    
    processedMovies.sort()

    # Construct the result
    result = ''
    for movie in processedMovies:
        if movie in bestMovies:
            result += f"🌟 {movie}\n"
        else:
            result += f"{movie}\n"
    
    return result

def sortDirectorsByMovies(directors):
    directorCounts = dict()
    for director in directors:
        directorCounts[director] = directorCounts.get(director, 0) + 1
    countsDirectors = [(directorCounts[director], director) 
                       for director in directorCounts]
    countsDirectors.sort(reverse = True)
    return [director for _, director in countsDirectors]


    


    

    