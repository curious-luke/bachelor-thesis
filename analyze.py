# This code filters JSON files for tweets which contain the term Bitcoin, bitcoin, btc or BTC
import os
import json
from pathlib import Path
from glob import iglob

def analyze_tweet_text (path, searchterms, result_file):
    path_to_json = path
    st = searchterms
    rf = result_file
    key_tweets = [] # Array for Key Tweets
    print("4. Analyze Tweets ...")

    # Search for JSON files
    print("     Importing data ...")
    rootdir = Path(path_to_json)
    json_files = list(rootdir.glob('**/*.json')) # List with all JSON Files

    # Start filter process
    print("     Filter process started ...")
    for index, js in enumerate(json_files):
        with open(os.path.join(path_to_json, js)) as json_file:
            for line in json_file:
                if line.strip():
                    tweet_line = json.loads(line)
                    line_items = tweet_line.items()

                # 1. Filter: Check for deleted tweets
                    for (k, v) in line_items:    # k = key, v = value
                        if k == "source":   # key = source

                # 2. Filter: Check if tweet has more than 140 characters (truncated = true)
                            if tweet_line['truncated'] == True:
                                tweet_text = tweet_line['extended_tweet']['full_text']
                            else:
                                tweet_text = tweet_line['text']

                # 3. Filter: Check if text contains any of the searchterms
                            if any(s in tweet_text for s in st):
                                key_tweets.append(tweet_line)
                            else:
                                continue
                        else:
                            continue

    # Write results to JSON file
    print("     Writing results to JSON ...")
    with open(rf, 'w', encoding="utf-8") as file:
        for item in key_tweets:
            file.write("%s\n" % json.dumps(item))
    print("     Number of Key Tweets: ")
    print(len(key_tweets))
    return
