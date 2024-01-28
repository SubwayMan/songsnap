function imgToURI(img) {
    return new Promise(resolve => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.readAsDataURL(img);
    });
}

function vision(img) {
    return new Promise(resolve => setTimeout(resolve, 2000, 'my content'))
}

function summarize(img) {
    return new Promise(resolve => setTimeout(resolve, 2000, 'my content'))
}

function genSongs(img) {
    return new Promise(resolve => setTimeout(resolve, 2000, 'my content'))
}

function uploadDB(img, description, summary, songs) {
    return new Promise(resolve => setTimeout(resolve, 2000, 'my content'))
}

async function handleImageUpload(event) {
    const file = event.target.files[0];
    const uploadButton = document.querySelector('.upload-button');
    uploadButton.style.display = 'none';

    const loader = document.querySelector('.loader');
    loader.style.display = 'block';

    const uploadBar = document.querySelector('.upload_bar');
    uploadBar.style.display = 'flex';

    const bar1 = document.querySelector('#load1');
    const bar2 = document.querySelector('#load2');
    const bar3 = document.querySelector('#load3');
    const bar4 = document.querySelector('#load4');

    const URI = imgToURI(file);

    const description = await vision(URI);
    bar1.style.backgroundColor = '#1DB954';

    const summary = await summarize(description);
    bar2.style.backgroundColor = '#1DB954';

    const songs = await genSongs(description);
    bar3.style.backgroundColor = '#1DB954';

    await uploadDB(file, description, summary, songs);
    bar4.style.backgroundColor = '#1DB954';

    window.location.href = 'albums';
}
