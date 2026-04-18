import importlib
from importlib.metadata import version


def check_import() -> bool:
    modules: dict[str, str] = {"pandas": "Data manipulation",
                               "numpy": "Numerical computation",
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
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        print("\nAnalyzing Matrix data...")

        np.random.seed(42)

        n = 100
        body_weigth = np.random.normal(loc=75, scale=10, size=n)
        prob_diabetes = 1 / (1 + np.exp(-(body_weigth - 80) / 5))
        diabetes = np.random.binomial(1, prob_diabetes)
        df = pd.DataFrame({
            'body_weigth': body_weigth,
            'diabetes': diabetes
        })

        print(f"Processing {n} data points...")
        print("Generating visualization...\n")

        plt.figure()
        plt.scatter(df['body_weigth'], df['diabetes'])
        coef = np.polyfit(df['body_weigth'], df['diabetes'], 1)
        poly1d_fn = np.poly1d(coef)
        plt.plot(df['body_weigth'], poly1d_fn(df['body_weigth']))

        plt.xlabel('Body Weigth (kg)')
        plt.ylabel('Diabetes (0 = no, 1 = yes)')
        plt.title('Relation between Body Weigth and Diabetes')

        plt.savefig("matrix_analysis.png")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")


if (__name__ == "__main__"):
    main()
