from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CSVExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        csv_content = ""
        quantity = len(data)
        for i in range(quantity):
            info = data[i][1]
            csv_content += f"{info}"
            if i != quantity - 1:
                csv_content += ","
        print(csv_content)


class JSONExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        if not data:
            return
        json_list: List[Dict[str, str]] = []
        for index, info in data:
            pair = {f"item_{index}": info}
            json_list.append(pair)
        print(json_list)


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.processed_data: List[str] = []
        self.total: int = 0
        self.index: int = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.processed_data:
            return -1, ""
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
            self.total += 1
        else:
            for elem in data:
                self.processed_data.append(str(elem))
                self.total += 1


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
            self.total += 1
        else:
            self.total += len(data)
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
            self.total += 1
        else:
            for dic in data:
                log_level = dic['log_level']
                log_message = dic['log_message']
                ingested = f"{log_level}: {log_message}"
                self.processed_data.append(ingested)
                self.total += 1


class DataStream():

    def __init__(self) -> None:
        self.__processors: Dict[str, DataProcessor] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        if proc is None or proc in self.__processors.values():
            return
        if isinstance(proc, NumericProcessor):
            self.__processors["Numeric"] = proc
        if isinstance(proc, TextProcessor):
            self.__processors["Text"] = proc
        if isinstance(proc, LogProcessor):
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
            proc_types = ["Numeric", "Text", "Log"]
            for proc_type in proc_types:
                processor = self.__processors.get(proc_type)
                if processor:
                    print(f"{proc_type} Processor: ", end="")
                    total = processor.total
                    remaining = len(processor.processed_data)
                    print(f" total {total} items processed, ", end="")
                    print(f" remaining {remaining} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        if not self.__processors:
            print("No processor found, no data")
            return
        if plugin is None:
            print("No plugin found, no data")
            return
        proc_types = ["Numeric", "Text", "Log"]
        if isinstance(plugin, CSVExportPlugin):
            plugin_type = "CSV"
        elif isinstance(plugin, JSONExportPlugin):
            plugin_type = "JSON"
        else:
            plugin_type = "Unknown"
        for proc_type in proc_types:
            processor = self.__processors.get(proc_type)
            output_list: list[tuple[int, str]] = []
            if processor:
                for _ in range(nb):
                    if processor.processed_data:
                        output_list.append(processor.output())
                print(f"{plugin_type} Output:")
                plugin.process_output(output_list)


def main() -> None:

    print("Initialize Data Stream...\n")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    num_proc = NumericProcessor()
    stream.register_processor(num_proc)
    text_proc = TextProcessor()
    stream.register_processor(text_proc)
    log_proc = LogProcessor()
    stream.register_processor(log_proc)

    print("Send first batch of data on stream: ", end="")
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
    print(batch)
    print()
    stream.process_stream(batch)
    stream.print_processors_stats()

    nb = 3
    print(f"Send {nb} processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    stream.output_pipeline(nb, csv_plugin)
    print()
    stream.print_processors_stats()

    print("\nSend another batch of data: ", end="")
    batch = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {
                'log_level': 'ERROR',
                'log_message': '500 server crash'
            },
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(batch)
    print()
    stream.process_stream(batch)
    stream.print_processors_stats()

    nb = 5
    print(f"Send {nb} processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    stream.output_pipeline(nb, json_plugin)
    print()
    stream.print_processors_stats()


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===\n")
    main()
