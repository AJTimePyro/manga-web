

// Displaying all pages of manga
window.onload = () => {
    const body = document.getElementById('page');

    for (const img in pageData) {

        // Creating tags
        var imgTag = document.createElement('img');

        // Adding Attributes
        imgTag.src = pageData[img];

        // Appending in DOM
        body.appendChild(imgTag);
    }
    
}