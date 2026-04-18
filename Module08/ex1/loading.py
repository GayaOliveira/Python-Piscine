import importlib
from importlib.metadata import version


def check_import() -> bool:
    modules: dict[str, str] = {"pandas": "Data manipulation",
                               "numpy": "Numerical computation",
                               "requests": "Network access",
                               "matplotlib": "Visualization"}
    try:
        for m in modules:
            importlib.import_module(m)
            print(f"[OK] {m} ({version(m)}) - {modules[m]} ready")
    except ModuleNotFoundError as e:
        mod_name: str = e.msg[17: len(e.msg) - 1]
        print(e)
        print(f'Import {mod_name} with "pip install {mod_name}"')
        return (False)
    return (True)


def main() -> None:
    if (check_import()):
        import requests
        import pandas as pd
        import matplotlib.pyplot as plt
        print("\nAnalyzing Matrix data...")
        url: str = "https://pokeapi.co/api/v2/pokemon/"
        response: requests.Response = requests.get(url)
        if (response.status_code == 200):
            data = response.json()
            print(data.keys())
            print("Processing 1000 data points")
            proc = pd.DataFrame(data['results'])
            plt.figure(figsize=(12, 5))
            plt.hist(proc['name'], range(3, 16), 'mediumseagreen', 'black')
            print("Generating visualization...")
            plt.savefig('teste.png')
            print("\nAnalysis complete!")
            print("Results saved to: teste.png")
        else:
            print(f"Error {response.status_code}")


if (__name__ == "__main__"):
    main()
