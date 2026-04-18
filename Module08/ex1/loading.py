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
        massa_corporal = np.random.normal(loc=75, scale=10, size=n)
        prob_diabetes = 1 / (1 + np.exp(-(massa_corporal - 80) / 5))
        diabetes = np.random.binomial(1, prob_diabetes)
        df = pd.DataFrame({
            'massa_corporal': massa_corporal,
            'diabetes': diabetes
        })

        print(f"Processing {n} data points...")
        print("Generating visualization...\n")

        plt.figure()
        plt.scatter(df['massa_corporal'], df['diabetes'])
        coef = np.polyfit(df['massa_corporal'], df['diabetes'], 1)
        poly1d_fn = np.poly1d(coef)
        plt.plot(df['massa_corporal'], poly1d_fn(df['massa_corporal']))

        plt.xlabel('Massa Corporal (kg)')
        plt.ylabel('Diabetes (0 = não, 1 = sim)')
        plt.title('Relação entre Massa Corporal e Diabetes')

        plt.savefig("matrix_analysis.png")

        print("Analysis complete!")
        print("Results saved to: matrix_analysis.png")


if (__name__ == "__main__"):
    main()
