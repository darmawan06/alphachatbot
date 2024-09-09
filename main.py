from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# Fungsi untuk memulai bot
def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Post to Channel", callback_data='post_to_channel')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Choose an action:', reply_markup=reply_markup)

# Fungsi untuk menangani callback
def button(update: Update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'post_to_channel':
        # Ganti 'CHANNEL_USERNAME' dengan username channel Telegram Anda
        context.bot.send_message(chat_id='@Dikdik0607', text="This is a post from the bot!")
        query.edit_message_text(text="Posted to channel!")

# Fungsi utama untuk menjalankan bot
def main():
    # Ganti 'YOUR_API_TOKEN' dengan token API bot Anda
    updater = Updater('7320928904:AAHPC4ns3Iblbiv1hJuBJVdenCADBHtpuU0', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
