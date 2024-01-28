var playlists = [{name: "Hello", img: "https://media.istockphoto.com/id/1431567498/vector/vector-illustration-of-musical-notes-on-white-background.jpg?s=612x612&w=0&k=20&c=E4Qx8E7OJm-itMPylpaZhNIU8mkJQt5XctWlKLLa1I8=", id: "Hello"}];

function Playlist(name, img, id) {
    this.name = name;
    this.img = img;
    this.id = id;
}

function addToPlaylist(pl) {
    console.log("Hellooooo");
    const temp = new Playlist(pl.name, pl.img, pl.id);
    playlists.push(temp);
}
