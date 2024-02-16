import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent
SCHEDULE_DIR = BASE_DIR / "SolarSchedule"
EDITOR_DIR = BASE_DIR / "solar_schedule"
TEMP_DIR = EDITOR_DIR / "templates"
STAT_DIR = EDITOR_DIR / "static"
DATA_DIR = STAT_DIR / "data"

if __name__ == '__main__':
    print(BASE_DIR)


