"""ViSP FITS access for L0 data."""
from typing import Optional
from typing import Union

from astropy.io import fits
from dkist_processing_common.parsers.l0_fits_access import L0FitsAccess


class VispL0FitsAccess(L0FitsAccess):
    """
    Class to provide easy access to L0 headers.

    i.e. instead of <VispL0FitsAccess>.header['key'] this class lets us use <VispL0FitsAccess>.key instead

    Parameters
    ----------
    hdu :
        Fits L0 header object

    name : str
        The name of the file that was loaded into this FitsAccess object

    auto_squeeze : bool
        When set to True, dimensions of length 1 will be removed from the array
    """

    def __init__(
        self,
        hdu: Union[fits.ImageHDU, fits.PrimaryHDU, fits.CompImageHDU],
        name: Optional[str] = None,
        auto_squeeze: bool = True,
    ):
        super().__init__(hdu=hdu, name=name, auto_squeeze=auto_squeeze)

        self.number_of_modulator_states: int = self.header.get("VSPNUMST")
        self.file_id: str = self.header.get("FILE_ID")
        self.raster_scan_step: int = self.header.get("VSPSTP")
        self.total_raster_steps: int = self.header.get("VSPNSTP")
        self.modulator_state: int = self.header.get("VSPSTNUM")
        self.polarimeter_mode: str = self.header.get("VISP_006")
