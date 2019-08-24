# This code extracts the Date, ID, Text, User-ID, User-Name and User-Timezone from a tweet
import json

def extract_key_info(source_file, result_file):
    sf = source_file
    rf = result_file
    raw_tweets = [] # Array for key tweets
    extracted_tweets = [] # Array for extracted tweets
    print("5. Extract key infos ...")

    # Import key tweets from JSON file
    with open(sf) as source:
        for line in source:
            if line.strip():
                raw_tweets.append(json.loads(line))
    print(len(raw_tweets))

    # Extract Date, ID, Text, User-ID, User-Name and User-Timezone
    print("     Extract Data ...")
    for i in range(len(raw_tweets)):
        # Text Attributes - Check if text contains more than 140 characters
        if raw_tweets[i]['truncated'] == True:
            tweet_text = raw_tweets[i]['extended_tweet']['full_text']
        else:
            tweet_text = raw_tweets[i]['text']

        # Tweet Key Values
        tweet_date = raw_tweets[i]['created_at']
        tweet_id = raw_tweets[i]['id']
        tweet_source = raw_tweets[i]['source']

        # Tweet User Attributes
        tweet_user_id = raw_tweets[i]['user']['id']
        tweet_user_name = raw_tweets[i]['user']['name']
        tweet_user_location = raw_tweets[i]['user']['location']
        tweet_user_url =  raw_tweets[i]['user']['url']
        tweet_user_description = raw_tweets[i]['user']['description']
        tweet_user_verified = raw_tweets[i]['user']['verified']
        tweet_user_follower_count = raw_tweets[i]['user']['followers_count']
        tweet_user_friends_count = raw_tweets[i]['user']['friends_count']
        tweet_user_favourites_count = raw_tweets[i]['user']['favourites_count']
        tweet_user_statuses_count = raw_tweets[i]['user']['statuses_count']
        tweet_user_created_at = raw_tweets[i]['user']['created_at']
        tweet_user_utc_offset = raw_tweets[i]['user']['utc_offset']
        tweet_user_timezone = raw_tweets[i]['user']['time_zone']
        tweet_user_geo_enabled = raw_tweets[i]['user']['geo_enabled']
        tweet_user_language = raw_tweets[i]['user']['lang']

        # Tweet Attributes
        tweet_geo = raw_tweets[i]['geo']
        tweet_coordinates = raw_tweets[i]['coordinates']
        tweet_place = raw_tweets[i]['place']
        tweet_quote_count = raw_tweets[i]['quote_count']
        tweet_reply_count = raw_tweets[i]['reply_count']
        tweet_retweet_count = raw_tweets[i]['retweet_count']
        tweet_favorite_count = raw_tweets[i]['favorite_count']
        #tweet_hastags = raw_tweets[i]['entities']['hastags']
        #tweet_urls = raw_tweets[i]['entities']['urls']
        tweet_language = raw_tweets[i]['lang']
        tweet_timestamp = raw_tweets[i]['timestamp_ms']

        # Create a new JSON-Object structure
        jsonobj = {
            "created_at": tweet_date,
            "id": tweet_id,
            "text": tweet_text,
            "source": tweet_source,
            "user": {
                "id": tweet_user_id,
                "name": tweet_user_name,
                "location": tweet_user_location,
                "url": tweet_user_url,
                "description": tweet_user_description,
                "verified": tweet_user_verified,
                "followers_count": tweet_user_follower_count,
                "friends_count": tweet_user_friends_count,
                "favourites_count": tweet_user_favourites_count,
                "statuses_count": tweet_user_statuses_count,
                "created_at": tweet_user_created_at,
                "utc_offset": tweet_user_utc_offset,
                "time_zone": tweet_user_timezone,
                "geo_enabled": tweet_user_geo_enabled,
                "lang": tweet_user_language,
                },
            "geo": tweet_geo,
            "coordinates": tweet_coordinates,
            "place": tweet_place,
            "quote_count": tweet_quote_count,
            "reply_count": tweet_reply_count,
            "retweet_count": tweet_retweet_count,
            "favorite_count": tweet_favorite_count,
            "lang": tweet_language,
            "timestamp_ms": tweet_timestamp,
        }

        extracted_tweets.append(jsonobj)

    # Write results to JSON file
    print("     Write JSON file ...")
    with open(rf, 'w', encoding="utf-8") as file:
        for item in extracted_tweets:
            file.write("%s\n" % json.dumps(item))
    print("     Number of extracted Tweets:")
    print(len(extracted_tweets))
    return
