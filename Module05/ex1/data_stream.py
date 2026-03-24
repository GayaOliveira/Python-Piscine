from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


class BatchError(Exception):
    pass


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
        return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:        
        return {}


class SensorStream(DataStream):
    def __init__(self, sensor_id: str) -> None:
        super().__init__()
        self.sensor_id = sensor_id
        self.__readings: List[List[str, float]] = []
        self.__available = ["temp", "humidity", "pressure"]

    def __populate_list(self, data_batch: List[str]) -> bool:
        try:
            for data in data_batch:
                separator_index = data.index(":")
                if separator_index == -1:
                    return False
                key = data[:separator_index]
                if key not in self.__available:
                    return False
                value = float(data[separator_index + 1:])
                self.__readings.append([key, value])
            return True
        except Exception:
            return False

    def count_readings(self, data_batch: List[Any]) -> int:
        if not self.is_str_list(data_batch):
            return 0
        if not self.__populate_list(data_batch):
            if self.__readings:
                self.__readings.clear()
            return 0
        num_readings = len(data_batch)
        self.__readings.clear()
        return num_readings

    def process_batch(self, data_batch: List[Any]) -> str:
        if not self.is_str_list(data_batch):
            raise BatchError("Invalid Batch Data")
        if not self.__populate_list(data_batch):
            if self.__readings:
                self.__readings.clear()
            raise BatchError("Invalid Batch Data")
        return f"{data_batch}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if not self.__readings:
            try:
                self.process_batch(data_batch)
            except Exception as err:
                print(err)
        filtered_list: List[Any] = []
        for element in self.__readings:
            if element[0] == criteria:
                filtered_list.append(element[1])
        return filtered_list
    
    def average_temp_readings(self) -> float:
        temp_list = self.filter_data(self.__readings, "temp")
        return sum(temp_list) / len(temp_list)
    
    def get_high_temp_alerts(self, limit: float = 50.0) -> List[float]:
        return [v for k, v in self.__readings if k == "temp" and v > limit]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        temp_list = self.filter_data(self.__readings, "temp")
        humidity_list = self.filter_data(self.__readings, "humidity")
        pressure_list = self.filter_data(self.__readings, "pressure")
        sensor_dict: Dict[str, List[float]] = {
            "temp": temp_list,
            "humidity": humidity_list,
            "pressure": pressure_list
        }
        return sensor_dict


class TransactionStream(DataStream):
    def __init__(self, sensor_id: str) -> None:
        super().__init__()
        self.sensor_id = sensor_id
        self.__operations: List[List[str, int]] = []
        self.__available = ["buy", "sell"]

    def __populate_list(self, data_batch: List[str]) -> bool:
        try:
            for data in data_batch:
                separator_index = data.index(":")
                if separator_index == -1:
                    return False
                key = data[:separator_index]
                if key not in self.__available:
                    return False
                value = int(data[separator_index + 1:])
                if value < 0:
                    return False
                self.__operations.append([key, value])
            return True
        except Exception:
            return False

    def count_operations(self, data_batch: List[Any]) -> int:
        if not self.is_str_list(data_batch):
            return 0
        if not self.__populate_list(data_batch):
            if self.__operations:
                self.__operations.clear()
            return 0
        num_operations = len(data_batch)
        self.__operations.clear()
        return num_operations

    def process_batch(self, data_batch: List[Any]) -> str:
        if not self.is_str_list(data_batch):
            raise BatchError("Invalid Batch Data")
        if not self.__populate_list(data_batch):
            if self.__operations:
                self.__operations.clear()
            raise BatchError("Invalid Batch Data")
        return f"{data_batch}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if not self.__operations:
            try:
                self.process_batch(data_batch)
            except Exception as err:
                print(err)
        filtered_list: List[Any] = []
        for element in self.__operations:
            if element[0] == criteria:
                filtered_list.append(element[1])
        return filtered_list
    
    def calc_net_flow(self) -> int:
        buy_list = self.filter_data(self.__operations, "buy")
        sell_list = self.filter_data(self.__operations, "sell")
        return sum(buy_list) - sum(sell_list)       

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        buy_list = self.filter_data(self.__operations, "buy")
        sell_list = self.filter_data(self.__operations, "sell")
        transaction_dict: Dict[str, List[int]] = {
            "buy": buy_list,
            "sell": sell_list
        }
        return transaction_dict


class EventStream(DataStream):
    def __init__(self, sensor_id: str) -> None:
        super().__init__()
        self.sensor_id = sensor_id
        self.__events: List[str] = []
        self.__available = ["login", "error", "logout"]

    def __populate_list(self, data_batch: List[str]) -> bool:
        try:
            for data in data_batch:                
                if data not in self.__available:
                    return False
                self.__events.append(data)
            return True
        except Exception:
            return False

    def count_events(self, data_batch: List[Any]) -> int:
        if not self.is_str_list(data_batch):
            return 0
        if not self.__populate_list(data_batch):
            if self.__events:
                self.__events.clear()
            return 0
        num_events = len(data_batch)
        self.__events.clear()
        return num_events

    def process_batch(self, data_batch: List[Any]) -> str:
        if not self.is_str_list(data_batch):
            raise BatchError("Invalid Batch Data")
        if not self.__populate_list(data_batch):
            if self.__events:
                self.__events.clear()
            raise BatchError("Invalid Batch Data")
        return f"{data_batch}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if not self.__events:
            try:
                self.process_batch(data_batch)
            except Exception as err:
                print(err)
        filtered_list: List[Any] = []
        for element in self.__events:
            if element == criteria:
                filtered_list.append(element)
        return filtered_list
    
    def count_error_events(self) -> int:
        event_list = self.filter_data(self.__events, "error")
        return len(event_list)       

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        login_list = self.filter_data(self.__events, "login")
        error_list = self.filter_data(self.__events, "error")
        logout_list = self.filter_data(self.__events, "logout")
        event_dict: Dict[str, List[int]] = {}
        if len(login_list) > 0:
            event_dict["login"] = login_list
        if len(error_list) > 0:
            event_dict["error"] = error_list
        if len(logout_list) > 0:
            event_dict["logout"] = logout_list
        return event_dict


class StreamProcessor():
    def __init__(self, id1: str, id2: str, id3: str) -> None:
        self.sensor = SensorStream(id1)
        self.trans = TransactionStream(id2)
        self.event = EventStream(id3)

    def count_activities(self, data_dict: Dict[str, Union[str, int, float]]) -> int:
        total_activities = 0
        for data, data_list in data_dict.items():
            if data in ["login", "error", "logout"]:
                total_activities = len(data_list)
            else:
                total_activities += sum(data_list)
        return total_activities
    
    @staticmethod
    def convert_values_to_float(data_dict: Dict[str, Union[str, int, float]]) -> Dict[str, float]:
        for value_list in data_dict.values():
            for value in value_list:
                value = float(value)
        return data_dict
    
    def analyze_sensor_data(self, data_batch: List[str]) -> str:
        readings = self.sensor.count_readings(data_batch)
        analysis = "Sensor analysis: "
        try:
            self.sensor.process_batch(data_batch)
            data_dict = self.sensor.get_stats()
            data_dict = self.convert_values_to_float(data_dict)
            if data_dict == {}:
                analysis += "Invalid Batch Data"
            else:
                avg_temp_readings = self.sensor.average_temp_readings()
                analysis += f"{readings} readings"
                if len(data_dict) == 1:
                    analysis = analysis[:-1]
                analysis += " processed, "
                analysis += f"avg temp: {avg_temp_readings}°C"
        except Exception:
            analysis += "Invalid Batch Data"
        return analysis

    @staticmethod
    def convert_values_to_int(data_dict: Dict[str, Union[str, int, float]]) -> Dict[str, int]:
        for value_list in data_dict.values():
            for value in value_list:
                value = int(value)
        return data_dict

    def analyze_transaction_data(self, data_batch: List[str]) -> str:
        operations = self.trans.count_operations(data_batch)
        analysis = "Transaction analysis: "
        try:
            self.trans.process_batch(data_batch)
            data_dict = self.trans.get_stats()
            data_dict = self.convert_values_to_int(data_dict)
            if data_dict == {}:
                analysis += "Invalid Batch Data"
            else:
                net_flow = self.trans.calc_net_flow()
                analysis += f"{operations} operations"
                if len(data_dict) == 1:
                    analysis = analysis[:-1]
                analysis += f", net flow: {net_flow} units"
        except Exception:
            analysis += "Invalid Batch Data"
        return analysis
    
    def analyze_event_data(self, data_batch: List[str]) -> str:
        events = self.event.count_events(data_batch)
        analysis = "Event analysis: "
        try:
            self.event.process_batch(data_batch)
            data_dict = self.event.get_stats()
            if data_dict == {}:
                analysis += "Invalid Batch Data"
            else:
                num_errors = self.event.count_error_events()
                analysis += f"{events} events"
                if len(data_dict) == 1:
                    analysis = analysis[:-1]
                analysis += f", {num_errors} errors"
                if num_errors == 1:
                    analysis = analysis[:-1]
                analysis += " detected"
        except Exception:
            analysis += "Invalid Batch Data"
        return analysis

    def is_multi_sensor(self, multi_batch: Dict[str, List[str]]) -> bool:
        if len(multi_batch) > 1:
            return True
        return False

    def analyze_multi_data(self, multi_batch: Dict[str, List[str]]) -> str:
        if "Environmental Data" in multi_batch.keys():
            data = multi_batch["Environmental Data"]
            readings = self.sensor.count_readings(data)
            self.sensor.process_batch(data)
            high_temp_alerts = self.sensor.get_high_temp_alerts()        
        else:
            readings = 0
        if "Financial Data" in multi_batch.keys():
                operations = self.trans.count_operations(multi_batch["Financial Data"])
        else:
            operations = 0
        if "System Events" in multi_batch.keys():
                events = self.event.count_events(multi_batch["System Events"])
        else:
            events = 0
        analysis = "Batch results: \n"
        analysis += f"- Sensor data: {readings} readings"
        if readings == 1:
                    analysis = analysis[:-1]
        analysis += " processed\n"
        analysis += f"- Transaction data: {operations} operations"
        if operations == 1:
                    analysis = analysis[:-1]
        analysis += " processed\n"
        analysis += f"- Event data: {events} events"
        if events == 1:
                    analysis = analysis[:-1]
        analysis += " processed\n"
        analysis += "\nStream filtering active: High-priority data only\n"
        analysis += "Filtered results: "
        if high_temp_alerts:
            analysis += f"{len(high_temp_alerts)} critical sensor alerts"
        else:
            analysis += "No alerts."
        return analysis

    def analyze_stream_stats(self, multi_batch: Dict[str, List[str]]) -> None:
        if not multi_batch or any(value is None for value in multi_batch.values()):
            print("Invalid Batch")
            return
        
        if not self.is_multi_sensor(multi_batch):
            env = ["Environmental Data", "Sensor"]
            if env[0] in multi_batch.keys():
                print(f"Initializing {env[1]} Stream...")
                id = self.sensor.sensor_id
                print(f"Stream ID: {id}, Type: {env[0]}")
                print(f"Processing sensor batch: {multi_batch[env[0]]}")
                print(self.analyze_sensor_data(multi_batch[env[0]]))

            fin = ["Financial Data", "Transaction"]
            if fin[0] in multi_batch.keys():
                print(f"Initializing {fin[1]} Stream...")
                id = self.trans.sensor_id
                print(f"Stream ID: {id}, Type: {fin[0]}")
                print(f"Processing transaction batch: {multi_batch[fin[0]]}")
                print(self.analyze_transaction_data(multi_batch[fin[0]]))

            eve = ["System Events", "Event"]
            if eve[0] in multi_batch.keys():
                print(f"Initializing {eve[1]} Stream...")
                id = self.event.sensor_id
                print(f"Stream ID: {id}, Type: {eve[0]}")
                print(f"Processing event batch: {multi_batch[eve[0]]}")
                print(self.analyze_event_data(multi_batch[eve[0]]))

        else:
            print("=== Polymorphic Stream Processing ===")
            print("Processing mixed stream types through unified interface...\n")
            print(self.analyze_multi_data(multi_batch))


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    stream_processor = StreamProcessor("SENSOR_001", "TRANS_001", "EVENT_001")
    multidata_batch0 = {
        "Environmental Data": ["temp:22.5", "humidity:65", "pressure:1013", "temp: 27.5", "temp: 31"]
    }
    multidata_batch1 = {
        "Financial Data": ["buy:100", "sell:150", "buy:75", "sell:100", "buy:25"]
    }
    multidata_batch2 = {
        "System Events":  ["login", "error", "logout", "login", "error"]
    }
    multidata_batch3 = {
        "Environmental Data": ["humidity:65", "pressure:1013", "temp: 27.5", "temp: 73.5"],
        "Financial Data": ["buy:100", "sell:150", "buy:75", "sell:100", "buy:525"],
        "System Events":  ["login", "error", "logout", "login", "error"]
    }
    stream_processor.analyze_stream_stats(multidata_batch0)
    print()
    stream_processor.analyze_stream_stats(multidata_batch1)
    print()
    stream_processor.analyze_stream_stats(multidata_batch2)
    print()
    stream_processor.analyze_stream_stats(multidata_batch3)

    print("\nAll streams processed successfully. Nexus throughput optimal.")

if __name__ == "__main__":
    main()
