import pandas as pd

from src import utils
from src.heuristics import Mean
from src.object_storage import S3ObjectStorage
from src.logger import logging
from settings import Settings


settings = Settings()
logger = logging.getLogger(settings.LOGGER)


def main():
    # Read from S3
    news_parsed_data = S3ObjectStorage().get(
        bucket=settings.BUCKET,
        path=f"chat-responses/{settings.RUN_ID}-gpt-responses.csv",
    )
    if not news_parsed_data:
        return

    scores_df = pd.read_csv(news_parsed_data)

    # Apply heuristic
    mean = Mean.apply(scores_df)
    score_df = pd.DataFrame({"score": [mean]})

    # Save on S3
    utils.save_object(
        object_storage=S3ObjectStorage(),
        key="mean-score.csv",
        obj=score_df,
    )


if __name__ == "__main__":
    main()
