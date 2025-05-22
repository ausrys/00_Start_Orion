import datetime


class SingletonBase:
    '''Base singleton class that other singleton classes will implement'''
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"[SingletonBase] Creating new instance of {cls.__name__}")
            cls._instances[cls] = super().__new__(cls)
        else:
            print(f"[SingletonBase] Using existing instance of {cls.__name__}")
        return cls._instances[cls]

# Example


class Logger(SingletonBase):
    def __init__(self, log_file="app.log"):
        # Prevent reinitialization
        if not hasattr(self, 'initialized'):
            self.log_file = log_file
            self.initialized = True
            with open(self.log_file, 'a') as f:
                f.write(
                    f"--- Logger started at {datetime.datetime.now()} ---\n")

    def log(self, message: str):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")
        print(f"[Logger] {message}")


logger1 = Logger()
logger2 = Logger()

logger1.log("First message from logger1")
logger2.log("Second message from logger2")

print("Logger1 is Logger2?", logger1 is logger2)  # True
