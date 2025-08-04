# bot.py
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import os

seen_videos = set()

def handle_video(update: Update, context: CallbackContext):
    video = update.message.video
    if not video:
        return

    file_id = video.file_unique_id
    if file_id in seen_videos:
        update.message.delete()
    else:
        seen_videos.add(file_id)

def main():
    TOKEN = os.environ.get("BOT_TOKEN")  # Store token in environment
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.video, handle_video))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()