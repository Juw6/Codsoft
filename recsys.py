import pandas as pd
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

# Loading the MovieLens dataset
url = "http://files.grouplens.org/datasets/movielens/ml-100k/u.data"
column_names = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv(url, sep='\t', names=column_names)

# Preparing the data for Surprise library
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

# Spliting the data into training and test sets
trainset, testset = train_test_split(data, test_size=0.25, random_state=42)

# Using KNNBasic algorithm for collaborative filtering
algo = KNNBasic()

# Training the algorithm on the training set
algo.fit(trainset)

# Function to get top-N recommendations for a given user
def get_top_n_recommendations(algo, user_id, n=10):
    # Get a list of all item ids
    item_ids = df['item_id'].unique()
    
    # Get a list of items the user has already rated
    user_rated_items = df[df['user_id'] == user_id]['item_id'].tolist()
    
    # Predict ratings for all items
    predictions = [algo.predict(user_id, iid) for iid in item_ids if iid not in user_rated_items]
    
    # Sort predictions by estimated rating
    predictions.sort(key=lambda x: x.est, reverse=True)
    
    # Get top-N recommendations
    top_n_recommendations = predictions[:n]
    
    return [(pred.iid, pred.est) for pred in top_n_recommendations]

# Loop to get user input and display recommendations
while True:
    user_input = input("Enter user ID to get recommendations (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    try:
        user_id = int(user_input)
        top_n_recommendations = get_top_n_recommendations(algo, user_id, n=10)
        print(f"Top-10 recommendations for user {user_id}:")
        for item_id, rating in top_n_recommendations:
            print(f"Item ID: {item_id}, Predicted Rating: {rating:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numerical user ID.")
