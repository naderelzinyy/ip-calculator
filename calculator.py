class AddressConverter:
    """Responsible for converting IP and Subnet Mask addresses to another values.
    """

    def __init__(self, address: str):
        """

        address: The address to be converted.
        """
        self.address = address

    @staticmethod
    def __octets_to_binary(octets: list) -> list:
        """Converts octets to binary.

        param octets: List of octets
        :return: A list of binary octets.
        """
        return ["{0:b}".format(int(octet)) for octet in octets]

    def to_binary(self) -> str:
        """Contains all the processes of converting an address to binary."""
        octets = self.address.split(".")
        return ".".join(self.__octets_to_binary(octets))


if __name__ == '__main__':
    ip = "64.224.115.45"
    AddressConverter(address=ip).to_binary()
