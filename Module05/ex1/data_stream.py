from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.processed_data: List[str] = []
        self.index: int = 0

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


class DataStream():

    def __init__(self):
        self.__processors: Dict[str, DataProcessor] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        if proc is None or proc in self.__processors.values():
            return
        if isinstance(proc, NumericProcessor) \
                and "Numeric" in self.__processors.keys():
            self.__processors["Numeric"] = proc
        if isinstance(proc, TextProcessor) \
                and "Text" in self.__processors.keys():
            self.__processors["Text"] = proc
        if isinstance(proc, LogProcessor) \
                and "Log" in self.__processors.keys():
            self.__processors["Log"] = proc

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            successful = False
            for processor in self.__processors.values():
                if processor.validate(data):
                    processor.ingest(data)
                    successful = True
            if not successful:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{data}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.__processors:
            print("No processor found, no data")
        else:
            if self.__processors["Numeric"]:
                print("Numeric Processor: ", end="")
            if self.__processors["Text"]:
                print("Text Processor: ", end="")
            if self.__processors["Log"]:
                print("Log Processor: ", end="")


def main() -> None:

    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print()

    num_proc = NumericProcessor()
    print("Registering Numeric Processor\n")
    stream.register_processor(num_proc)
    batch = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    print("Send first batch of data on stream: ", end="")
    print(batch)
    stream.process_stream(batch)
    stream.print_processors_stats()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    main()
