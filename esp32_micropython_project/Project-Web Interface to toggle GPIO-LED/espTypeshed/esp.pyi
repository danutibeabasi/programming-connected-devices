"""
functions related to the ESP8266 and ESP32.

Descriptions taken from:
https://raw.githubusercontent.com/micropython/micropython/master/docs/library/esp.rst.
==================================

.. module:: esp
   :synopsis: functions related to the ESP8266 and ESP32

The `esp` module contains specific functions related to both the ESP8266 and 
ESP32 modules.  Some functions are only available on one or the other of these
ports.
"""

from typing import Any


def flash_erase(byte_offset, length_or_buffer): ...
def flash_read(byte_offset, length_or_buffer): ...
def flash_size() -> None: 
    """Read the total size of the flash memory."""
def flash_user_start() -> None: 
    """Read the memory offset at which the user flash space begins."""
def flash_write(byte_offset, bytes) -> None: ...
