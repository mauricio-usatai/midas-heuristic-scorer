from abc import ABC, abstractmethod

from pandas import DataFrame


class Heuristic(ABC):
    """
    An "interface" for heuristics
    """

    @staticmethod
    @abstractmethod
    def apply(data: DataFrame) -> object:
        """
        Apply the heuristic to procided data

        Args:
            data (DataFrame): The data in which the heuristic
            will be applied to

        Returns:
            object: The calculated heuristic
        """
        raise NotImplementedError
