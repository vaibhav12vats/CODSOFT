import pandas as pd
from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import KNNBasic
from surprise import accuracy

# Load data (assuming MovieLens dataset)
data = pd.read_csv('ratings.csv')  # Example CSV file with user, item, rating columns

# Create a Surprise Dataset
reader = Reader(rating_scale=(1, 5))
dataset = Dataset.load_from_df(data[['userId', 'movieId', 'rating']], reader)

# Train-test split
trainset, testset = train_test_split(dataset, test_size=0.2)

# Build and train the model (user-based collaborative filtering)
sim_options = {
    'name': 'cosine',
    'user_based': True
}
model = KNNBasic(sim_options=sim_options)
model.fit(trainset)

# Make predictions
predictions = model.test(testset)

# Evaluate the model
rmse = accuracy.rmse(predictions)
print('RMSE:', rmse)

# Generate recommendations for a user
user_id = 1
top_n = 10
user_ratings = data[data['userId'] == user_id]
user_items = set(user_ratings['movieId'])
unseen_items = list(user_items ^ set(model.get_neighbors(user_id, k=top_n)[1]))

# Display recommendations
recommendations = data[data['movieId'].isin(unseen_items)]['title'].unique()
print('Recommendations for User', user_id, ':')
for movie in recommendations:
    print('- ', movie)
