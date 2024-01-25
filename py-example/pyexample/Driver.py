class Driver:
    """
    Driver for specific sensor

    Attributes
    ----------
    name : str
        Name of the sensor

    Methods
    -------
    write(buffer):
        Send data to the sensor.
    """

    def __init__(self, name:str):
        """
        Constructs all the necessary attributes for the driver object.

        Parameters
        ----------
            name : str
                Name of the sensor
        """

        self.name = name

    def write(self, buffer:str) -> int:
        """
        Send data buffer to the sensor.

        Parameters
        ----------
        buffer : str
            Data buffer to be send

        Returns
        -------
        status_code : int
            status code of the operation SUCCES, FAILURE
        """

        # Do something
        return 0