

// Displaying Chapters
window.onload = () => {
    const body = document.getElementById('chapters');
    for (const chapter in chapterList) {

        var chapData = chapterList[chapter];

        // Creating tags
        var chapterDom = document.createElement('div');
        var aTag = document.createElement('a');

        // Adding Attributes
        aTag.href = `/chapters/${chapData['chapter-id']}`;
        aTag.innerText = chapData['chapter-title'];
        chapterDom.className = 'chapter';

        // Appending in DOM
        chapterDom.appendChild(aTag);
        body.appendChild(chapterDom);

    }
}

