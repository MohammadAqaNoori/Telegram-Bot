from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import random
from datetime import datetime
import imghdr  # Keeping imghdr as requested

# Replace 'YOUR_API_TOKEN' with your actual Telegram Bot API token
API_TOKEN = '7950232025:AAGSyC_IJnyHsI7A1MyKgGZZRJntQ6RNP7Y'
print("hello world")
# Menu options
MENU_KEYBOARD = [
    ['📚 Help', '🌐 About'],
    ['🎲 Random Number', '📅 Date'],
    ['👤 Who are you?', '🎓 My Info'],
    ['💡 Features']
]

# Command to handle /start
async def start(update: Update, context: CallbackContext) -> None:
    reply_markup = ReplyKeyboardMarkup(MENU_KEYBOARD, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Welcome to the Smart Bot! 🚀\n\n"
        "I am here to assist you. Choose an option below: ",
        reply_markup=reply_markup
    )

# Command to handle /help
async def help_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "📌 Available Commands:\n"
        "/start - Start the bot\n"
        "/help - Get help\n\n"
        "You can also use the menu buttons below for quick access! 😊"
    )

# Handle menu options
async def handle_menu(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text == '📚 Help':
        await help_command(update, context)
    elif text == '🌐 About':
        await update.message.reply_text(
            "🤖 This is a smart menu-based Telegram bot designed to assist you.\n\n"
            "I can generate random numbers, provide the current date, and answer basic questions! 🚀"
        )
    elif text == '🎲 Random Number':
        random_number = random.randint(1, 100)
        await update.message.reply_text(f"🎲 Your random number is: **{random_number}**")
    elif text == '📅 Date':
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await update.message.reply_text(f"📅 Today's date and time is: **{current_date}**")
    elif text == '👤 Who are you?':
        await update.message.reply_text(
            "🤖 I am a smart Telegram bot, designed to help you with basic commands.\n\n"
            "I can provide random numbers, display the current date, and share useful information. 🚀"
        )
    elif text == '🎓 My Info':
        await update.message.reply_text(
            "👨‍🎓 **User Information:**\n"
            "👤 Name: M. Aqa Noori\n"
            "🎓 Field: Software Engineering\n"
            "🏫 University: COMSATS University, Islamabad\n\n"
            "📌 I am passionate about coding, AI, and technology! 🚀"
        )
    elif text == '💡 Features':
        await update.message.reply_text(
            "✨ **Bot Features:**\n"
            "✔️ Generate random numbers 🎲\n"
            "✔️ Show current date 📅\n"
            "✔️ Provide information about the user 🎓\n"
            "✔️ Answer common questions 🤖\n\n"
            "More features coming soon! 🚀"
        )
    else:
        await update.message.reply_text("⚠️ Sorry, I didn't understand that. Please use the menu or type /help.")

# Handle unknown commands
async def unknown(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("⚠️ Unknown command. Type /help for assistance.")

def main() -> None:
    # Create the Application and pass it your bot's token
    application = Application.builder().token(API_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Register message handler for menu options
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_menu))

    # Handle unknown commands
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
