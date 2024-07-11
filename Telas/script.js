function download_music() {
    var link_music = document.getElementById('link').value;

    fetch('http://127.0.0.1:5000/download_music', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ music: link_music })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao baixar música');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        alert('Música baixada com sucesso!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Erro ao baixar música');
    });
}

function download_playlist_music() {
    var link_playlist = document.getElementById('link').value;

    fetch('http://127.0.0.1:5000/download_playlist_music', {
        method: 'POST', // Altera o método para POST
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ playlist: link_playlist }) // Envia o link da playlist no corpo da solicitação
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao baixar a playlist');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        alert('Playlist baixada com sucesso!');
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao baixar a playlist');
    });
}

function download_video() {
    var link_video = document.getElementById('link').value;

    fetch('http://127.0.0.1:5000/download_video', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ video: link_video })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao baixar video');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        alert('Video baixado com sucesso!');
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Erro ao baixar video');
    });
}

function download_playlist_video() {
    var link_playlist = document.getElementById('link').value;

    fetch('http://127.0.0.1:5000/download_playlist_video', {
        method: 'POST', // Altera o método para POST
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ playlist: link_playlist }) // Envia o link da playlist no corpo da solicitação
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao baixar a playlist');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        alert('Playlist baixada com sucesso!');
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao baixar a playlist');
    });
}