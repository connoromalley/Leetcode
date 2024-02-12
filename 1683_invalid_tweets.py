import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    newdf = tweets[tweets['content'].str.len()>15]
    
    return newdf[['tweet_id']]
