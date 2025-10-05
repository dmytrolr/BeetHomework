import requests
import json
import time

#пашфіт теж не працює, виводить пустий [], тому додаю ще HackerNews
# --- Reddit / Pushshift ---
SUBREDDIT = "python"
PUSHSHIFT_URL = "https://api.pushshift.io/reddit/comment/search/"

reddit_comments = []
params = {
    "subreddit": SUBREDDIT,
    "size": 100,
    "sort": "asc",
    "sort_type": "created_utc"
}

print(f"Завантаження коментарів із r/{SUBREDDIT}...")

while True:
    response = requests.get(PUSHSHIFT_URL, params=params)
    data = response.json().get("data", [])

    if not data:
        break

    reddit_comments.extend(data)
    params["after"] = data[-1]["created_utc"]
    time.sleep(1)

print(f"Отримано {len(reddit_comments)} коментарів із Reddit")

with open(f"{SUBREDDIT}_comments.json", "w", encoding="utf-8") as f:
    json.dump(reddit_comments, f, ensure_ascii=False, indent=2)

# --- Hacker News ---
print("Завантаження коментарів із Hacker News...")

HN_TOP = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM = "https://hacker-news.firebaseio.com/v0/item/{}.json"

hn_comments = []
top_stories = requests.get(HN_TOP).json()

for story_id in top_stories[:5]:
    story = requests.get(HN_ITEM.format(story_id)).json()
    if "kids" in story:
        for comment_id in story["kids"][:10]:
            comment = requests.get(HN_ITEM.format(comment_id)).json()
            hn_comments.append(comment)

print(f"Отримано {len(hn_comments)} коментарів із Hacker News")

with open("hackernews_comments.json", "w", encoding="utf-8") as f:
    json.dump(hn_comments, f, ensure_ascii=False, indent=2)

print("Усі коментарі збережено")
