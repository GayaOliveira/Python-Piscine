#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Optional, Union


def is_collection(data: Any) -> bool:
    try:
        len(data)
        return True
    except Exception:
        return False


def is_numeric(data: Any) -> bool:
    if data.__class__.__name__ == "int" or data.__class__.__name__ == "float":
        return True
    return False


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        total_numbers = 0
        total_sum = 0
        if (self.validate(data)):
            try:
                total_sum += data            
                total_numbers += 1
            except TypeError:
                if (self.validate(data)):
                    for element in data:
                        total_numbers += 1
                        total_sum += element
            finally:
                result = f"Processed {total_numbers} numeric values"
                if total_numbers == 1:
                    result = result[:-1]
                result += f", sum={total_sum}, avg={total_sum / total_numbers}"
                return result
        return "Processing failed..."

    def validate(self, data: Any) -> bool:
        if is_numeric(data):
            return True
        if is_collection(data):
            for element in data:
                if not is_numeric(element):
                    return False
            return True
        return False

    def format_output(self, result: str) -> str:
        return result


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if (self.validate(data)):
            try:
                words = data.split()
                total_words = len(words)
                total_charac = 0
                for word in words:
                    total_charac += len(word)
                if total_words > 0:
                    total_charac += total_words - 1
            except Exception:
                return "Processing failed..."
            result = "Processed text: "
            result += f"{total_charac} characters, {total_words} words"
            if total_words == 1:
                result = result[:-1]
            return result
        return "Processing failed..."

    def validate(self, data: Any) -> bool:
        try:
            data.split()
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return result


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

    def format_output(self, result: str) -> str:
        return result


def main() -> None:
    print("\n\n==> Initializing Numeric Processor...\n")
    numeric_processor = NumericProcessor()
    num_tests: List[Any] = [
        [4, 5],
        5,
        [1, "a"],
        "5",
        {"key1": 1, "key2": 2}
    ]
    for test in num_tests:
        print(f"Processing data: {test}")
        output = numeric_processor.process(test)
        if output == "Processing failed...":
            print("Validation fail: Not numeric data")
        else:
            print("Validation: Numeric data verified")
        print(f"Output: {numeric_processor.format_output(output)}")
        print("--------------------------------------")

    print("\n\n==> Initializing Text Processor...\n")
    text_processor = TextProcessor()
    text_tests: List[Any] = [
        "Hello Nexus World",
        ["sun", "moon"],
        5,
        "",
        {"key1": 1, "key2": 2}
    ]
    for test in text_tests:
        print(f"Processing data: {test}")
        output = text_processor.process(test)
        if output == "Processing failed...":
            print("Validation fail: Not textual data")
        else:
            print("Validation: Text data verified")
        print(f"Output: {text_processor.format_output(output)}")
        print("--------------------------------------")

    print("\n\n==> Initializing Log Processor...\n")
    log_processor = LogProcessor()
    log_tests: List[Any] = [
        "INFO: File loaded successfully",
        "WARNING: Disk space running low",
        "ERROR: Connection timeout",
        "CRITICAL: System out of memory",
        "log",
        ["log1", "log2"]
    ]
    for test in log_tests:
        print(f"Processing data: {test}")
        output = log_processor.process(test)
        if output == "Processing failed...":
            print("Validation fail: Not log data")
        else:
            print("Validation: Log data verified")
        print((f"Output: {log_processor.format_output(output)}"))
        print("--------------------------------------")

    print("\n\n=== Polymorphic Processing Demo ===")
    print("\n==> Processing multiple data types through same interface...\n")
    element1: List[Any] = [[42, 4.2, 0.42], "num"]
    element2: List[Any] = ["Oops", "num"]
    element3: List[Any] = ["The secret agent", "text"]
    element4: List[Any] = [["secret", "agent"], "text"]
    element5: List[Any] = ["INFO: User login OK", "log"]
    element6: List[Any] = ["MISTAKE: it's wrong", "log"]

    multiple_data: List[List[Union[Any, str]]] = [
        element1,
        element2,
        element3,
        element4,
        element5,
        element6
    ]
    i = 0
    for entry in multiple_data:
        i += 1
        processor: Optional[DataProcessor] = None
        if entry[1] == "num":
            processor = numeric_processor
        elif entry[1] == "text":
            processor = text_processor
        else:
            processor = log_processor
        output = processor.process(entry[0])
        print(f"Result {i}: ", end="")
        print(processor.format_output(output))


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    main()
    print("\n\nFoundation systems online. Nexus ready for advanced streams.")
