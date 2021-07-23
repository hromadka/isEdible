import pandas as pd

# brewery_id,brewery_name,review_time,review_overall,review_aroma,review_appearance,review_profilename,beer_style,review_palate,review_taste,beer_name,beer_abv,beer_beerid
df1 = pd.read_csv("beer_reviews-1.csv", usecols = ['beer_style','beer_name'])
df1.to_csv("beer_reviews_lite-1.csv",index=False)

df2 = pd.read_csv("beer_reviews-2.csv", usecols = ['beer_style','beer_name'])
df2.to_csv("beer_reviews_lite-2.csv",index=False)
