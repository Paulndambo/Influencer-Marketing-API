const adsList = []

const ADS_BACKEND_URL = "http://127.0.0.1:8000/products/"

var ads = [];
var currentAdIndex = 0;
// Function to show the ad container
function showAd() {
    var adContainer = document.getElementById('ad-container');
    adContainer.style.display = 'block';
}

// Function to hide the ad container
function hideAd() {
    var adContainer = document.getElementById('ad-container');
    adContainer.style.display = 'none';
}

// Function to shuffle the ads array
function shuffleAds() {
    for (var i = ads.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        [ads[i], ads[j]] = [ads[j], ads[i]]; // Swap elements
    }
}


function fetchAds() {
    fetch(`${ADS_BACKEND_URL}`)
        .then(response => response.json())
        .then(adData => {
            ads = adData.results; // Assuming the API returns an array of ads
            shuffleAds();
            displayNextAd();
        })
        .catch(error => {
            console.error('Error fetching ad content:', error);
        }
    );
}


function displayNextAd() {
    if (ads.length === 0) {
        hideAd(); // No ads to display, hide the container
        return;
    }
    var adContainer = document.getElementById('ad-container');
    var currentAd = ads[currentAdIndex];
    adContainer.innerHTML = `
        <img src="${currentAd.product_url}" alt="Ad Image" width="200" height="150">
        <p>${currentAd.name}</p>
        <p>
            <a href="">Visit Site</a> <span> <button>Close Ad!</button> </span>
        </p>
    `;
    showAd();

    // Increment the ad index and loop back to the beginning if necessary
    currentAdIndex = (currentAdIndex + 1) % ads.length;

    setTimeout(displayNextAd, 10000); // Show the next ad after 10 seconds
}