#!/bin/sh

(crontab -l 2>/dev/null; echo "15 * * * * /usr/local/bin/python3 /scripts/python/TelegramComplimentBot/sender.py") | crontab -
