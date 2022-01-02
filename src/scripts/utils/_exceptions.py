class ModelNotFittedError(Exception):
    """
    It is raised when a method or attribute is requested that requires the model 
    to be trained (such as .predict() or .score())
    """
    pass
