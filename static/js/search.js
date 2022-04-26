

// Displaying search results
window.onload = () => {
    const body = document.getElementById('results');
    for (const data in query) {

        // Creating Tags
        var resultDom = document.createElement('div');
        var imgTags = document.createElement('img');
        var titleTags = document.createElement('a')

        // Adding some attributes
        imgTags.src = query[data]['img'];
        titleTags.href = query[data]['url'];
        titleTags.innerText = query[data]['title'];

        // Appending in DOM
        resultDom.appendChild(imgTags);
        resultDom.appendChild(titleTags);
        body.appendChild(resultDom);
    }
}

