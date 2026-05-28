from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = 8702001488:AAF5ns5aV96L-t_Q-Wam9VpYcYW2ZPjDPMM

seen_links = set()

async def check_duplicate(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message or not update.message.text:
        return

    text = update.message.text

    words = text.split()

    links = [
        w for w in words
        if "http://" in w or "https://" in w or "t.me/" in w
    ]

    for link in links:

        clean_link = link.strip().lower()

        if clean_link in seen_links:

            try:
                await update.message.delete()
            except:
                pass

            return

        seen_links.add(clean_link)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & (~filters.COMMAND), check_duplicate)
)

print("Bot running...")
app.run_polling()
