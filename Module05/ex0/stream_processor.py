#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List


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
    
    def ingest(self, data: int | float | List[int | float]) -> None:
        if data and not self.validate(data):
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
        if data and not self.validate(data):
            raise Exception("Improper text data")
        elif isinstance(data, (str)):
            self.processed_data.append(data)
        else:
            self.processed_data.extend(data)


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if (self.validate(data)):
            separator = data.find(":")
            log = data[:separator]
            log_message = data[separator + 2:]
            result = f"[ALERT] {log} level detected: {log_message}"
            return result
        return "Processing failed..."

    def validate(self, data: Any) -> bool:
        logs = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        try:
            separator = data.find(":")
            log = data[:separator]
            if log in logs:
                return True
            return False
        except Exception:
            return False


def main() -> None:

    print("\n==> Testing Numeric Processor...")
    num_proces = NumericProcessor()
    print(f"Trying to validate input '42': {num_proces.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proces.validate("Hello")}")
    print(f"Trying to validate input '(4.5, -2)': {num_proces.validate((4.5, -2))}")
    print(f"Trying to validate input '[4.5, -2]': {num_proces.validate([4.5, -2])}")
    print(f"Trying to validate input 'None': {num_proces.validate(None)}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proces.ingest("foo")
    except Exception as err:
        print(f"Got exception: {err}")
    data1 = [1, 2, 3, 4, 5]
    print(f"Processing data: {data1}")
    num_proces.ingest(data1)
    times = 3
    print(f"Extracting {times} {'value' if times == 1 else 'values'}...")
    for _ in range(times):
        index, element = num_proces.output()
        print(f"Numeric value {index}: {element}")
    print()

    print("==> Testing Text Processor...")
    text_proces = TextProcessor()
    print(f"Trying to validate input '42': {text_proces.validate(42)}")
    print(f"Trying to validate input 'Hello': {text_proces.validate("Hello")}")
    print(f"Trying to validate input '('Hello', '42')': {text_proces.validate(("Hello", "42"))}")
    print(f"Trying to validate input '['Hello', '42']': {text_proces.validate(["Hello", "42"])}")
    print(f"Trying to validate input 'None': {text_proces.validate(None)}")
    print("Test invalid ingestion of number 500 without prior validation:")
    try:
        text_proces.ingest(500)
    except Exception as err:
        print(f"Got exception: {err}")
    data2 = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {data2}")
    text_proces.ingest(data2)
    times = 2
    print(f"Extracting {times} {'value' if times == 1 else 'values'}...")
    for _ in range(times):
        index, element = text_proces.output()
        print(f"Text value {index}: {element}")
    print()

    

    
    # print("\n\n==> Initializing Log Processor...\n")
    # log_processor = LogProcessor()
    # log_tests: List[Any] = [
    #     "INFO: File loaded successfully",
    #     "WARNING: Disk space running low",
    #     "ERROR: Connection timeout",
    #     "CRITICAL: System out of memory",
    #     "log",
    #     ["log1", "log2"]
    # ]
    # for test in log_tests:
    #     print(f"Processing data: {test}")
    #     output = log_processor.process(test)
    #     if output == "Processing failed...":
    #         print("Validation fail: Not log data")
    #     else:
    #         print("Validation: Log data verified")
    #     print((f"Output: {log_processor.format_output(output)}"))
    #     print("--------------------------------------")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    main()
