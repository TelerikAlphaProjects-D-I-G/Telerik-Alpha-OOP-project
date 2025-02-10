

class PackageStatus:


    package_status = ["Pending", "In Transit", "Delivered"]

    def next(self,status):
        index = self.package_status.index(status)
        if index < len(self.package_status) -1:
            return self.package_status[index +1]
        return status

    def previous(self,status):
        index = self.package_status.index(status)
        if index > 0:
            return self.package_status[index -1]
        return status

package_status = PackageStatus()
current_status = "In Transit"

print(package_status.previous(current_status))
