import praw
import time

f = open("D://Github Details//basic-reddit-bot_details.txt","r")
lines = f.readlines()

reddit = praw.Reddit(client_id = "{}".format((lines[0]).strip()),
                     client_secret = "{}".format((lines[1]).strip()),
                     username = "{}".format((lines[2]).strip()),
                     password = "{}".format((lines[3]).strip()),
                     user_agent = "{}".format((lines[4]).strip()))

def search():
    schoice = input("Enter name of a subreddit: ").strip()
    subreddit = reddit.subreddit(schoice)
    hot_sub = subreddit.hot(limit = 5)

    for submission in hot_sub:
        if not submission.stickied:
            print("-"*100,
                  "\nTITLE: ",submission.title,
                  "\n\tUPVOTES: ",submission.ups,
                  "\n\tDOWNVOTES: ",submission.downs)
        try:
            for comment in submission.comments:
                print("\n\tCOMMENT: ",comment.body)
                try:
                    for reply in comment.replies:
                        print("\n\t\tREPLY: ",reply)
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


def stream():
    schoice = input("Enter name of a subreddit: ").strip()
    subreddit = reddit.subreddit(schoice)
    try:
        for comment in subreddit.stream.comments():
            print("-"*100,
                  "\nCOMMENT: ",comment.body)
            try:
                for reply in comment.replies:
                    print("\n\t\tREPLY: ",reply)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)

while True:
    choice = int(input("\n\nOptions are: \n\t1. Search a subreddit, get titles, upvotes, downvotes, comments. \n\t2. Stream comments of a subreddit. \n\t3. Exit \nEnter your choice: ").strip())

    if choice == 1:
        search()
    elif choice == 2:
        stream()
    else:
        print("Bye!")
        sleep(4)
        SystemExit

        