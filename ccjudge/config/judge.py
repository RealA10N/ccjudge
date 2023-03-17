from pydantic import PositiveInt

from ccjudge.config.base import CCJudgeBaseConfigModel


class JudgeConfig(CCJudgeBaseConfigModel):
    max_queue_size: PositiveInt | None = 1024
