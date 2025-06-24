import asyncio
import logging

from pyrogram import Client
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import InputStream, InputAudioStream
from pytgcalls.exceptions import NoActiveGroupCall

from CUTEXMUSIC import app
from CUTEXMUSIC.core.userbot import assistants
from config import GROUP_CALL_LIMIT

LOG = logging.getLogger(__name__)

class MusicBotCall:
    def __init__(self):
        self.clients = {}
        self.streams = {}

    def get_group_call(self, chat_id):
        return self.clients.get(chat_id)

    async def start_call(self, chat_id, audio_file):
        if chat_id not in self.clients:
            group_call = PyTgCalls(app)
            await group_call.start()
            self.clients[chat_id] = group_call
        else:
            group_call = self.clients[chat_id]

        try:
            await group_call.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        audio_file,
                    )
                ),
                stream_type=StreamType().local_stream,
            )
            LOG.info(f"[MUSIC] Joined group call in {chat_id}")
        except NoActiveGroupCall:
            LOG.error(f"[ERROR] No active group call in chat {chat_id}")
        except Exception as e:
            LOG.exception(f"[EXCEPTION] While joining group call: {e}")

    async def stop_call(self, chat_id):
        group_call = self.clients.get(chat_id)
        if group_call:
            try:
                await group_call.leave_group_call(chat_id)
                await group_call.stop()
                del self.clients[chat_id]
                LOG.info(f"[MUSIC] Left and stopped call in {chat_id}")
            except Exception as e:
                LOG.exception(f"[ERROR] Could not stop call: {e}")

CUTE = MusicBotCall()
