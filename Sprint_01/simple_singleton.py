class Singleton:
    """The simple singleton class pattern"""
    instance = None

    def __new__(cls):
        """the singleton pattern is using this new method with 
        the super for create and check the new singleton object
        """
        if Singleton.instance is None:
            Singleton.instance = super().__new__(cls)
        return Singleton.instance

    def job_singleton_example(self):
        """this method just an example and in real life 
        could be removed
        """
        print("do some action just at call")
        self.sample_data = 10


if __name__ == '__main__':
    first = Singleton()
    first.job_singleton_example()
    print(first)
    second = Singleton()
    print(second)
    print(first is second)
    print(first.sample_data)
    first.sample_data = 90
    print(second.sample_data)
  
