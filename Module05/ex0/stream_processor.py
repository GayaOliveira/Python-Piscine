#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.processed_data: List[str] = []
        self.index: int = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        data = self.processed_data.pop(0)
        self.index += 1
        return self.index, data


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(item, (int, float)) for item in data)
        return False

    def ingest(
            self,
            data: int
            | float
            | List[int]
            | List[float]
            | List[Union[int, float]]
            ) -> None:
        if data is not None and not self.validate(data):
            raise Exception("Improper numeric data")
        elif isinstance(data, (int, float)):
            self.processed_data.append(str(data))
        else:
            for elem in data:
                self.processed_data.append(str(elem))


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(item, str) for item in data)
        return False

    def ingest(self, data: str | List[str]) -> None:
        if data is not None and not self.validate(data):
            raise Exception("Improper text data")
        elif isinstance(data, (str)):
            self.processed_data.append(data)
        else:
            self.processed_data.extend(data)


class LogProcessor(DataProcessor):

    def is_dict_str_str(self, item: Any) -> bool:
        if not isinstance(item, dict):
            return False
        mandatory_keys = {"log_level", "log_message"}
        if set(item.keys()) != mandatory_keys:
            return False
        return all(
            isinstance(k, str) and isinstance(v, str)
            for k, v in item.items()
        )

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return self.is_dict_str_str(data)

        if isinstance(data, list) and data:
            return all(self.is_dict_str_str(item) for item in data)

        return False

    def ingest(self, data: Dict[str, str] | List[Dict[str, str]]) -> None:
        if data is not None and not self.validate(data):
            raise Exception("Improper log data")
        elif isinstance(data, dict):
            log_level = data['log_level']
            log_message = data['log_message']
            ingested = f"{log_level}: {log_message}"
            self.processed_data.append(ingested)
        else:
            for dic in data:
                log_level = dic['log_level']
                log_message = dic['log_message']
                ingested = f"{log_level}: {log_message}"
                self.processed_data.append(ingested)


def main() -> None:

    print("\nTesting Numeric Processor...")
    num_proces = NumericProcessor()
    print(f"  Trying to validate input '42': {num_proces.validate(42)}")
    print(f"  Trying to validate input 'Hello': "
          f"{num_proces.validate('Hello')}")
    print(f"  Trying to validate input '(4.5, -2)': "
          f"{num_proces.validate((4.5, -2))}")
    print(f"  Trying to validate input '[4.5, -2]': "
          f"{num_proces.validate([4.5, -2])}")
    print(f"  Trying to validate input 'None': "
          f"{num_proces.validate(None)}")
    print("  Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proces.ingest("foo")   # type: ignore[arg-type]
    except Exception as err:
        print(f"  Got exception: {err}")
    data1 = [1, 2, 3, 4, 5]
    print(f"  Processing data: {data1}")
    num_proces.ingest(data1)
    times = 3
    print(f"  Extracting {times} {'value' if times == 1 else 'values'}...")
    for _ in range(times):
        index, element = num_proces.output()
        print(f"  Numeric value {index}: {element}")
    print()

    print("Testing Text Processor...")
    text_proces = TextProcessor()
    print(f"  Trying to validate input '42': {text_proces.validate(42)}")
    print(f"  Trying to validate input 'Hello': "
          f"{text_proces.validate('Hello')}")
    print(f"  Trying to validate input '('Hello', '42')': "
          f"{text_proces.validate(('Hello', '42'))}")
    print(f"  Trying to validate input '['Hello', '42']': "
          f"{text_proces.validate(['Hello', '42'])}")
    print(f"  Trying to validate input 'None': {text_proces.validate(None)}")
    print("  Test invalid ingestion of number 500 without prior validation:")
    try:
        text_proces.ingest(500)    # type: ignore[arg-type]
    except Exception as err:
        print(f"  Got exception: {err}")
    data2 = ['Hello', 'Nexus', 'World']
    print(f"  Processing data: {data2}")
    text_proces.ingest(data2)
    times = 2
    print(f"  Extracting {times} {'value' if times == 1 else 'values'}...")
    for _ in range(times):
        index, element = text_proces.output()
        print(f"  Text value {index}: {element}")
    print()

    print("Testing Log Processor...")
    log_proces = LogProcessor()
    print(f"  Trying to validate input 'Hello': "
          f"{log_proces.validate("Hello")}")
    print("  Test invalid ingestion of dict without prior validation:")
    try:
        log_proces.ingest({'log_level': 'NOTICE'})
    except Exception as err:
        print(f"  Got exception: {err}")
    data3 = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f"  Processing data: {data3}")
    log_proces.ingest(data3)
    times = 2
    print(f"  Extracting {times} {'value' if times == 1 else 'values'}...")
    for _ in range(times):
        index, element = log_proces.output()
        print(f"  Log entry {index}: {element}")
    print()


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    main()
