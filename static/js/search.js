

// Displaying search results
window.onload = () => {
    const body = document.getElementById('results');
    for (const data in query) {

        // Creating Tags
        var resultDom = document.createElement('div');
        var imgTag = document.createElement('img');
        var imgATag = document.createElement('a');
        var titleTag = document.createElement('a')

        // Adding some attributes
        imgTag.src = query[data]['img'];
        titleTag.href = `/manga/${query[data]['url-data']}`;
        imgATag.href = titleTag.href;
        titleTag.innerText = query[data]['title'];
        resultDom.className = 'manga';
        imgATag.className = 'manga-poster';
        titleTag.className = 'manga-title';

        // Appending in DOM
        imgATag.appendChild(imgTag);
        resultDom.appendChild(imgATag);
        resultDom.appendChild(titleTag);
        body.appendChild(resultDom);
    }
}

