from typing import NoReturn

import pandas as pd

FILE_NAME = "netflix.csv"


def convert_to_xlsx() -> NoReturn:
    """
    Converte arquivo para a extensão xlsx.
    :return: NoReturn
    """
    try:
        read_file = pd.read_csv(FILE_NAME)
        file_xlsx = FILE_NAME.replace("csv", "xlsx")
        read_file.to_excel(file_xlsx, index=False, header=True)
        print("Arquivo convertido!")
    except Exception as e:
        print(e)
        print("Arquivo não pode ser convertido!")


if __name__ == '__main__':
    convert_to_xlsx()
