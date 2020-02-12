var config = {

          apiKey: "AIzaSyDTVLBlkzZxHfV02pbFKcIkOZnLPr76fbI",
          authDomain: "ucc2019-5bec6.firebaseapp.com",
          databaseURL: "https://ucc2019-5bec6.firebaseio.com",
          projectId: "ucc2019-5bec6",
          storageBucket: "ucc2019-5bec6.appspot.com",
          messagingSenderId: "705711290007",
          appId: "1:705711290007:web:880929afd7593fdca01bd2",
          measurementId: "G-SY9WQ7NV7C"

          };

        firebase.initializeApp(config);

function parseURLParams(url) {
    var queryStart = url.indexOf("?") + 1,
        queryEnd   = url.indexOf("#") + 1 || url.length + 1,
        query = url.slice(queryStart, queryEnd - 1),
        pairs = query.replace(/\+/g, " ").split("&"),
        parms = {}, i, n, v, nv;

    if (query === url || query === "") return;

    for (i = 0; i < pairs.length; i++) {
        nv = pairs[i].split("=", 2);
        n = decodeURIComponent(nv[0]);
        v = decodeURIComponent(nv[1]);

        if (!parms.hasOwnProperty(n)) parms[n] = [];
        parms[n].push(nv.length === 2 ? v : null);
    }
    return parms;
}

console.log("ghi");

let game;

const params = parseURLParams(window.location.href);
console.log(params)

let reviews = [];

async function getReviews() {
    await firebase.database().ref("/Reviews").once("value").then(_reviews => {
        _reviews.forEach(_review => {
            const review = _review.val();
            if(review.game == params.game) {
                reviews.push(review);
            }
        });
    });
}

(async () => {
    await getReviews();
    console.log(reviews);

    for(const review of reviews) {

        const container = document.createElement("div");
        container.setAttribute("class", "reviewContainer");

        const h1 = document.createElement("h1");
        h1.innerHTML = review.name;
        h1.setAttribute("id", "nameTitle");

        const secondh1 = document.createElement("h1");
        secondh1.innerHTML = review.review;
        secondh1.setAttribute("id", "reviewTitle");

        const thirdh1 = document.createElement("h1");
        thirdh1.innerHTML = review.game;
        thirdh1.setAttribute("id", "reviewTitle");   

        container.appendChild(thirdh1);     
        container.appendChild(secondh1);     
        container.appendChild(h1);     

        document.body.appendChild(container);
        // document.body.appendChild(h1);
        // document.body.appendChild(secondh1);

    }
})();


// game = params['game'][0];
// review = params['review'][0];
// name = params['name'][0];
// console.log(game, review, name);

// // Loop trough params['game']
// // create a 'gameTitle', 'reviewTitle', 'nameTitle'
// // Add the text to them


// document.getElementById("gameTitle").innerHTML = game;
// document.getElementById("reviewTitle").innerHTML = review;
// document.getElementById("nameTitle").innerHTML = name;