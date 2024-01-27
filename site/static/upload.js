function fetchData() {
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

    bar1.style.backgroundColor = '#1DB954';
    
    const description = await fetchData();
    bar2.style.backgroundColor = '#1DB954';

    const summary = await fetchData();
    bar3.style.backgroundColor = '#1DB954';

    const songs = await fetchData();
    bar4.style.backgroundColor = '#1DB954';

    // redirect to albums.html
    window.location.href = 'albums';
}
