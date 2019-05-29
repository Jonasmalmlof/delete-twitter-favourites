# What is this?

Just a handy little script for mass-deleting any and all tweets you may have favourited.
Written by JonasMalmlof based on https://github.com/QuincyLarson/delete-tweets

# How To

1) Go to https://twitter.com/settings/your_twitter_data and request your data. It might take up to a day before you are able to download it.

2) Move 'like.js' from the zip-file to the folder you downloaded this script to.

2b) edit the like.js and remove anything by the TweetID number. Leave the first row as "tweet_id", then followed by all the numbers.

3) Go to https://developer.twitter.com/en/apps and create an app.
Once created, go to its Keys and tokens and copy the "API Key", "API Secret key", "Access token", and "Access token secret" and paste them into lines 130 through 133 in unfavourite.py.

4) either create a virtual environment, or not. 

5) launch the program with "Python unfavourite.py -d year-month-day" (example: "-d 2018-12-31"). All tweets created before that day will be removed from your likes.

The more twitter-likes you have, the longer it will take. again, as an example, it took me between three and four months to remove 85,000 likes.


# to-do  
twitter has changed the format of the like.js file slightly since I created this script. I will see if I can update it so you don't have to edit the like.js any more (it used to be a simple find all-replace all operation. now they actually include the text of the tweet you've liked. so that's no longer possible.)