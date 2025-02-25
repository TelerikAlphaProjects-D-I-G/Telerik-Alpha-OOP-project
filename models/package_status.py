class PackageStatus:

    PENDING = 'Pending'
    IN_TRANSIT = 'In Transit'
    DELIVERED = 'Delivered'


    package_status = [PENDING, IN_TRANSIT, DELIVERED]

    @staticmethod
    def next(status):
        index = PackageStatus.package_status.index(status)
        if index < len(PackageStatus.package_status) - 1:
            return PackageStatus.package_status[index + 1]
        return status

    @staticmethod
    def previous(status):
        index = PackageStatus.package_status.index(status)
        if index > 0:
            return PackageStatus.package_status[index - 1]
        return status

