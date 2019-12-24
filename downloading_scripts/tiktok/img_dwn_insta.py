import wget #додаємо бібліотеку для скачування

def dwn_img_insta(link, filename):
    
    link += "media/?size=l" #добавляє в кінець рядка текст для перенаправлення на саму картинку
    wget.download(link, filename) #скачує файл і присвоює йому імя


