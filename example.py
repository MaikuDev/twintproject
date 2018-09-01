#import twint
import twint

# Configure
c = twint.Config()
c.Username = "rubiu5"
c.Since = "2017-01-01"
c.Until = "2018-09-01"
c.Search = "-filter:retweets AND -filter:replies"
# Run

data = twint.run.Search(c)

for tweet in data:
    print(tweet.preview)
    
