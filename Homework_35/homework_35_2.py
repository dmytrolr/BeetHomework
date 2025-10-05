import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor

HN_TOP = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM = "https://hacker-news.firebaseio.com/v0/item/{}.json"

def fetch_comments(story_id):
    """Завантажує коментарі для однієї історії"""
    story = requests.get(HN_ITEM.format(story_id)).json()
    results = []
    if story and "kids" in story:
        for comment_id in story["kids"]:
            comment = requests.get(HN_ITEM.format(comment_id)).json()
            if comment:
                results.append(comment)
    return results

def main_threads():
    top_stories = requests.get(HN_TOP).json()[:10]
    comments = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(fetch_comments, sid) for sid in top_stories]
        for future in as_completed(futures):
            comments.extend(future.result())

    comments.sort(key=lambda c: c.get("time", 0))

    with open("hn_comments_threads.json", "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

    print(f"[Threads] Збережено {len(comments)} коментарів")

if __name__ == "__main__":
    main_threads()


#ProcessPoolExecutor

def main_processes():
    top_stories = requests.get(HN_TOP).json()[:10]
    comments = []

    with ProcessPoolExecutor() as executor:
        results = executor.map(fetch_comments, top_stories)
        for res in results:
            comments.extend(res)

    comments.sort(key=lambda c: c.get("time", 0))

    with open("hn_comments_processes.json", "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

    print(f"[Processes] Збережено {len(comments)} коментарів")

if __name__ == "__main__":
    main_processes()
