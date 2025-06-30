"""
Defines the abstract interface for 3D printer cameras.
"""

from abc import ABC, abstractmethod
from typing import Optional, Union


class IPrinterCamera(ABC):
    """
    Abstract Base Class defining the common interface for 3D printer cameras.
    Any concrete camera implementation must inherit from this class
    and implement all abstract methods and properties.
    """

    @abstractmethod
    def __init__(
        self,
        hostname: str,
        access_code: str,
        port: int = 6000,
        username: str = 'bblp'
    ) -> None:
        """
        Initializes the camera interface.
        :param hostname: The IP address or hostname of the printer camera.
        :param access_code: The access code/password for the camera.
        :param port: The port for camera connection (default 6000).
        :param username: The username for camera connection (default 'bblp').
        """
        pass

    @abstractmethod
    def start(self) -> bool:
        """
        Starts the camera streaming/worker thread.
        :return: True if the camera thread was started successfully, False if already running.
        """
        pass

    @abstractmethod
    def stop(self) -> None:
        """
        Stops the camera streaming/worker thread.
        """
        pass

    @property
    @abstractmethod
    def last_frame(self) -> Optional[bytes]:
        """
        Abstract property to get the last raw image frame received from the camera.
        Returns None if no frame is available yet.
        """
        pass

    @property
    @abstractmethod
    def is_alive(self) -> bool:
        """
        Abstract property to check if the camera streaming/worker thread is alive.
        """
        pass

    @abstractmethod
    def get_frame_as_base64(self) -> str:
        """
        Retrieves the latest camera frame as a Base64 encoded string.
        :return: A Base64 encoded string of the image frame.
        :raises Exception: If no frame is available.
        """
        pass

