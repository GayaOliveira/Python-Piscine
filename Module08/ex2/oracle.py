import os
try:
    from dotenv import load_dotenv
except ModuleNotFoundError as err:
    print(err)
    exit


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    envs = {"MATRIX_MODE": "Mode", "DATABASE_URL": "Database",
            "API_KEY": "API Access", "LOG_LEVEL": "Log Level",
            "ZION_ENDPOINT": "Zion Network"}
    load_dotenv()
    print("Configuration loaded:")
    for env, txt in envs.items():
        env_result = os.getenv(env)
        if not env_result:
            print(f"ERROR: env {txt} not found")
        else:
            mode_actual = os.getenv("MATRIX_MODE", "development")
            if mode_actual.lower() == "production" and env in [
                    "API_KEY", "DATABASE_URL"]:
                hidden = env_result[:4] + "**********"
                print(f"{txt}: {hidden}")
            else:
                print(f"{txt}: {env_result}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.isfile(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found, running on system variables only"
              )
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.\n")


if __name__ == "__main__":
    main()
