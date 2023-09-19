from pandas import DataFrame

from .heuristic import Heuristic


class Mean(Heuristic):
    @staticmethod
    def apply(data: DataFrame) -> object:
        """
        Calculates the mean of a dataframe column

        Args:
            data (DataFrame): Input data

        Returns:
            object: Mean value
        """
        return data["scores"].mean()
