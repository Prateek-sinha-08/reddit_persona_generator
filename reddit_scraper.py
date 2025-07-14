import praw
from dotenv import load_dotenv
load_dotenv()
import os

def get_reddit_data(username):
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent="persona-generator-script"
    )

    user = reddit.redditor(username)
    user_data = {
        "posts": [],
        "comments": []
    }

    try:
        for submission in user.submissions.new(limit=50):
            user_data["posts"].append({
                "title": submission.title,
                "selftext": submission.selftext,
                "url": f"https://reddit.com{submission.permalink}"
            })

        for comment in user.comments.new(limit=100):
            user_data["comments"].append({
                "body": comment.body,
                "url": f"https://reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"Error fetching user data: {e}")

    return user_data