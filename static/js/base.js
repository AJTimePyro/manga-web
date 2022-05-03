

// For search Box
function searchQuery(e) {
    var query
    query = document.querySelector('#search-box input').value;
    window.location.href = `/?search=${query}`;
}

// For enter in search box
document.getElementById(
    "search-box"
).addEventListener(
    'keypress',
    (e)=> {
        if (e.key == "Enter") {
            searchQuery(e);
        };
    }
);

// On clicking on search icon
document.getElementById(
    "search-btn"
).addEventListener(
    'click',
    (e)=> {
        console.log('hi')
        searchQuery(e);
    }
);

