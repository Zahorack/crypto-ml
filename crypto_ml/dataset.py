import os
import json
import shutil
import logging
import pandas as pd
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

from crypto_ml.config import constants
from crypto_ml.api import ApiIterator

LOG = logging.getLogger(__name__)


@dataclass
class DatasetSettings:
    """
    Wrapper used for storing metadata to separated json file
    """
    DATASET_STORAGE_PATH = constants.DATA_STORAGE_DIR
    DATASET_SETTINGS_FILE = 'dataset_settings.json'

    name: str
    version: int
    last_modified: str

    def to_dict(self):
        return asdict(self)

    def save(self):
        with open(os.path.join(self.DATASET_STORAGE_PATH, self.name, 'dataset_settings.json'), 'w') as f:
            json.dump(self.to_dict(), f, indent=2)


@dataclass
class Dataset:
    """
    Dataset class for generic data handling, storing from API iterator and storage
    """
    VERSION = constants.VERSION
    BATCH_SIZE = constants.BATCH_SIZE
    DATASET_SETTINGS_FILE = 'dataset_settings.json'
    DATASET_STORAGE_PATH = constants.DATA_STORAGE_DIR

    name: str

    def exists(self) -> bool:
        """
        Check if directory for dataset exists
        """
        dataset_dir = os.path.join(self.DATASET_STORAGE_PATH, self.name)

        if os.path.exists(dataset_dir):
            return True
        return False

    def initialize(self, overwrite: Optional[bool] = False):
        """
        Create dataset directory by name and path set in config
        """
        dataset_dir = os.path.join(self.DATASET_STORAGE_PATH, self.name)

        if os.path.exists(dataset_dir):
            if overwrite:
                shutil.rmtree(dataset_dir)
            else:
                LOG.error(f"Dataset {self.name} already exists!")
                return None

        os.makedirs(dataset_dir)

        DatasetSettings(name=self.name,
                        version=self.VERSION,
                        last_modified=str(datetime.now())).save()

    def create_from_api_iterator(self, api: ApiIterator):
        """
        Create dataset from API iterator and store as pandas parquet
        """
        samples_queue = []

        for sample in api.iterate():
            samples_queue.append(sample.to_dict())

            if len(samples_queue) >= self.BATCH_SIZE:
                df = pd.DataFrame(samples_queue)
                df.to_parquet(os.path.join())


Dataset(name='test').initialize()
