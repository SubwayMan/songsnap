from taipy import Gui


login_md = "# Login"
uploading_md = "# Upload"
single_album_md = "# Album"
albums_md = "# My Albums"

pages = {
    "login": login_md,
    "upload": uploading_md,
    "album": single_album_md,
    "albums": albums_md
}

Gui(pages=pages).run()

    
