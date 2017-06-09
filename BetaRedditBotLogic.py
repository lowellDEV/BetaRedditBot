bot = __import__('BetaRedditBot')
import praw
import re
import sys
"""Contains the logic for the bot"""
count =0
def main():
    """Run the Logic"""
    bot.Authenticate()
    if bot.reddit is None:
        print("Authentication Failed, check Credentials File")
        sys.exit()
    
    global reddit
    reddit = bot.reddit
    search()

    
def search():
    """Search for users with pm in the username"""
    while True:
        pm = None
        pm = bot.searchForPM()
        if pm is not None:
            congratulate(pm)

def congratulate(pm):
    """Send Scripted Message to user"""
    msg= "Hello,\n This is a scripted message to greet people like you! I am curious to know if you have gotten your requested pms. Message back and you will get a human responder (probably).\n\nThanks!"
    bot.message(pm,"Congrats!",msg)
    count+=1
    
        
if __name__=="__main__":
    main():