from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        text = "Output: "
        text += result
        return text


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        total_numbers = 0
        total_sum = 0
        if (self.validate(data)):
            print("Validation: Numeric data verified")
            try:
                num = float(data)
                total_numbers += 1
                total_sum += num
            except ValueError:
                return "Processing failed..."
            except TypeError:
                if (self.validate(data)):
                    for element in data:
                        num = float(element)
                        total_numbers += 1
                        total_sum += num
            finally:
                result = f"Processed {total_numbers} numeric values"
                if total_numbers == 1:
                    result = result[:-1]
                result += f", sum={total_sum}, avg={total_sum / total_numbers}"
                return result
        print("Validation fail: Not numeric data")
        return "Processing failed..."

    def validate(self, data: Any) -> bool:
        try:
            float(data)
            return True
        except ValueError:
            return False
        except TypeError:
            for element in data:
                try:
                    float(element)
                except ValueError:
                    return False
            return True
        except Exception:
            print("An unexpected error occurred")
            return False

    def format_output(self, result: str) -> str:
        text = "Output: "
        text += result
        return text


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if (self.validate(data)):
            print("Validation: Text data verified")
            try:
                words = data.split()
                total_words = len(words)
                total_charac = 0
                for word in words:
                    total_charac += len(word)
                total_charac += total_words - 1
            except Exception:
                return "Processing failed..."
            result = "Processed text: "
            result += f"{total_charac} characters, {total_words} words"
            if total_words == 1:
                result = result[:-1]
            return result
        print("Validation fail: Not textual data")
        return "Processing failed..."

    def validate(self, data: Any) -> bool:
        try:
            data.split()
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        text = "Output: "
        text += result
        return text


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("==> Initializing Numeric Processor...\n")
    numeric_processor = NumericProcessor()
    output = numeric_processor.process([4, 5])
    print(numeric_processor.format_output(output))
    print("--------------------------------------")
    output = numeric_processor.process(5)
    print(numeric_processor.format_output(output))
    print("--------------------------------------")
    output = numeric_processor.process([1, "a"])
    print(numeric_processor.format_output(output))
    print("--------------------------------------")
    output = numeric_processor.process("*")
    print(numeric_processor.format_output(output))
    print("--------------------------------------")
    output = numeric_processor.process({"key1": 1, "key2": 2})
    print(numeric_processor.format_output(output))

    print("\n\n==> Initializing Text Processor...\n")
    text_processor = TextProcessor()
    output = text_processor.process("Hello Nexus World")
    print(text_processor.format_output(output))
    print("--------------------------------------")
    output = text_processor.process(["sun", "moon"])
    print(text_processor.format_output(output))
    print("--------------------------------------")
    output = text_processor.process(5)
    print(text_processor.format_output(output))
    print("--------------------------------------")
    output = text_processor.process(None)
    print(text_processor.format_output(output))
    print("--------------------------------------")
    output = text_processor.process({"key1": 1, "key2": 2})
    print(text_processor.format_output(output))
