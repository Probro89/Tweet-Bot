import tweepy
import schedule
import time
import pytz

consumer_key = "Sp6PliK6A7WjFWmxafC86lh6v"
consumer_secret = 'J8rkTsgzdjjQAViXsljCf5DsIJI09sP4vf0j27gS9EssjMaErp'
access_token = '1744329967083917312-L8Zc8No6w5LE7syyoPlK1anFhxxNvN'
access_token_secret = 'xFBYIi8gLzut4RlcjQtFe7OJ84Vp1tlvAwqexCewufakV'

# Read the initial day count from the file
with open('/Users/yash/Twitter bott/day-count.txt', mode='r') as day_count_file:
    start = int(day_count_file.read() or 0)

with open('/Users/yash/Twitter bott/list of accomplisments.txt') as tweets:
    tweet_content = tweets.readlines()


def tweet():
    global start  # Use global variable to track the day count across function calls
    client = tweepy.Client(
        consumer_key=consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret)

    todays_tweet = tweet_content[start]
    start += 1

    text = f'''(This tweet is automated.)
    Currently I am learning Python. 
    Today I learned {todays_tweet}
    I made this Twitter bot from scratch by myself.
    #Python #Webdev #Webdevelopment #Bot #Twitter
    '''

    # Update the day count in the file
    with open('/Users/yash/Twitter bott/day-count.txt', mode='w') as day_count_file:
        day_count_file.write(str(start))

    client.create_tweet(text=text)


# Schedule the tweet to be posted every day at 12:00 PM in the "Asia/Kolkata" (Indian Standard Time) time zone
schedule.every().day.at("18:30").do(tweet).timezone = pytz.timezone('Asia/Kolkata')

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
