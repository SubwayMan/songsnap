from taipy import Gui
from pages.login_md import *
from pages.uploading_md import *
from pages.albums_md import *
from pages.single_album_md import *


pages = {
    "login": login_md,
    "upload": uploading_md,
    "album": single_album_md,
    "albums": albums_md
}

Gui(pages=pages).run()

    
