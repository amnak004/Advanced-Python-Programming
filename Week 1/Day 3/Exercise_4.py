import sys
import os
import venv


def main():
    if len(sys.argv) != 2:
        print("Usage: python project_bootstrapper.py <env_path>")
        return

    env_path = sys.argv[1]
    venv.create(env_path, with_pip=True)

    if sys.platform.startswith("win"):
        interpreter_path = os.path.join(env_path, "Scripts", "python.exe")
    else:
        interpreter_path = os.path.join(env_path, "bin", "python")

    if os.path.exists(interpreter_path):
        print(f"Success: virtual environment created at {env_path}")
    else:
        print(f"Failure: interpreter not found at {interpreter_path}")
        return

    if sys.platform.startswith("win"):
        activate_cmd = f"{env_path}\\Scripts\\activate"
    else:
        activate_cmd = f"source {env_path}/bin/activate"

    print(f"Next step: activate the environment with: {activate_cmd}")


if __name__ == "__main__":
    main()
