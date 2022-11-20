import os
from urllib.request import urlopen, Request


def mangalib_download(user_url, pages_count=1):
    # Заголовки, которые мы будем передавать сайту с мангой, чтобы он считал нас браузером.
    # Headers that we are transferring to the web-site to make it consider the script
    # as a web-browser.
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/41.0.2228.0 Safari/537.3'}

    # Драконим ссылку на кусочки, разделённые слешем, убирая последнюю часть с именем файла.
    # Splitting the URL into pieces and removing the last part of it which contains file extension.
    # ['https:', '', 'img33.imgslib.link', '', 'manga', 'genshin-impact', 'chapters', '1-0']
    splitted_url = [elem for elem in user_url.split('/') if not elem.endswith('.jpg')]

    # Вытаскиваем название манги, которое будет использоваться для именования локальной папки.
    # Getting the manga title to use it as a local folder's name.
    manga_name = ' '.join(splitted_url[5].split('-')).title()  # Genshin Impact

    # Формируем базовую часть URL, которая будет неизменной для всех файлов.
    # Generating the base part of an URL that is the same for all files.
    # https://img33.imgslib.link//manga/genshin-impact/chapters/1-0
    basic_url_part = '/'.join(splitted_url)

    # Описываем формирование удалённого имени файла типа 73.jpg_res.jpg.
    # Здесь же динамически формируем имя локального файла.
    # Setting remote and local files names.
    for i_num in range(pages_count + 1):
        if i_num < 10:
            image_name = '0' + str(i_num) + '.jpg_res.jpg'
            local_image_name = splitted_url[5] + '-0' + str(i_num) + '.jpg'
        else:
            image_name = str(i_num) + '.jpg_res.jpg'
            local_image_name = splitted_url[5] + '-' + str(i_num) + '.jpg'

        # Формируем полный URL.
        # Creating the full URL for download.
        full_url = '/'.join([basic_url_part, image_name])

        # Формируем название локальной папки и создаём её, если она ещё не создана.
        # Setting a local folder name and creating it if it is not exist yet.
        local_dir = os.path.abspath(os.path.join(os.path.sep,
                                                 'Users', 'sinka', 'YandexDisk',
                                                 manga_name))
        if not os.path.isdir(local_dir):
            print(f'\n{local_dir} is not created. Creating...')
            os.mkdir(local_dir)

        # Скачиваем и сохраняем.
        # Downloading the picture file.
        print(f'Processing {full_url}...')
        local_file_path = os.path.join(local_dir, local_image_name)
        local_file = open(local_file_path, 'wb')
        req = Request(url=full_url, headers=headers)
        with urlopen(req) as response:
            local_file.write(response.read())
        print('Done.')
        local_file.close()


url = 'https://img33.imgslib.link//manga/genshin-impact/chapters/1-0/73.jpg_res.jpg'
mangalib_download(url, 73)
