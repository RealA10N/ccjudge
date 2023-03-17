from typing import Type, TypeVar

import toml
from pydantic import BaseSettings, Field
from pydantic.env_settings import SettingsSourceCallable

from ccjudge.config.api import APIConfig
from ccjudge.config.judge import JudgeConfig

T = TypeVar('T', bound=BaseSettings)
DEFAULT_CCJUDGE_CONFIG = 'ccjudge.toml'


class CCJudgeConfig(BaseSettings):
    """ A class that describes the scheme of the CCJudge configuration file.
    The configuration is divided into multiple sub-configurations, like
    'api' and 'judge'. """

    api: APIConfig = Field(default_factory=APIConfig)
    judge: JudgeConfig = Field(default_factory=JudgeConfig)

    class Config:
        # To load certain fields from environment variables, the name of the
        # env variable should be prefixed with 'ccjudge_'
        env_prefix = "ccjudge_"
        env_nested_delimiter = "__"

        # It is possible to use .env files to load secrets that should not be
        # stored together with the general configurations file.
        env_file = '.env'

        @classmethod
        def customise_sources(
            cls,
            init_settings: SettingsSourceCallable,
            env_settings: SettingsSourceCallable,
            file_secret_settings: SettingsSourceCallable,
        ) -> tuple[SettingsSourceCallable, ...]:
            # The highest priority is for env variable, then the .env file,
            # and only then the toml configuration file.
            return env_settings, init_settings

    @classmethod
    def load(cls: Type[T], path: str = DEFAULT_CCJUDGE_CONFIG) -> T:
        """ Loads the configuration file from the current directory, and
        returns an instance of the configuration. Raises errors if there are
        validation errors. """

        with open(path, 'r') as file:
            return cls.parse_obj(toml.load(file))
