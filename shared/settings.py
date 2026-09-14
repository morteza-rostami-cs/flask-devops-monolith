from environs import Env

env = Env()
env.read_env()  # read .env


class Settings:
    ENV_NAME = env.str("ENV_NAME", default="dev")
    DATABASE_URL = env.str("DATABASE_URL")
    REDIS_URL = env.str("REDIS_URL")
    RABBITMQ_URL = env.str("RABBITMQ_URL")


settings = Settings()  # singleton
