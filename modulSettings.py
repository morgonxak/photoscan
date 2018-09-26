import json

class Settings:
    def __init__(self, pathFileSettings):
        self.pathFileSettings = pathFileSettings
        self.importSettrings()

    def getSettings(self):
        return self.jsonSettings

    def importSettrings(self):
        file = open(self.pathFileSettings, 'r')
        self.jsonSettings = json.loads(file.read())
        file.close()
        return self.jsonSettings

    def saveSettings(self):

        with open(self.pathFileSettings, 'w') as outfile:
            json.dump(self.jsonSettings, outfile)

    def change(self, parameter, value):
        self.jsonSettings[parameter] = value
        self.saveSettings()

