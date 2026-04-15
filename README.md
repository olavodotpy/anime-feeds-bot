# Anime Feeds Bot

Anime Feeds Bot is a Discord bot that receives JSON data from the Anime Feeds RSS parsing system. 

It uses a clean architecture with **Cogs + Service Layer**, facilitating maintenance and growth of the bot.

## 🛠 Technologies Used

<!-- Python -->
<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python 3.10+">

<!-- discord.py -->
<img src="https://img.shields.io/badge/discord.py-2.7.1%20(Mar%202026)-5865F2?logo=discord&logoColor=white" alt="discord.py 2.7.1">

<!-- python-dotenv -->
<img src="https://img.shields.io/badge/python--dotenv-Environment%20Variables-ECD53F?logo=python&logoColor=black" alt="python-dotenv">

<!-- pydantic -->
<img src="https://img.shields.io/badge/Pydantic-Data%20Validation-E92063?logo=pydantic&logoColor=white" alt="pydantic">

---

## 🚀 How to run the bot

### 1. Clone the repository

```bash
git clone https://github.com/olavob/anime-feeds-bot.git
cd anime-feeds-bot
```

### 2. Create the virtual environment (recommended)

```bash
python -m venv venv
# Windows
# venv\Scripts\activate
# Linux / Mac
# source venv/bin/activate
```

3. Install the dependencies

```Bash
pip install -U -r requirements.txt
```

4. Configure the .env file

Create a .env file in the project root and add:

```env
DISCORD_TOKEN=TOKEN_HERE
```

Never commit your token to GitHub!

### 5. Start the bot

```Bash
python main.py
```

## 🤝 Contributing

Want to help improve the bot?

Feel free to open Issues or Pull Requests!

## 📄 License

This project is under the MIT license.

## 📬 Support / Contact

Discord: @olavobilac