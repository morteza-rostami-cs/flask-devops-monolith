from environs import Env

env = Env()
env.read_env()  # read .env


class Settings:
    ENV_NAME = env.str("ENV_NAME", default="dev")


settings = Settings()  # singleton
