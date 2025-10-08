import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CourseRecommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path).head(2000)

        self.df['text'] = (
            self.df['title'].fillna('') + ' ' +
            self.df['duration'].fillna('') + ' ' +
            self.df['instructors_id'].astype(str)
        )

        # TF-IDF
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.vectorizer.fit_transform(self.df['text'])

        # Cosine similarity
        self.similarity = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def get_courses(self):
        return self.df['title'].tolist()

    def recommend(self, course_name, topn=5):
        matches = self.df[self.df['title'].str.lower() == course_name.lower()]
        if matches.empty:
            return []

        idx = matches.index[0]
        sim_scores = list(enumerate(self.similarity[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        recommended = []
        for i, score in sim_scores[1:topn+1]:
            recommended.append({
                'title': self.df.iloc[i]['title'],
                'rating': self.df.iloc[i]['rating'],
                'duration': self.df.iloc[i]['duration'],
                'image': self.df.iloc[i]['image'],
                'url': self.df.iloc[i]['url'],
                'score': float(score)
            })
        return recommended
