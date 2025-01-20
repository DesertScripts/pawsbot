from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)
API_ID: int
API_HASH: str

SLEEP_TIME: 
START_DELAY: 
 
RANDOM_DELAY_IN_RUN: 

ACC_STATS:
AUTO_TASK: 
NIGHT_MODE:
BAN_PROTECTION:
CONNECT_WALLETS:
NIGHT_TIME:
USE_PROXY_FROM_FILE:
YOUR_WALLET:



JOIN_TG_CHANNELS: 
USE_REF: 
REF_ID:



settings = Settings()
