from ZerodhaConsoleEmulator import ZerodhaConsoleEmulator
from utils import readProperties


def main():
    props = readProperties()
    emulator = ZerodhaConsoleEmulator(
        props.get("clientId"), props.get("password"), props.get("pin"), props.get('report'))
    emulator.run()


if __name__ == "__main__":
    main()
