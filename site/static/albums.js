var playlists = [{name: "Arcade Night", img: "/static/arcade.jpg", sid: "5QVevz6hYtUvaYlUZ2toyu", id: "Hello"},
                {name: "A slow dance", img: '/static/dance.jpg', sid: "1DOt1RZ2E4vM8UQodQxmIk", id: "NewPlaylist"},
                {name: "Dark City Night", img: '/static/darkcitynight.jpg', sid: "0gFQBRD9mjMWtxYsiu2wlN", id: "NewPlaylist"},
                {name: "80s vibes", img: '/static/dudes.jpg', sid: "2lWobUd7t2lRSPI0oTi95D", id: "DK"},
                {name: "Jazz afternoon", img: '/static/jazzyday.jpg', sid: "2vmNPx4fkgz1WuOD24mV4U", id: "Dhd"}];

function getData(url) {
  return fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  });
}
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
        var anchor = document.createElement("a");
        var nhref = "/album?playlist="+playlists[i]["sid"]
        anchor.setAttribute("href", nhref)
        var plImg = document.createElement("img");
        var plName = document.createElement("h3")
    
        playlist.className = "playlist";
    
        plImg.src = playlists[i]["img"];
        plImg.alt = playlists[i]["name"];
        plImg.style.width = "17rem";
        plImg.style.height = "17rem";
    
        plName.innerHTML = playlists[i]["name"];
    
        anchor.appendChild(plImg);
        playlist.appendChild(anchor);
        playlist.appendChild(plName);
        
        document.getElementById("playlists").appendChild(playlist);
    }
}

function encode(val) {
  return encodeURIComponent(val).replace("/", "%2F")
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
