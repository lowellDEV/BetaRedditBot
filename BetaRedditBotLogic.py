import puniX #contains user info
import praw
reddit =None

def TestAuth():
    if reddit is None:
        Authenticate()
    user = reddit.user
    if user is not None:
        print(user.me())
        count =0
        for item in reddit.inbox.unread(limit=None):
            if isInstance(item, Comment):
                count= count+1
        print('Unread: '+ str(count))
        
      
def Authenticate():
    global reddit
    reddit = praw.Reddit(client_id=puniX.botID,
                     client_secret=puniX.botSecret,
                     password=puniX.password,
                     user_agent='pythonScript/BetaRedditBot by /u/'+puniX.username,
                     username=puniX.username)
