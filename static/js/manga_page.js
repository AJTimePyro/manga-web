

// Nothing
window.onload = () => {
    
    const body = document.getElementById('page');
    
    var imgTag = document.createElement('img');
    
    imgTag.src = pageData[0];
    imgTag.referrerPolicy = 'strict-origin-when-cross-origin';
    body.appendChild(imgTag);
}