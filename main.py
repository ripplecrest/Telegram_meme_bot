import praw
import telegram
import time
import asyncio

#reddit setup
reddit = praw.Reddit(
    client_id="<client_id>",
    client_secret="<client_secret>",
    user_agent="<app name>:v1.0 by u/<user name>")
#bot setup
bot = telegram.Bot(token="<token>")
channel_id = "<channel id>"
topic_id = "<topic id>"
# Async function to send meme
async def send_meme(bot, channel_id, topic_id, url, caption):
    await bot.send_photo(chat_id=channel_id, photo=url, caption=caption, message_thread_id=topic_id)

#main logic
async def main():
    subreddit = reddit.subreddit("memes+dankmeme+Wholesomememes+PrequelMemes+ProgrammerAnimemes")
    for post in subreddit.hot(limit=50):
        if not post.stickied and post.url.endswith((".jpg", ".png", ".gif")):
            await send_meme(bot, channel_id, topic_id, post.url, post.title)
            print(f"Posted: {post.title}")
            await asyncio.sleep(10)  # Wait time

    await reddit.close()  # Clean up

# Run the async loop
if __name__ == "__main__":
    asyncio.run(main())

