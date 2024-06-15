class VersionManager:
    def __init__(self, version='0.0.1'):
        self.initial_version = version
        self.major = 0
        self.minor = 0
        self.patch = 1

    def validate(self):
        try:
            version = self.initial_version.split('.')
            print(version)
            print(f'{self.initial_version=}')
            print(version[:3])

            version_list = [int(_) for _ in version[:3]]
            print(version_list)
        except ValueError:
            return "Error occured while parsing version!"
        except TypeError:
            return "Default initial version"



    def major(self):
        pass

    def minor(self):
        pass

    def patch(self):
        pass

    def rollback(self):
        pass

    def release(self):
        return f"{self.major}.{self.minor}.{self.patch}"
        if release_version == '0.0.1':
            return "Default initial version"
        return self.initial_version

print(VersionManager("1.2.3").release(), VersionManager("1.2.3").validate())
print(VersionManager("1.2.3.4").release(), VersionManager("1.2.3.4").validate())
print(VersionManager("1.2.3.d").release(), VersionManager("1.2.3.d").validate())
print(VersionManager("1").release(), VersionManager("1").validate())
# print(VersionManager("1.1").release(), VersionManager("1.1").validate())
print(VersionManager().release(), VersionManager().validate())
# print(VersionManager("").release(), VersionManager("").validate())



# print(VersionManager("1.2.3").release(), "1.2.3", "No version changes")
# print(VersionManager("1.2.3.4").release(), "1.2.3", "No version changes")
# print(VersionManager("1.2.3.d").release(), "1.2.3", "No version changes")
# print(VersionManager("1").release(), "1.0.0", "Default minor version is 0")
# print(VersionManager("1.1").release(), "1.1.0", "Default patch is 0")
# print(VersionManager().release(), "0.0.1", "Default initial version")
# print(VersionManager("").release(), "0.0.1", "Default initial version")