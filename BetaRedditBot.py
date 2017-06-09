DEV = __import__('puniXbot') #contains user info
import praw
import re
"""Contains the functions for the bot"""
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
    reddit = praw.Reddit(client_id=DEV.botID,
                     client_secret=DEV.botSecret,
                     password=DEV.password,
                     user_agent='pythonScript/BetaRedditBot by /u/'+DEV.username,
                     username=DEV.username)
def AcquireTopPosts(sub ='all',time='hour'):
    """Grabs the top posts of all in the past hour"""
    global topPosts
    topPosts = reddit.subreddit(sub).top(time)
    
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
    
def Message(user,subject,msg):
    """Send a message to user (user)"""
    reddit.redditor(user).message(subject,msg)

def TestMessage():
    """Send a message to user (user)"""
    Message(DEV.username,'TEST','TEST TEST TEST TEST')

def GetRedditObj():
    return reddit

def search():
    """Search with increase scope (to be optimized)"""
    users =[]
    if reddit is None:
        Authenticate()
    
    AcquireTopPosts()
    for post in topPosts:
        if re.search(re.compile(re.escape(x),re.IGNORECASE),post.author.name):
            users.append(post.author)
        removeDuplicates(users)
    if not users:
        AcquireTopPosts('all','day')
            for post in topPosts:
                if re.search(re.compile(re.escape(x),re.IGNORECASE),post.author.name):
                    users.append(post.author)
                removeDuplicates(users)
    if not users:
        AcquireTopPosts('all','week')
            for post in topPosts:
                if re.search(re.compile(re.escape(x),re.IGNORECASE),post.author.name):
                    users.append(post.author)
                removeDuplicates(users)
    if not users:
        AcquireTopPosts('all','month')
            for post in topPosts:
                if re.search(re.compile(re.escape(x),re.IGNORECASE),post.author.name):
                    users.append(post.author)
                removeDuplicates(users)
    return users

def removeDuplicates(userList):
    """Remove names that have already been pm'ed"""
    user = set(userList)
    master =set(masterList)
    unique = users -master
    userList =list(unique)
    masterList+= userList
    return userList
        
    
def main():
    print("TestAuth()")
    TestAuth()
    print("TestAuth()")
    raw_input('press enter to continue...')
    print("TestAcquireTop()")
    TestAcquireTop()
    raw_input('press enter to continue...')
    print("TestGetPMUsers()")
    TestGetPMUsers()
    raw_input('press enter to continue...')
    print("TestGetUsers('b')")
    TestGetUsers('b')
    raw_input('press enter to continue...')
    print("TestMessage()")
    TestMessage()
    print("Done")
    
    

if __name__=="__main__":
    main()