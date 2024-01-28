var playlists = [{name: "Hello", img: "https://media.istockphoto.com/id/1431567498/vector/vector-illustration-of-musical-notes-on-white-background.jpg?s=612x612&w=0&k=20&c=E4Qx8E7OJm-itMPylpaZhNIU8mkJQt5XctWlKLLa1I8=", id: "Hello"},
                {name: "New Playlist", img: 'https://s3-alpha-sig.figma.com/img/7064/f6f8/39d00f85d1e1d4d73376dfb1da93af17?Expires=1707091200&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=YpgwpCdX9~izElBIiDYuxxeRFtWbX4EVdDjDFQ2GyCjYjS5FMs4vrpNJDbYGgCM4Lwh5jK-7OFIC5c5dxVW-Zrd3DYL7O7vNjvwW~7d~x~NmbvFy6M6PGRBnpPG~f5N7zogKXjZZcp9TCiflhQIhM~SVz99zpfHhscJ~RlzURXBuTy9bi6MKYHf48tC7OYBhxF~0ljPmr0AWhjj5gSzIgmUalyuMSxfQsDbkJGPiaOyu4Oj45f9TlBXMDK6nwSYQLn5nmckuE0nQg1OxythzhXPgm68-xPKBN9qgyRXWoFzF78po1y1U6eASW22LCIkC-1A3bek2-~gDl9oQQQ~7Vg__', id: "NewPlaylist"},
                {name: "New Playlist", img: 'https://s3-alpha-sig.figma.com/img/7064/f6f8/39d00f85d1e1d4d73376dfb1da93af17?Expires=1707091200&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=YpgwpCdX9~izElBIiDYuxxeRFtWbX4EVdDjDFQ2GyCjYjS5FMs4vrpNJDbYGgCM4Lwh5jK-7OFIC5c5dxVW-Zrd3DYL7O7vNjvwW~7d~x~NmbvFy6M6PGRBnpPG~f5N7zogKXjZZcp9TCiflhQIhM~SVz99zpfHhscJ~RlzURXBuTy9bi6MKYHf48tC7OYBhxF~0ljPmr0AWhjj5gSzIgmUalyuMSxfQsDbkJGPiaOyu4Oj45f9TlBXMDK6nwSYQLn5nmckuE0nQg1OxythzhXPgm68-xPKBN9qgyRXWoFzF78po1y1U6eASW22LCIkC-1A3bek2-~gDl9oQQQ~7Vg__', id: "NewPlaylist"}];

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
