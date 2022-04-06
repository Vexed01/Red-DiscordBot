import discord as _discord

from .. import __version__, version_info, VersionInfo, vance_version
from .config import Config

__all__ = ["Config", "__version__", "version_info", "VersionInfo"]

# Prevent discord PyNaCl missing warning
_discord.voice_client.VoiceClient.warn_nacl = False
