import puniX #contains user info
import praw
import re
"""Contains the logic for the bot"""
reddit =None 
topPosts =None 

def TestAuth():
    """Prints the from the results of Authenticate()"""
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
    """Authenticates the client and sets the reddit object"""
    global reddit
    reddit = praw.Reddit(client_id=puniX.botID,
                     client_secret=puniX.botSecret,
                     password=puniX.password,
                     user_agent='pythonScript/BetaRedditBot by /u/'+puniX.username,
                     username=puniX.username)
def AcquireTopPosts():
    """Grabs the top posts of all in the past hour"""
    global topPosts
    topPosts = reddit.subreddit('all').top('hour')
    
def TestAcquireTop():
    """Prints the from the results of AcquireTopPosts()"""
    if topPosts is None:
        AcquireTopPosts()
    for post in topPosts:
        print(post.author.name)
        
def GetPMUsers(new):
    """Get the usernames of redditors whose
    submissions reach the top page and 
    who have pm in thier username"""
    return GetXUsers(new,'pm')
    # if reddit is None:
        # Authenticate()
    # if topPosts is None or new is True:
        # AcquireTopPosts()
    # for post in topPosts:
        # if re.search(r'pm',post.author.name):
            # print(post.author.name)
    

def GetXUsers(new,x):
    """Get the usernames of redditors whose
    submissions reach the top page with 
    the specified string (x) in thier username"""
    users =[]
    if reddit is None:
        Authenticate()
    if topPosts is None or new is True:
        AcquireTopPosts()
    for post in topPosts:
        if re.search(re.compile(re.escape(x),re.IGNORECASE),post.author.name):
            users.append(post.author)
    return users

def TestGetPMUsers():
    """Prints the results of GetXUsers with 'pm' as
    the parameter"""
    TestGetUsers('pm')

def TestGetUsers(x):
    """Prints the results of GetXUsers with (x) as
    the parameter"""
    users = GetXUsers(True,x)
    for user in users:
        print(user.name)
    
