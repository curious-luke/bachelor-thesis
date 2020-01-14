# bachelor_thesis
This repository contains the code pipeline from my prototype for a Twitter Text-Mining Tool that I developed in my bachelor thesis. Elasticsearch ist used for indexing the relevant documents and Kibana for displaying the final results in a dashboard.

Data source: https://archive.org/details/twitterstream

1. Setup your Elasticsearch cluster (local or in the cloud).

2. Configure all relevant variables in the Code Setup:
* Path to files for downloaded datasets
* Identifiers for the datasets you want to analyze from archive.org
* Index name for Elasticsearch 
* Searchterms that the Tweets should be analyzed with

3. Setup the config file for archive.org with your user name and passwort.

4. Execute code.

5. Run Kibana on your Elasticsearch cluster and create visualizations a dashboard.

6. View final results in your dashboard in Kibana.
_____________________________________________________________________________________________________________________

Elasticsearch version 6.6.0 (https://www.elastic.co/de/downloads/elasticsearch)

Kibana version 6.6.0 (https://www.elastic.co/de/downloads/kibana)
