"""
functionality specific to the ESP32. See https://docs.micropython.org/en/latest/library/esp32.html 

Descriptions taken from:
https://raw.githubusercontent.com/micropython/micropython/master/docs/library/esp32.rst.
==================================

.. module:: esp32
   :synopsis: functionality specific to the ESP32

The `esp32` module contains functions and classes specifically aimed at
controlling ESP32 modules.
"""
from typing import Any

Node = Any

def wake_on_touch(wake) -> None:
    """Configure whether or not a touch will wake the device from sleep.
    *wake* should be a boolean value."""

def wake_on_ext0() -> None: 
    """Configure how EXT0 wakes the device from sleep.  *pin* can be `None`
    or a valid Pin object.  *level* should be `esp32.WAKEUP_ALL_LOW` or
    `esp32.WAKEUP_ANY_HIGH`."""

def wake_on_ext1() -> None: 
    """Configure how EXT1 wakes the device from sleep.  *pins* can be ``None``
    or a tuple/list of valid Pin objects.  *level* should be ``esp32.WAKEUP_ALL_LOW``
    or ``esp32.WAKEUP_ANY_HIGH``."""

def raw_temperature() -> None: 
    """Read the raw value of the internal temperature sensor, returning an integer."""
   
def hall_sensor() -> None: 
    """Read the raw value of the internal Hall sensor, returning an integer."""

def idf_heap_info() -> None: 
   """    Returns information about the ESP-IDF heap memory regions. One of them contains
    the MicroPython heap and the others are used by ESP-IDF, e.g., for network
    buffers and other data. This data is useful to get a sense of how much memory
    is available to ESP-IDF and the networking stack in particular. It may shed
    some light on situations where ESP-IDF operations fail due to allocation failures.
    The information returned is *not* useful to troubleshoot Python allocation failures,
    use `micropython.mem_info()` instead.

    The capabilities parameter corresponds to ESP-IDF's ``MALLOC_CAP_XXX`` values but the
    two most useful ones are predefined as `esp32.HEAP_DATA` for data heap regions and
    `esp32.HEAP_EXEC` for executable regions as used by the native code emitter.

    The return value is a list of 4-tuples, where each 4-tuple corresponds to one heap
    and contains: the total bytes, the free bytes, the largest free block, and
    the minimum free seen over time.

    Example after booting::

     >>> import esp32; esp32.idf_heap_info(esp32.HEAP_DATA)
        [(240, 0, 0, 0), (7288, 0, 0, 0), (16648, 4, 4, 4), (79912, 35712, 35512, 35108),
         (15072, 15036, 15036, 15036), (113840, 0, 0, 0)]"""

class NVS:
    def commit() -> None: ...
    def erase_key() -> None: ...
    def get_blob() -> None: ...
    def get_i32() -> None: ...
    def set_blob() -> None: ...
    def set_i32() -> None: ...

class Partition:
    def find() -> None: ...
    def get_next_update() -> None: ...
    def info(): 
        """Returns a 6-tuple ``(type, subtype, addr, size, label, encrypted)``."""
    def ioctl() -> None: ...
    def mark_app_valid_cancel_rollback() -> None: ...
    def readblocks() -> None: ...
    def set_boot() -> None: ...
    def writeblocks() -> None: ...

class RMT:
    def clock_div() -> None: ...
    def deinit() -> None: ...
    def loop() -> None: ...
    def source_freq() -> None: ...
    def wait_done() -> None: ...
    def write_pulses() -> None: ...

class ULP:
    def load_binary() -> None: ...
    def run() -> None: ...
    def set_wakeup_period() -> None: ...

