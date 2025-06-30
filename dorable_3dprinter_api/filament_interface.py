import dataclasses
from enum import Enum
from abc import ABC, abstractmethod
from functools import cache, cached_property
from typing import Any
from typing import Any, runtime_checkable


@dataclasses.dataclass(frozen=True)
class AMSFilamentSettings:
    """
    Dataclass for the filament settings
    """
    tray_info_idx: str
    nozzle_temp_min: int
    nozzle_temp_max: int
    tray_type: str


@dataclasses.dataclass
class IFilamentTray(ABC):
    """
    Abstract Base Class defining the interface for a Filament Tray data structure
    with associated behaviors.
    """
    # Define the expected attributes of the dataclass as abstract properties
    # (assuming they are read-only conceptually for the interface)
    @abstractmethod
    def __init__(self, k: float, n: int, tag_uid: str, tray_id_name: str,
                 tray_info_idx: str, tray_type: str, tray_sub_brands: str,
                 tray_color: str, tray_weight: str, tray_diameter: str,
                 tray_temp: str, tray_time: str, bed_temp_type: str,
                 bed_temp: str, nozzle_temp_max: int, nozzle_temp_min: int,
                 xcam_info: str, tray_uuid: str, cols: list[str] | None = None):
        # The __init__ is abstract to enforce the constructor signature.
        # In concrete implementations, dataclass will generate it.
        pass

    # Attributes that are part of the dataclass are typically not abstractproperties
    # if the concrete class is also a dataclass. You define them in the __init__ signature.
    # If the concrete class was *not* a dataclass, then you'd use abstract properties.

    @abstractmethod
    def keys(self) -> set[str]:
        """
        Abstract method to get the keys of the dataclass.
        """
        pass

    @abstractmethod
    def from_dict(self, d: dict[str, Any]):
        """
        Abstract method to initialize the dataclass from a dictionary.
        Note: Python's ABC does not enforce staticmethod/classmethod directly on abstract methods.
        The implementation will determine if it's static/class.
        """
        pass

    @property # Using @property to indicate it's accessed like an attribute
    @abstractmethod
    def filament(self) -> AMSFilamentSettings: # Use the interface for return type
        """
        Abstract method to get the filament information from the tray information.
        """
        pass


