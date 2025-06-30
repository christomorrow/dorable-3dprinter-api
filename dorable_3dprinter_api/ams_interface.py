"""
Defines abstract interfaces for AMS (Automated Material System)
and AMSHub data structures and their core behaviors.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List
from .filament_interface import IFilamentTray


class IAMS(ABC):
    """
    Abstract Base Class defining the interface for an Automated Material System (AMS).
    Any concrete AMS implementation must inherit from this class and implement
    all abstract methods and properties.
    """

    @abstractmethod
    def __init__(
        self, humidity: int, temperature: float, **kwargs: Dict[str, Any]
    ) -> None:
        """
        Abstract constructor for AMS. Concrete implementations must match this signature.
        :param humidity: The humidity reading of the AMS.
        :param temperature: The temperature reading of the AMS.
        :param kwargs: Additional keyword arguments, potentially including 'tray' data.
        """
        pass

    @property
    @abstractmethod
    def humidity(self) -> int:
        """Abstract property for the humidity reading of the AMS."""
        pass

    @property
    @abstractmethod
    def temperature(self) -> float:
        """Abstract property for the temperature reading of the AMS."""
        pass

    @property
    @abstractmethod
    def filament_trays(self) -> Dict[int, IFilamentTray]:
        """
        Abstract property for the dictionary of filament trays by index.
        Returns: A dictionary where keys are tray indices (int) and values are
                 IFilamentTray instances.
        """
        pass

    @abstractmethod
    def process_trays(self, trays: List[Dict[str, Any]]):
        """
        Abstract method to process a list of raw tray data dictionaries and
        populate the filament_trays.
        :param trays: A list of dictionaries, each representing raw tray data.
        """
        pass

    @abstractmethod
    def set_filament_tray(
        self,
        filament_tray: IFilamentTray,
        tray_index: int
    ) -> None:
        """
        Abstract method to set the filament tray at the given index.
        Will overwrite any existing tray at the given index.
        :param filament_tray: An instance of IFilamentTray describing the filament tray.
        :param tray_index: The index of the tray (e.g., 0-3 for a 4-slot AMS).
        """
        pass

    @abstractmethod
    def get_filament_tray(self, tray_index: int) -> IFilamentTray | None:
        """
        Abstract method to get the filament tray at the given index.
        If no tray exists at the index, return None.
        :param tray_index: The index of the filament tray.
        :return: IFilamentTray instance if found, otherwise None.
        """
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> IFilamentTray:
        """
        Abstract method to allow accessing filament trays using dictionary-like indexing.
        :param index: The index of the tray.
        :return: The IFilamentTray at the given index.
        :raises KeyError: If no tray exists at the index.
        """
        pass

    @abstractmethod
    def __setitem__(self, index: int, filament_tray: IFilamentTray) -> None:
        """
        Abstract method to allow setting filament trays using dictionary-like indexing.
        :param index: The index of the tray.
        :param filament_tray: The IFilamentTray instance to set.
        """
        pass


class IAMSHub(ABC):
    """
    Abstract Base Class defining the interface for an AMS Hub,
    which manages multiple AMS units.
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        Abstract constructor for AMSHub.
        """
        pass

    @property
    @abstractmethod
    def ams_hub(self) -> Dict[int, IAMS]:
        """
        Abstract property for the dictionary of AMS units by ID.
        Returns: A dictionary where keys are AMS IDs (int) and values are
                 IAMS instances.
        """
        pass

    @abstractmethod
    def parse_list(self, ams_dict: List[Dict[str, Any]]):
        """
        Abstract method to parse a list of raw AMS data dictionaries and
        populate the ams_hub.
        :param ams_dict: A list of dictionaries, each representing raw AMS data.
        """
        pass

    @abstractmethod
    def __getitem__(self, ind: int) -> IAMS:
        """
        Abstract method to allow accessing AMS units using dictionary-like indexing.
        :param ind: The ID of the AMS unit.
        :return: The IAMS instance for the given ID.
        :raises KeyError: If no AMS unit exists with the given ID.
        """
        pass

    @abstractmethod
    def __setitem__(self, ind: int, item: IAMS) -> None:
        """
        Abstract method to allow setting AMS units using dictionary-like indexing.
        :param ind: The ID of the AMS unit.
        :param item: The IAMS instance to set.
        """
        pass
