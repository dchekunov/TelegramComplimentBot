# TelegramComplimentBot

This is a tiny bot for Telegram which generates and sends out compliments to people who have contacted him. 

Messages are generated in the following form:

```*name*, *body* *compliment*!```

Uses cron for scheduling, so can be installed on Unix systems.

## Getting Started

Clone the repository, add your Telegram bot api key to ``bot.cfg``. 

Add the preferred names, message bodies and compliments to the dictionaries in ``dict`` folder.

Edit the ``cronjob.sh`` script with your Python installation location and the location of the ``sender.py`` file and run the script to add a job to cron. 

Next, run the ``listener.py`` for the bot to start listening. 

## Usage

Message the bot with '/start' to be added to the list of people receiving the compliments.

Message the bot with '/stop' to stop receiving compliments.
