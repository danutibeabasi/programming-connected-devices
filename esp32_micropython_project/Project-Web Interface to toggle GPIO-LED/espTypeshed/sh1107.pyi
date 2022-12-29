# https://www.displayfuture.com/Display/datasheet/controller/SH1107.pdf

from micropython import const
from framebuf import FrameBuffer, MONO_VLSB, MONO_HMSB

SET_CONTRAST = const(0x81)
SET_ENTIRE_ON = const(0xA4)
SET_NORM_INV = const(0xA6)
SET_DISP = const(0xAE)
SET_DCDC_MODE = const(0xAD)
SET_MEM_MODE = const(0x20)
SET_PAGE_ADDR = const(0xB0)
SET_COL_LO_ADDR = const(0x00)
SET_COL_HI_ADDR = const(0x10)
SET_DISP_START_LINE = const(0xDC)
SET_SEG_REMAP = const(0xA0)
SET_MUX_RATIO = const(0xA8)
SET_COM_OUT_DIR = const(0xC0)
SET_DISP_OFFSET = const(0xD3)
SET_DISP_CLK_DIV = const(0xD5)
SET_PRECHARGE = const(0xD9)
SET_VCOM_DESEL = const(0xDB)

TEST_CHUNK = const(8)

# Subclassing FrameBuffer provides support for graphics primitives
# http://docs.micropython.org/en/latest/pyboard/library/framebuf.html
class SH1107(framebuf.FrameBuffer):
    def __init__(self, width, height, external_vcc): ...

    def init_display(self): ...

    def poweroff(self): 
        """power off the display, pixels persist in memory"""
    def poweron(self): 
        """power on the display, pixels redrawn"""

    def contrast(self, contrast : int): 
        """0: dim, 255: bright"""

    def show(self): 
        """write the contents of the FrameBuffer to display memory"""

    def show_page_mode(self): ...
    def show_vert_mode(self): ...
    def test_modified(self, offs, width): ...


class SH1107_I2C(SH1107):
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False): ...

    def write_cmd(self, cmd): ...

    def write_data(self, buf): ...
