```python
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
TELEGRAM_API = os.getenv("TELEGRAM_API")
TELEGRAM_HASH = os.getenv("TELEGRAM_HASH")
DATABASE_URL = os.getenv("DATABASE_URL")
USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "")
DOWNLOAD_DIR = os.getenv("DOWNLOAD_DIR", "/usr/src/app/downloads/")
CMD_SUFFIX = os.getenv("CMD_SUFFIX", "")
AUTHORIZED_CHATS = os.getenv("AUTHORIZED_CHATS", "")
```
