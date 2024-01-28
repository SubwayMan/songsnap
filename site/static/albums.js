var playlists = [{name: "Classical", img: "https://media.istockphoto.com/id/1431567498/vector/vector-illustration-of-musical-notes-on-white-background.jpg?s=612x612&w=0&k=20&c=E4Qx8E7OJm-itMPylpaZhNIU8mkJQt5XctWlKLLa1I8=", id: "Hello"},
                {name: "Calming Music", img: 'https://w0.peakpx.com/wallpaper/115/408/HD-wallpaper-iceberg-minimalist.jpg', id: "NewPlaylist"},
                {name: "Pac-man", img: 'https://static.wixstatic.com/media/a4f877_011744a8632946aeae314e1792963fb0~mv2.jpg/v1/fill/w_816,h_800,al_c,q_85/a4f877_011744a8632946aeae314e1792963fb0~mv2.jpg', id: "NewPlaylist"},
                {name: "Donkey Kong", img: 'https://upload.wikimedia.org/wikipedia/en/thumb/f/fd/Donkey_Kong_Gameplay.png/220px-Donkey_Kong_Gameplay.png', id: "DK"}];

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

function printStuff() {
    for (var i = 0; i < playlists.length; i++) {
        var playlist = document.createElement("div");
        var plImg = document.createElement("img");
        var plName = document.createElement("h3")
    
        playlist.className = "playlist";
    
        plImg.src = playlists[i]["img"];
        plImg.alt = playlists[i]["name"];
        plImg.style.width = "17rem";
        plImg.style.height = "17rem";
    
        plName.innerHTML = playlists[i]["name"];
    
        playlist.appendChild(plImg);
        playlist.appendChild(plName);
        
        document.getElementById("playlists").appendChild(playlist);
    }
}

// for (var i = 0; i < playlists.length; i++) {
//     var playlist = document.createElement("div");
//     var plImg = document.createElement("img");
//     var plName = document.createElement("h3")

//     playlist.className = "playlist";

//     plImg.src = playlists[i]["img"];
//     plImg.alt = playlists[i]["name"];
//     plImg.width = "250rem"
//     plImg.length = "250rem"

//     plName.innerHTML = playlists[i]["name"];

//     playlist.appendChild(plImg);
//     playlist.appendChild(plName);

//     document.getElementById("playlists").appendChild(playlist);
// }
