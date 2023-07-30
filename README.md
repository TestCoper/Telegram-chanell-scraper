# Telegram Channel Scraper

This repository contains a Python script for scraping messages and media from specific Telegram channels and forwarding them to other channels. To get started, follow the instructions below:

## Prerequisites

- Python 3.x
- Pyrogram
- Requests
- PIL (Python Imaging Library)

## How to Use

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/TestCoper/Telegram-chanell-scraper.git
   cd Telegram-chanell-scraper
   ```

2. Install the required dependencies:

   ```
   pip install pyrogram requests Pillow
   ```

3. Run the `make.py` file to initialize your Pyrogram session:

   ```
   python make.py
   ```

   This will create a file named `my_account.session`, which will be used for authentication in subsequent runs.

4. After the `my_account.session` file is created, you can run the main bot script:

   ```
   python bot.py
   ```

## Configuration

Before running the bot, you need to set up the configuration in the `bot.py` file. Open `bot.py` in a text editor and modify the following variables:

- `idch`: Replace this with the target channel ID where you want to forward messages.
- `idch2`: Replace this with another target channel ID (optional) for additional forwarding.
- `token1`: Replace with your Telegram bot token for sending messages to the first channel.
- `token2`: Replace with your Telegram bot token for sending messages to the second channel (optional).

## How It Works

The `bot.py` script defines several functions, each corresponding to a specific Telegram channel that you want to scrape. Currently, it supports the following channels:
- `usd_iran`
- `lear_ir`
- `cryptoprice_live`
- `web3insider_fa`

Each function is decorated with `@app.on_message` and filters incoming messages to match the specified channel name. When a new message is received in one of the specified channels, the corresponding function is triggered.

The script then extracts the message content, modifies it if needed, and forwards it to the designated target channels specified by `idch` and `idch2`. For the `web3insider_fa` channel, the script also downloads and forwards any photos sent in the messages.

Please note that the script may require further modifications and adjustments based on the actual use case and channel structures.

## Disclaimer

This script is provided for educational and informational purposes only. The use of automated scripts to scrape and forward content from Telegram channels may violate Telegram's Terms of Service. Use it responsibly and at your own risk.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to fork and modify the code as needed.
