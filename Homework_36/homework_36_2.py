import asyncio
import aiohttp
import json
import time

HN_TOP = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM = "https://hacker-news.firebaseio.com/v0/item/{}.json"

async def fetch_json(session, url):
    async with session.get(url) as resp:
        return await resp.json()

async def fetch_comments(session, story_id):
    story = await fetch_json(session, HN_ITEM.format(story_id))
    results = []
    if story and "kids" in story:  # kids = список id коментарів
        tasks = [fetch_json(session, HN_ITEM.format(cid)) for cid in story["kids"]]
        comments = await asyncio.gather(*tasks)
        results.extend([c for c in comments if c])
    return results

async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        top_ids = await fetch_json(session, HN_TOP)
        top_ids = top_ids[:10]
        tasks = [fetch_comments(session, sid) for sid in top_ids]
        results = await asyncio.gather(*tasks)
        all_comments = [c for sublist in results for c in sublist]
        all_comments.sort(key=lambda c: c.get("time", 0))

        with open("hn_comments_async.json", "w", encoding="utf-8") as f:
            json.dump(all_comments, f, ensure_ascii=False, indent=2)

        print(f"Збережено {len(all_comments)} коментарів")
        print(f"Час виконання: {time.time() - start:.2f} секунд")

if __name__ == "__main__":
    asyncio.run(main())
