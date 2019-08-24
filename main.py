import data_download as down
import unzip
import analyze
import extract
import synthesize
import es_indexer as index
import os
import glob

# Path to files and identifiers from Archive.org
path_to_files = 'D:/Downloads/Test'
path_to_result_files = 'D:/Dokumente/Uni/Bachelorarbeit/BA/Code'
identifier_list = ['archiveteam-twitter-stream-2017-11', 'archiveteam-twitter-stream-2018-01', 'archiveteam-twitter-stream-2018-02']
es_index_name = 'test_tweet_results'

# Searchterms
st_bitcoin = ("Bitcoin", "bitcoin", "BTC", "btc")
st_litecoin = ("Litecoin", "Litecoin", "LTC", "ltc")
searchterm = st_litecoin

# File names for result files
rf_key_tweets = 'key_tweets.json'
rf_extracted_tweets = 'extracted_tweets.json'
rf_all_extracted_tweets = 'all_extracted_tweets.json'

def delete_files(path):
    file_path = path
    for item in glob.glob(file_path + '/**/*.json', recursive=True):
        os.remove(item)
    return

# Call functions
down.downloader(identifier_list)
unzip.extract_tar(path_to_files)
unzip.extract_bz2(path_to_files)
analyze.analyze_tweet_text(path_to_files, searchterm, rf_key_tweets)
delete_files(path_to_files)
extract.extract_key_info(rf_key_tweets, rf_extracted_tweets)
synthesize.synthesize_rf(path_to_result_files, rf_all_extracted_tweets)
index.index_to_es(es_index_name, rf_all_extracted_tweets)
