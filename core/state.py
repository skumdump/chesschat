class AppState:
    '''Singleton-like state manager for global app state.'''
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Initialize state variables here
        return cls._instance