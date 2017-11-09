#!/usr/bin/env python
# -*- coding: utf-8 -*-

from link_processing import AffiliateLinkConverter, Connection
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome to the PCBC Link Bot.\n')
    update.message.reply_text('How to use the bot: ')
    update.message.reply_text('Send the bot a message with the following syntax.')
    update.message.reply_text('Link you want to convert \n Title for bitly')
    update.message.reply_text('You have to send the link and title in one message.')
    update.message.reply_text('Have fun!')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):

    message = update.message.text.splitlines()
    link = message[0]
    link_title = message[1]

    alc = AffiliateLinkConverter(link)
    (affiliateLink, description_note) = alc.get_affiliate_link()
    link_title = description_note + link_title

    c = Connection(access_token='8e2a2f5a74e7fdef0d945977940634e2cbb5cdb5')
    short_url = str(c.shorten_processed(affiliateLink, preferred_domain='bit.ly'))
    c.user_link_edit_processed(short_url, link_title, description_note)

    update.message.reply_text(link_title + "\n" + short_url)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("453047193:AAFGMknWHE1kJvPkSI9S1uvdx7S-C1YIOl0")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
