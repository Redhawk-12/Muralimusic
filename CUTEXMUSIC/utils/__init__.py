from .channelplay import register_channel_players
from .database import init_db, close_db
from .decorators import admin_only, handle_errors
from .formatters import (
    format_duration,
    time_to_seconds,
    bytes_to_human
)
from .inline import setup_inline_handlers
from .sys import (
    restart_bot,
    update_bot,
    get_logs
)

__all__ = [
    'register_channel_players',
    'init_db',
    'close_db',
    'admin_only',
    'handle_errors',
    'format_duration',
    'time_to_seconds',
    'bytes_to_human',
    'setup_inline_handlers',
    'restart_bot',
    'update_bot',
    'get_logs',
]

def setup_utils(app):
    """Initialize all utility modules"""
    init_db()
    setup_inline_handlers(app)
    # any other setup
