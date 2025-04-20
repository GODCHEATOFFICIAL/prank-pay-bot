
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

BOT_TOKEN = "8198822011:AAF3K-AXQVD_blPOCF0jkVa7whGVoioH7Gc"
FORCE_JOIN_CHANNEL = -1001857302142
SOURCE_CHANNEL_USERNAME = "Fakephonepay_paytm_gpay"
SPECIFIC_MESSAGE_ID = 17

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(FORCE_JOIN_CHANNEL, user_id)
        if member.status in ["member", "administrator", "creator"]:
            await send_verify_message(update, context)
        else:
            await send_join_prompt(update)
    except:
        await send_join_prompt(update)

async def send_join_prompt(update: Update):
    keyboard = [
        [InlineKeyboardButton("Join Channel", url="https://t.me/+hrIjYhMdgMthNDI1")],
        [InlineKeyboardButton("✅ Verify", callback_data="verify")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Join Our Official Channel For using it - https://t.me/+hrIjYhMdgMthNDI1\n\n also join this channel https://t.me/Fakephonepay_paytm_gpay After join click on verify botton 👇",
        reply_markup=reply_markup
    )

async def send_verify_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_user.id
    try:
        await context.bot.copy_message(
            chat_id=chat_id,
            from_chat_id=f"@{Fakephonepay_paytm_gpay}",
            message_id=SPECIFIC_MESSAGE_ID
        )
    except Exception as e:
        print(f"Error forwarding: {e}")
        await context.bot.send_message(chat_id=chat_id, text="Error forwarding message.")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    try:
        member = await context.bot.get_chat_member(FORCE_JOIN_CHANNEL, user_id)
        if member.status in ["member", "administrator", "creator"]:
            await send_verify_message(update, context)
        else:
            await query.message.reply_text("⛔️ First join the channel then click Verify.")
    except Exception as e:
        print(f"Verification error: {e}")
        await query.message.reply_text("⛔️ Error during verification. Try again later.")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
