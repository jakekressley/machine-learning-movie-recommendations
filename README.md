# 🎥 Movie Recommendation System
This project takes a list of movies a user likes and recommends similar movies using cosine similarity on movie data. The system is powered by a CSV file containing movie information such as genres, cast, and other key features.

# Features
- 📊 Cosine Similarity: Finds movies similar to the five movies you enter.
- 🔍 Smart Search: Don’t worry if you make a typo in your movie titles; our closest-match algorithm will automatically correct it for a smooth experience.
- 📁 CSV Movie Data: Movie information is pre-loaded into the system.
- ⚡ Quick Setup: Run the entire project in a Docker container for seamless installation.

### Requirements
You'll need Docker installed on your machine. The Docker environment will handle all other dependencies for you.

Setup & Running the Program with Docker
Clone the repository:

```
git clone https://github.com/your-username/movie-recommendation.git
cd movie-recommendation
```
Build the Docker image:

```
docker build -t movie-recommender .
```
Run the Docker container:
```
docker run -it movie-recommender
```

Input the names of your favorite movies when prompted, and get recommendations instantly:

```bash
Enter your favorite movie name 1:
Enter your favorite movie name 2:
Enter your favorite movie name 3:
Enter your favorite movie name 4:
Enter your favorite movie name 5:
1 . The Dark Knight Rises
2 . Batman Begins
3 . The Prestige
4 . London Has Fallen
5 . Zodiac
6 . The Killer Inside Me
7 . The Cotton Club
8 . Superman
9 . Highway
10 . Batman Returns
```
