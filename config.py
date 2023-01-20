"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "20256702")
        self.API_HASH: str = os.environ.get("API_HASH", "c81d1c06212c1c9624f44e159c651a5c")
        self.SESSION: str = os.environ.get("SESSION", "AQAIFq6kaoIHpDOAjfPVr_v9U--mvrH61_YllrWtudQ7tt4YoU5naku_BplTalLUBUo7Ln8omO3Dr29QdVee5keZlKThgfU2zsEL1MFSqur88B3g8ACb8txZrFM__xWMPBZLBJjH3D0QO-E5sFZIqjdqPRqGNzX8dKDiXqsf4YUnkv-9Ta3Wr-NmPtwxJe6n_H1RtwUdcUDEH_jr2Wlmz0HMIfw2NZtdElD0KruacQaBURyKLa_Bg8JiT-nXkLFYSi2tYS_KTnMenn4yRV9QwG4ZcIXC1jvkHK_-QO58uN3rJcJGPBu_Q93TKZ92Cw8jSicvya2vyAhjIWDsyzpSFdPTAAAAAV3FS3AA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "5955204118:AAH4hbCzi51OLMKWQxiJTje5o1zUq6v_Zx8")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", "5868178288").split() if id.isnumeric()
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", None)


config = Config()
