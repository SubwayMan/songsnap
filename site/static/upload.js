var num_songs = 10;
// Function to make a POST request
function postData(url, data) {
  return fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  });
}
function imgToURI(img) {
    return new Promise(resolve => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.readAsDataURL(img);
    });
}

async function handleImageUpload(event) {
    const file = event.target.files[0];
    const uploadButton = document.querySelector('.upload-button');
    uploadButton.style.display = 'none';

    const songs_label = document.querySelector('.songs-label');
    songs_label.style.display = 'none';

    const songs_range = document.querySelector('.songs-range');
    songs_range.style.display = 'none';

    const loader = document.querySelector('.loader');
    loader.style.display = 'block';

    const uploadBar = document.querySelector('.upload_bar');
    uploadBar.style.display = 'flex';

    num_songs = document.querySelector('.songs-range').value;

    imgToURI(file)
      .then((image_url) => {
        return postData("/songsnapapi/analyse-image", {"img_url": image_url})}
      )
      .then((data) => {
        document.querySelector('#load1').style.backgroundColor = '#1DB954';
        return postData("/songsnapapi/summarise", {"content": data.data})
      })
      .then((data) => {
        document.querySelector('#load2').style.backgroundColor = '#1DB954';
        return postData("/songsnapapi/generate-prompt", {"content": data.description, "songs": num_songs})
      })
      .then(data => {
        document.querySelector('#load3').style.backgroundColor = '#1DB954';
        return postData("/songsnapapi/generate-songs", {"content": data.data})
      })
      .then((data) => {
        document.querySelector('#load4').style.backgroundColor = '#1DB954';
        console.log(data.data)
      });

    //window.location.href = 'albums';
}


