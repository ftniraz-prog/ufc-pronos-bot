import os
import json
import asyncio
from datetime import datetime, timedelta

import discord
from discord import app_commands
from discord.ext import tasks

# ============================================================
# CONFIGURATION
# ============================================================

TOKEN = os.getenv("DISCORD_TOKEN")
DATA_FILE = "data.json"

EMOJI_ROUGE = "🔴"
EMOJI_BLEU = "🔵"

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
