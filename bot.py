
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8198822011:AAF3K-AXQVD_blPOCF0jkVa7whGVoioH7Gc"
FORCE_JOIN_CHANNEL = -1001857302142
SOURCE_CHANNEL_ID = -1002297114392

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("✅ Verify", callback_data="verify")]])
    msg = (
        f"Join Our Official Channel For using it -\n"
        f"https://t.me/+hrIjYhMdgMthNDI1\n\n"
        "After join click on verify botton 👇"
    )
    await update.message.reply_text(msg, reply_markup=keyboard)

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.callback_query.from_user
    chat_member = await context.bot.get_chat_member(FORCE_JOIN_CHANNEL, user.id)

    if chat_member.status in ['member', 'administrator', 'creator']:
        try:
            async for message in context.bot.get_chat_history(SOURCE_CHANNEL_ID, limit=1):
                await context.bot.copy_message(
                    chat_id=update.callback_query.message.chat.id,
                    from_chat_id=SOURCE_CHANNEL_ID,
                    message_id=message.message_id
                )
                break
        except:
            await update.callback_query.message.reply_text("Error forwarding message.")
    else:
        await update.callback_query.answer("Please join the channel first!", show_alert=True)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(verify, pattern="verify"))
app.run_polling()
