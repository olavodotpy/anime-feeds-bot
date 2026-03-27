# Anime Feeds Bot

Anime Feeds Bot is a Discord bot that receives JSON data from the Anime Feeds RSS parsing system. 

It uses a clean architecture with **Cogs + Service Layer**, facilitating maintenance and growth of the bot.

---

## 🚀 How to run the bot

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/your-discord-bot.git
cd your-discord-bot
```

### 2. Create the virtual environment (recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate
```

3. Install the dependencies

```Bash
pip install -U -r requirements.txt
```

4. Configure the .env file

Create a .env file in the project root and add:

```env
DISCORD_TOKEN=coloque_seu_token_aqui
```

Never commit your token to GitHub!

### 5. Start the bot

```Bash
python main.py
```

## 🛠 Technologies Used

Python 3.10+
discord.py 2.7.1 (March 2026)
python-dotenv
pydantic (validation)

## 🤝 Contributing

Want to help improve the bot?

Feel free to open Issues or Pull Requests!

## 📄 License

This project is under the MIT license.

## 📬 Support / Contact

Discord: @olavobilac