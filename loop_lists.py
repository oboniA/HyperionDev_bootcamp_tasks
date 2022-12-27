movies = ['Violet Evergarden', 'Ghibli Movies', 'Maquia', 'Before Trilogy', 'Intersteller']

for i in range(len(movies)):
    print(f"Movie: {movies[i]}")
    """ print(f"Movie {i+1}'s name: {movies[i]}") """

# reference: https://www.youtube.com/watch?v=W4qU4YeC-cs
for index, movie in enumerate(movies):
    print('Movie', index+1, ':', movie)