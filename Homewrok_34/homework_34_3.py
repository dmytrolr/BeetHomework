#https://api.pushshift.io/reddit/comment/search/ не працює.
# Я обрав альтернативний форум

import requests
import threading
import json

HN_TOP = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM = "https://hacker-news.firebaseio.com/v0/item/{}.json"

comments = []
lock = threading.Lock()

def fetch_comments(story_id):
    """Завантажує коментарі для однієї історії"""
    story = requests.get(HN_ITEM.format(story_id)).json()
    if "kids" in story:
        for comment_id in story["kids"]:
            comment = requests.get(HN_ITEM.format(comment_id)).json()
            if comment:
                with lock:
                    comments.append(comment)

def main():
    top_stories = requests.get(HN_TOP).json()
    threads = []
    for story_id in top_stories[:10]:
        t = threading.Thread(target=fetch_comments, args=(story_id,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    comments.sort(key=lambda c: c.get("time", 0))

    with open("hn_comments.json", "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

    print(f"Збережено {len(comments)} коментарів у hn_comments.json")

if __name__ == "__main__":
    main()
