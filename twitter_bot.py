import tweepy
try:
    # for Python2
    from Tkinter import *    
except ImportError:
    # for Python3
    from tkinter import *

# providing twitter app keys
consumer_key = 'your twitter app key'
consumer_secret = 'your twitter app secret key'
access_token = 'your twitter access token'
access_token_secret = 'your twitter access secret token'

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# initializing tkinter
root  = Tk()

# GUI 
label1 = Label( root, text="Search")
E1 = Entry(root, bd =5)
label2 = Label( root, text="Number of Tweets")
E2 = Entry(root, bd =5)
label3 = Label( root, text="Response")
E3 = Entry(root, bd =5)
label4 = Label( root, text="Reply?")
E4 = Entry(root, bd =5)
label5 = Label( root, text="Retweet?")
E5 = Entry(root, bd =5)
label6 = Label( root, text="Favorite?")
E6 = Entry(root, bd =5)
label7 = Label( root, text="Follow?")
E7 = Entry(root, bd =5)

def getE1():
    return E1.get()
def getE2():
    return E2.get()
def getE3():
    return E3.get()
def getE4():
    return E4.get()
def getE5():
    return E5.get()
def getE6():
    return E6.get()
def getE7():
    return E7.get()


def mainFunction():
    getE1()
    search = getE1()
    getE2()
    numberOfTweets = getE2()
    numberOfTweets = int(numberOfTweets)
    getE3()
    response = getE3()
    getE4()
    reply = getE4()
    getE5()
    retweet = getE5()
    getE6()
    favorite = getE6()
    getE7()
    follow = getE6()

    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.retweet()
            print('Retweeted the tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.favorite()
            print('Favorite the tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

    tweetID = tweet.user.id 
    username = tweet.user.screen_name

    phrase = "I like this post"

    if reply == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweetID = tweet.user.id
                username = tweet.user.screen_name
                api.update_status('@' + username + " " + phrase, in_reply_to_status_id = tweetID)
                print("Replied with " + phrase)

            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
    if favorite == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweetID = tweet.user.id
                username = tweet.user.screen_name
                api.update_status('@' + username + " " + phrase, in_reply_to_status_id = tweetID)
                print("Replied with " + phrase)

            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
    if retweet == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweetID = tweet.user.id
                username = tweet.user.screen_name
                api.update_status('@' + username + " " + phrase, in_reply_to_status_id = tweetID)
                print("Replied with " + phrase)

            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break
    if follow == 'yes':
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                tweetID = tweet.user.id
                username = tweet.user.screen_name
                api.update_status('@' + username + " " + phrase, in_reply_to_status_id = tweetID)
                print("Replied with " + phrase)

            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

# sumbit button that call mainFucntion
submit = Button(root, text ="Submit", command = mainFunction)

# Packing 
label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
submit.pack(side = BOTTOM)
root.mainloop()




