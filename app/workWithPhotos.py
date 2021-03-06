import os
import shutil

'''
класс для работы с файлами, создания рабочего котолога пользователя и перемещения туда фотографий
'''
class workPhotos:

    def __init__(self, pachTempImage, pachDirWork):
        '''
        Изициализация принимает каталог с начальными фото и кудда скинуть
        :param pachTempImage:
        :param pachDirWork:
        '''
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

        listDir = {'DEM', 'Ortopfoto', 'photo', 'DHM', 'report'}

        for nameDir in listDir:
            directory = self.pachDirWork+'\/'+USER_ID + '\/' + nameDir
            if not os.path.exists(directory):
                os.makedirs(directory)

    def movePhoto(self, USER_ID):

        files = os.listdir(self.pachTempImage)
        print("количество фотографий ", len(files))
        for f in files:
            shutil.move(self.pachTempImage +'\/'+ f, self.pachDirWork+'\/'+ USER_ID + '\/' + 'photo')

if __name__ == "__main__":
    pachTempImage = r'D:\dimaProject\photoscan\app\static\images'
    pachDirWork = r'D:\dimaProject\photoscan\processing_photoscan'

    test = workPhotos(pachTempImage,pachDirWork)
    #test.creatDir('ID_2')
    #test.movePhoto('ID_2')
