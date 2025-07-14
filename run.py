from reddit_scraper import get_reddit_data
from llm_analyzer import analyze_user_data_with_llm
from persona_builder import build_user_persona
import argparse
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser(description="Reddit User Persona Generator")
    parser.add_argument("--username", required=True, help="Reddit username (without /u/)")
    args = parser.parse_args()

    username = args.username

    print(f"\n Fetching data for user: u/{username}")
    reddit_data = get_reddit_data(username)

    if not reddit_data["posts"] and not reddit_data["comments"]:
        print(" No Reddit posts or comments found for this user.")
        return

    print("\n Analyzing posts and comments\n")
    analyzed_data = analyze_user_data_with_llm(reddit_data)

    print("\n Building persona...\n")
    build_user_persona(username, analyzed_data)

    print(f"\n Persona for u/{username} saved to output/{username}_persona.txt")

if __name__ == "__main__":
    main()
