# What is this?

Just a handy little script for mass-deleting any and all tweets you may have favourited.
Written by JonasMalmlof based on https://github.com/QuincyLarson/delete-tweets

# How To

1) Go to https://twitter.com/settings/your_twitter_data and request your data. It might take up to a day before you are able to download it.

2) Go to https://developer.twitter.com/en/apps and create an app.
Once created, go to its Keys and tokens and copy the "API Key", "API Secret key", "Access token", and "Access token secret" and paste them into lines 130 through 133 in unfavourite.py.

3) either create a virtual environment, or not. 

4) launch the program with "Python unfavourite.py -d year-month-day" (example: "-d 2018-12-31"). All twitter-likes before that day will be removed.

The more twitter-likes you have, the longer it will take. again, as an example, it took me between three and four months to remove 85,000 likes.
