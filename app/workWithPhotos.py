import os
import shutil

class workPhotos:
    def __init__(self, pachTempImage, pachDirWork):
        self.pachTempImage = pachTempImage
        self.pachDirWork = pachDirWork

    def creatDir(self, USER_ID):
        '''
        Создать список папок:
            ID_2
                DEM
                Ortopfoto
                photo
                DHM
                report
        :param USER_ID:
        :return:
        '''
        listDir = set()
        listDir = {'DEM', 'Ortopfoto', 'photo', 'DHM', 'report'}

        for nameDir in listDir:
            directory = self.pachDirWork+'\/'+USER_ID + '\/' + nameDir
            if not os.path.exists(directory):
                os.makedirs(directory)

    def movePhoto(self, USER_ID):

        files = os.listdir(self.pachTempImage)
        for f in files:
            shutil.move(self.pachTempImage +'\/'+ f, self.pachDirWork+'\/'+ USER_ID + '\/' + 'photo')

if __name__ == "__main__":
    pachTempImage = r'D:\dimaProject\photoscan\app\static\images'
    pachDirWork = r'D:\dimaProject\photoscan\processing_photoscan'

    test = workPhotos(pachTempImage,pachDirWork)
    #test.creatDir('ID_2')
    #test.movePhoto('ID_2')
