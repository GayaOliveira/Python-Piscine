from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union

class DataStream(ABC):

    def is_str_list(self, data_batch: List[Any]) -> bool:
        for data in data_batch:
            if not isinstance(data, str):
                return False
        return True

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        filtered_data: List[Any] = []
        return filtered_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        instance_dict: Dict[str, Union[str, int, float]] = dict()
        return instance_dict


class SensorStream(DataStream):
    def __init__(self, sensor_id: str) -> None:
        super().__init__()
        self.sensor_id = sensor_id
        self.__readings: Dict[str, float] = {}

    # def __populate_dict(self, data_batch: List[str]) -> bool:
    #     for data in data_batch:
    #         separator_index = data.index(":")
    #         if separator_index == -1:
    #             return False
    #         key = data[:separator_index]
    #         try:
    #             value = float(data[separator_index + 1:])
    #             self.__readings[key] = self.__readings.get(key, 0) + value
    #         except ValueError:
    #             return False
    #     return True
    
    def __populate_dict(self, data_batch: List[str]) -> bool:
        for data in data_batch:
            separator_index = data.index(":")
            if separator_index == -1:
                return False
            key = data[:separator_index]
            try:
                value = float(data[separator_index + 1:])
                self.__readings[key] = self.__readings.get(key, 0) + value
            except ValueError:
                return False
        return True

    def count_readings(self, data_batch: List[Any]) -> int:
        if not self.is_str_list(data_batch):
            return 0
        if not self.__populate_dict(data_batch):
            if self.__readings:
                self.__readings.clear()
            return 0
        readings = len(data_batch)
        self.__readings.clear()
        return readings

    def process_batch(self, data_batch: List[Any]) -> str:
        if not self.is_str_list(data_batch):
            return "Invalid Batch..."
        if not self.__populate_dict(data_batch):
            if self.__readings:
                self.__readings.clear()
            return "Invalid Batch..."
        return f"{data_batch}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        pass

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.__readings
    

class TransactionStream(DataStream):
    pass


class EventStream(DataStream):
    pass


class StreamProcessor():
    def __init__(self, id1: str, id2: str, id3: str) -> None:
        self.sensor = SensorStream(id1)
        # self.trans = TransactionStream(id2)
        # self.event = EventStream(id3)

    def is_multi_sensor(self, multi_batch: Dict[str, List[str]]) -> bool:
        if len(multi_batch) > 1:
            return True
        return False
    
    @staticmethod
    def convert_values_to_float(data_dict: Dict[str, Union[str, int, float]]) -> Dict[str, float]:
        for value in data_dict.values():
            value = float(value)
        return data_dict

    @staticmethod
    def calc_average_temp(data_dict: Dict[str, float], readings: int) -> float:
        temp_sum = 0
        for parameter, value in data_dict.items():
            if parameter == "temp":
                temp_sum += value
        return temp_sum / readings

    def analyze_sensor_data(self, data_batch: List[str]) -> str:
        readings = self.sensor.count_readings(data_batch)
        self.sensor.process_batch(data_batch)
        data_dict = self.sensor.get_stats()
        data_dict = self.convert_values_to_float(data_dict)
        print(data_dict)
        analysis = "Sensor analysis: "
        analysis += f"{readings} readings"
        if len(data_dict) == 1:
            analysis = analysis[:-1]
        analysis += " processed, "
        analysis += f"avg temp: {self.calc_average_temp(data_dict, readings)}°C"
        return analysis

    def analyze_stream_stats(self, multi_batch: Dict[str, List[str]]) -> None:
        if not multi_batch or any(value is None for value in multi_batch.values()):
            return
        
        if not self.is_multi_sensor(multi_batch):
            env = ["Environmental Data", "Sensor"]
            if env[0] in multi_batch.keys():
                print(f"Initializing {env[1]} Stream...")
                id = self.sensor.sensor_id
                print(f"Stream ID: {id}, Type: {env[0]}")
                print(f"Processing sensor batch: {multi_batch[env[0]]}")
                print(self.analyze_sensor_data(multi_batch[env[0]]))


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    stream_processor = StreamProcessor("SENSOR_001", "TRANS_001", "EVENT_001")
    multidata_batch = {
        "Environmental Data": ["temp:22.5", "humidity:65", "pressure:1013", "temp: 27.5", "temp: 32"]
    }
    stream_processor.analyze_stream_stats(multidata_batch)
    # multidata_batch = {
    #     "Environmental Data": ["temp:22.5", "humidity:65", "pressure:1013"],
    #     "Financial Data": ["buy:100", "sell:150", "buy:75"],
    #     "System Events":  ["login", "error", "logout"]
    # }

if __name__ == "__main__":
    main()
