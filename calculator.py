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

    @staticmethod
    def add_zeros(address) -> list:
        """Adds zeros if an octet contains less than 8 bits.

        :return: a list with the whole 8 bits.
        """
        new_address = []
        for octet in address:
            if zeros_to_be_added := (8 - len(octet)):
                for _ in range(zeros_to_be_added):
                    octet = f"0{octet}"
            new_address.append(octet)
        print(f"{address = } -- {new_address = }")
        return new_address

    def to_binary(self) -> list:
        """Contains all the processes of converting an address to binary.
        :return: ip address in binary format.
        """
        octets = self.address.split(".")
        return AddressConverter.add_zeros(self.__octets_to_binary(octets))


class IDExtractor:
    def __init__(self, ip_address, subnet):
        self.bin_ip = AddressConverter(address=ip_address).to_binary()
        self.bin_subnet = AddressConverter(address=subnet).to_binary()

    def get_network_id(self) -> List[str]:
        """Extracts the network id from ip and subnet mask addresses.
        """
        network_id = []
        for oct1, oct2 in zip(self.bin_ip, self.bin_subnet):
            print(f"{oct1 = } -- {oct2 = }")
            octet = ''

            for bit1, bit2 in zip(oct1, oct2):
                octet += str(int(bit1) & int(bit2))
                print(f"{bit1 = } -- {bit2 = } {int(bit1) & int(bit2) =}")
            network_id.append(octet)
        return network_id


if __name__ == '__main__':
    ip = "64.224.115.45"
    AddressConverter(address=ip).to_binary()
