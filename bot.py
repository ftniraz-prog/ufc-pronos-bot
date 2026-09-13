import os
import sys
import json
import asyncio
from datetime import datetime, timedelta

print(">>> Le script bot.py a bien démarré", flush=True)

import discord
from discord import app_commands
from discord.ext import tasks

print(">>> discord.py importé avec succès, version :", discord.__version__, flush=True)

# ============================================================
# CONFIGURATION
# ============================================================

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    print(">>> ERREUR : la variable DISCORD_TOKEN est vide ou absente !", flush=True)
    sys.exit(1)
else:
    print(f">>> Token trouvé, longueur : {len(TOKEN)} caractères", flush=True)

DATA_FILE = "data.json"

EMOJI_ROUGE = "🔴"
EMOJI_BLEU = "🔵"

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
