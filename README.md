# Inline Telegram bot that allows you to find out user stats in Spotify
## What it Does

- Display the top of the user's most listened to tracks for different time periods.
- Display the top of the user's most listened to music artists for different time periods.
- Try it out now: [Spotify Statistic Bot](https://t.me/SpotifyStatisticBot)

## Installation

To install the required dependencies, run the following command:

```bash

pip install -r requirements.txt
```

### Dependencies

The project uses the following libraries:

- `aiogram`: Library for asynchronous interaction with Telegram Bot API.
- `cryptography`: Library for encrypting user refresh tokens.
- `Flask`: Framework for running a web server to authorize users via Spotify.
- `python-dotenv`: Tool for loading environment variables from a `.env` file.
- `Requests`: Library for making HTTP requests in Python.
- `SQLAlchemy`: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- `typing_extensions`: Backport of typing features from Python 3.5+ to older versions.

### Configuration

Fill in the `.env.example` file with your tokens and API keys, and then rename it to `.env.local`.

### Usage

1. Start the Flask web server:
```bash
  python web_server.py
```

2. Then, run the bot:
```bash
  python bot.py
```

You're all set! Users can authenticate through Spotify to access their statistics and share them with friends or in chats!

### License

This project is licensed under the MIT License. For more details, please see the [LICENSE](LICENSE) file.
