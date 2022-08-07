import os
import sys

from banking.exception import BankingException
from banking.util.util import load_object

import pandas as pd


class BankingData:

    def __init__(self,
                 step: float,
                 amount: float,
                 newbalanceOrig: float,
                 newbalanceDest: float,
                 isFlaggedFraud: float
                 ):
        try:
            self.step = step
            self.amount = amount
            self.newbalanceOrig = newbalanceOrig
            self.newbalanceDest = newbalanceDest
            self.isFlaggedFraud = isFlaggedFraud
        except Exception as e:
            raise BankingException(e, sys) from e

    def get_banking_input_data_frame(self):

        try:
            banking_input_dict = self.get_banking_data_as_dict()
            return pd.DataFrame(banking_input_dict)
        except Exception as e:
            raise BankingException(e, sys) from e

    def get_banking_data_as_dict(self):
        try:
            input_data = {
                "step": [self.step],
                "amount": [self.amount],
                "newbalanceOrig": [self.newbalanceOrig],
                "newbalanceDest": [self.newbalanceDest],
                "isFlaggedFraud": [self.isFlaggedFraud]
                }
            return input_data
        except Exception as e:
            raise BankingException(e, sys)


class BankingPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise BankingException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise BankingException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            median_house_value = model.predict(X)
            return median_house_value[0]
        except Exception as e:
            raise BankingException(e, sys) from e