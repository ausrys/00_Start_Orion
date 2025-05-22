class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"[SingletonMeta] Creating new instance of {cls.__name__}")
            cls._instances[cls] = super().__call__(*args, **kwargs)
        else:
            print(f"[SingletonMeta] Using existing instance of {cls.__name__}")
        return cls._instances[cls]


class AppConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.settings = {}

    def set(self, key, value):
        self.settings[key] = value
        print(f"[AppConfig] Set {key} = {value}")

    def get(self, key, default=None):
        return self.settings.get(key, default)


def main():
    config1 = AppConfig()
    config2 = AppConfig()

    config1.set("theme", "dark")
    print(config2.get("theme"))  # Should print "dark"

    print("Config1 is Config2?", config1 is config2)  # True


if __name__ == "__main__":
    main()
