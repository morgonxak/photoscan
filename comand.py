import PhotoScan
import socket
from threading import Thread

def openPachDir():
    '''
    открывает окно для указания вапки возвращает путь
    :return:
    '''
    return PhotoScan.app.getExistingDirectory("Dosier images avec Exif:")

def AddPhoto(chunk, patchDirImage):
    '''
    patchDirImage: Путь до папки с изображениями
    :param chunk
    :param patchDirImage r"F:\18.08.02 Шерегеш\Фото\1 флешка"
    :return:
    '''
    import os
    path_photos = patchDirImage
    image_list = os.listdir(path_photos)
    photo_list = list()
    for photo in image_list:
        if photo.rsplit(".", 1)[1].lower() in ["jpg", "jpeg", "tif", "tiff"]:
            photo_list.append("/".join([path_photos, photo]))
    chunk.addPhotos(photo_list)

def creatProject(project_path, project_name):
    '''
    Создаем новый проект либо открывваем существующий
    :param project_path: Путь до папки с проектом
    :param project_name: Имя проекта
    :return: Chunk
    '''
    doc = PhotoScan.app.document
    doc.save(project_path + project_name + ".psx")
    if len(doc.chunks):
        chunk = PhotoScan.app.document.chunk
    else:
        chunk = doc.addChunk()

    return chunk, doc

def alingPhotos(accuracy=PhotoScan.HighAccuracy, generic_preselection=True, reference_preselection=True,
                  filter_mask=False, keypoint_limit=350000, tiepoint_limit=0):
    '''
    выровнить фотографии
    :param accuracy:
    :param generic_preselection:
    :param reference_preselection:
    :param filter_mask:
    :param keypoint_limit:
    :param tiepoint_limit:
    :return:
    '''
    chunk.matchPhotos(accuracy, generic_preselection, reference_preselection,filter_mask, keypoint_limit, tiepoint_limit)
    chunk.alignCameras()
    doc.save()

def setCoordinateSystem(CK = "EPSG::4326"):
    '''
    Установить систему координат
    :return:
    '''
    chunk.crs = PhotoScan.CoordinateSystem(CK)
    chunk.updateTransform()
    doc.save()

def buildDenseCloud(quality=PhotoScan.UltraQuality, filter=PhotoScan.AggressiveFiltering):
    '''
    строить плотное облако
    :param quality:
    :param filter:
    :return:
    '''
    chunk.buildDenseCloud(quality=PhotoScan.UltraQuality, filter=PhotoScan.AggressiveFiltering)
    doc.save()

def exportPoints(project_path, project_name,binary=True, precision=6, colors=True,
                   format=PhotoScan.PointsFormatLAS):
    '''
    Экспорт облако точек
    :param project_path: Путь до папки для экспорта
    :param project_name: Имя файла
    :param binary:
    :param precision:
    :param colors:
    :param format:
    :return:
    '''
    chunk.exportPoints(project_path + project_name + ".las", binary=True, precision=6, colors=True,
                   format=PhotoScan.PointsFormatLAS)

def buildModel(surface=PhotoScan.HeightField, interpolation=PhotoScan.EnabledInterpolation,
                 face_count=PhotoScan.MediumFaceCount):
    '''
    Создать модель
    :param surface:
    :param interpolation:
    :param face_count:
    :return:
    '''
    chunk.buildModel(surface, interpolation, face_count)
    doc.save()

def buildDEM(source=PhotoScan.DenseCloudData, interpolation=PhotoScan.EnabledInterpolation):
    '''
    Построить карту высот
    :param source:
    :param interpolation:
    :return:
    '''
    chunk.buildDem(source, interpolation)
    doc.save()

def exportDem(project_path, project_name, image_format=PhotoScan.ImageFormatTIFF,
                format=PhotoScan.RasterFormatTiles, nodata=-32767, write_kml=False, write_world=True):
    '''
    Экспортировать карту высот
    :param project_path:
    :param project_name:
    :param image_format:
    :param format:
    :param nodata:
    :param write_kml:
    :param write_world:
    :return:
    '''
    chunk.exportDem(project_path + project_name + "_DEM.tif", image_format,
                format, nodata, write_kml, write_world)

def buildOrtho(surface=PhotoScan.ElevationData, blending=PhotoScan.MosaicBlending, color_correction=False):
    '''
    Построить ортофотоплан
    :param surface:
    :param blending:
    :param color_correction:
    :return:
    '''
    chunk.buildOrthomosaic(surface, blending, color_correction)
    doc.save()

def exportOrthomosaic(project_path, project_name, image_format=PhotoScan.ImageFormatTIFF,
                        format=PhotoScan.RasterFormatTiles, raster_transform=PhotoScan.RasterTransformNone,
                        write_kml=False, write_world=True):
    '''
    Экспорт ортофотоплана
    :param project_path: Папка
    :param project_name: Имя
    :param image_format:
    :param format:
    :param raster_transform:
    :param write_kml:
    :param write_world:
    :return:
    '''
    chunk.exportOrthomosaic(project_path + project_name + ".tif", image_format, format, raster_transform, write_kml,write_world )

def dispatch(self, value):
    method_name = str(value)
    method = getattr(self, method_name)
    return method()

class ConnectServer(Thread):
    def __init__(self, addr):
        self.addr = addr

    def run(self):
        self.startClient()

    def startClient(self):
        sock = socket.socket()
        sock.connect(self.addr)

        while True:
            #sock.settimeout(60)  # установка таймаута
            #sock.setblocking(0)
            data = sock.recv(1024)
            print("данные с сервера", data)
            #dispatch(data)
            if data == b'stop':
                break
            if data == b'creat':
                creatProject(r"D:\dimaProject\photoscan\processing_photoscan\ID_1", "test")
        sock.close()
        print("соеденения закрыто")


host = 'localhost'
port = 777
addr = (host, port)

ThreadSoket = ConnectServer(addr)
ThreadSoket.run()
