"""
Labsphere SRS-99-020 - Labsphere (2019)
=======================================

Defines the objects implementing support for *Labsphere (2019)* *Labsphere
SRS-99-020* dataset loading:

-   :class:`colour_datasets.loaders.DatasetLoader_Labsphere2019`
-   :func:`colour_datasets.loaders.build_Labsphere2019`

References
----------
-   :cite:`Labsphere2019` : Labsphere. (2019). Labsphere SRS-99-020.
    doi:10.5281/zenodo.3245875
"""

import numpy as np
import os

from colour import SpectralDistribution
from colour.hints import Boolean, Dict, Optional
from colour.utilities import tsplit

from colour_datasets.loaders import AbstractDatasetLoader
from colour_datasets.records import datasets

__author__ = "Colour Developers"
__copyright__ = "Copyright (C) 2019-2021 - Colour Developers"
__license__ = "New BSD License - https://opensource.org/licenses/BSD-3-Clause"
__maintainer__ = "Colour Developers"
__email__ = "colour-developers@colour-science.org"
__status__ = "Production"

__all__ = [
    "DatasetLoader_Labsphere2019",
    "build_Labsphere2019",
]


class DatasetLoader_Labsphere2019(AbstractDatasetLoader):
    """
    Defines the *Labsphere (2019)* *Labsphere SRS-99-020* dataset loader.

    Attributes
    ----------
    -   :attr:`colour_datasets.loaders.DatasetLoader_Labsphere2019.ID`

    Methods
    -------
    -   :meth:`colour_datasets.loaders.DatasetLoader_Labsphere2019.__init__`
    -   :meth:`colour_datasets.loaders.DatasetLoader_Labsphere2019.load`

    References
    ----------
    :cite:`Labsphere2019`
    """

    ID: str = "3245875"
    """
    Dataset record id, i.e. the *Zenodo* record number.
    """

    def __init__(self):
        super().__init__(datasets()[DatasetLoader_Labsphere2019.ID])

    def load(self) -> Dict[str, SpectralDistribution]:
        """
        Syncs, parses, converts and returns the *Labsphere (2019)*
        *Labsphere SRS-99-020* dataset content.

        Returns
        -------
        :class:`dict`
            *Labsphere (2019)* *Labsphere SRS-99-020* dataset content.

        Examples
        --------
        >>> from colour_datasets.utilities import suppress_stdout
        >>> dataset = DatasetLoader_Labsphere2019()
        >>> with suppress_stdout():
        ...     dataset.load()
        >>> len(dataset.content.keys())
        1
        """

        super().sync()

        sd_path = os.path.join(
            self.record.repository, "dataset", "SRS-99-020.txt"
        )

        values = tsplit(np.loadtxt(sd_path, delimiter="\t", skiprows=2))
        self._content = dict(
            [
                (
                    "Labsphere SRS-99-020",
                    SpectralDistribution(
                        values[1], values[0], name="Labsphere SRS-99-020"
                    ),
                ),
            ]
        )

        return self._content


_DATASET_LOADER_LABSPHERE2019: Optional[DatasetLoader_Labsphere2019] = None
"""
Singleton instance of the *Labsphere (2019)* *Labsphere SRS-99-020* dataset
loader.
"""


def build_Labsphere2019(load: Boolean = True) -> DatasetLoader_Labsphere2019:
    """
    Singleton factory that builds the *Labsphere (2019)* *Labsphere SRS-99-020*
    dataset loader.

    Parameters
    ----------
    load
        Whether to load the dataset upon instantiation.

    Returns
    -------
    :class:`colour_datasets.loaders.DatasetLoader_Labsphere2019`
        Singleton instance of the *Labsphere (2019)* *Labsphere SRS-99-020*
        dataset loader.

    References
    ----------
    :cite:`Labsphere2019`
    """

    global _DATASET_LOADER_LABSPHERE2019

    if _DATASET_LOADER_LABSPHERE2019 is None:
        _DATASET_LOADER_LABSPHERE2019 = DatasetLoader_Labsphere2019()
        if load:
            _DATASET_LOADER_LABSPHERE2019.load()

    return _DATASET_LOADER_LABSPHERE2019
