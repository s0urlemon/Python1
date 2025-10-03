import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from colorama import Fore,Style,init

init(autoreset=True)


movies = {

"title": [

"Toy Story", "Finding Nemo", "Shrek",

"Frozen", "Moana", "Coco",

"Zootopia", "Despicable Me", "Kung Fu Panda",

"The Lion King"

],

"genre": [

"animated family adventure", "animated family ocean adventure", "animated comedy fairy tale",

"animated musical fantasy", "animated musical adventure", "animated family music fantasy",

"animated family comedy mystery", "animated family comedy", "animated martial arts comedy",

"animated family adventure classic"

]

}

df=pd.DataFrame(movies)

vectorizer=TfidfVectorizer(stop_words="english")
tfidf_matrix=vectorizer.fit_transform(df["genre"])

cosine_sim=cosine_similarity(tfidf_matrix,tfidf_matrix)

def recommend_movie(movie_title):
    if movie_title not in df["title"].values:
        print(Fore.RED+f"Sorry!'{movie_title}' was not found in our kids movie database.")
        return
    idx=df[df["title"]==movie_title].index[0]

    sim_scores=list(enumerate(cosine_sim[idx]))

    sim_scores=sorted(sim_scores,key=lambda x: x[1],reverse=True)[1:4]

    print(Fore.CYAN+f"Recommended kids movies similar too '{movie_title}':")
    for i,score in sim_scores:
        print(Fore.GREEN+f"-> {df.iloc[i]['title']}"+Fore.YELLOW+f"(Similarity:{score:.2f})")
print(Fore.MAGENTA+Style.BRIGHT+"===Kids movie recommendation system===")
user_input=input(Fore.BLUE+"Enter a kid's movie you like:")
recommend_movie(user_input)