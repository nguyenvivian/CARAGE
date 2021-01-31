var firebaseConfig = {
    apiKey: "AIzaSyC2PcsXezCkb_GuNFDm4E-H_RouoagTrtY",
    authDomain: "formal-era-303305.firebaseapp.com",
    databaseURL: "https://formal-era-303305-default-rtdb.firebaseio.com",
    projectId: "formal-era-303305",
    storageBucket: "formal-era-303305.appspot.com",
    messagingSenderId: "314330842077",
    appId: "1:314330842077:web:1d7bd2d6aa300b52b0ec34",
    measurementId: "G-THYBJQN9Q7"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

//Reference to the db
var ref = firebase.database().ref('DensityData/Lot6A').orderByChild('TimeTaken');
let arr = [];
ref.once('value', (snapshot) => {
    snapshot.forEach((childSnapshot) => {
        var childKey = childSnapshot.key;
        var childData = childSnapshot.val();
        arr.push(childData);
    });

});
console.log(arr)

totalArr = new Map()

// arr.map(review => {
//     totalArr.set(review.TimeTaken, {
//         EXECUTIVE: review.EXECUTIVE,
//         GENERAL: review.GENERAL,
//         HANDICAP: review.HANDICAP,
//         PREFERRED: review.PREFERRED,
//         RESERVED: review.RESERVED,
//         Total: review.TOTAL,
//     });
// });
console.log(totalArr)

//     if (!isNaN(review.stars)) {
//         if (countryBasedReviews.has(review.country)) {
//             countryBasedReviews.set(review.country, {
//                 frequency: ++countryBasedReviews.get(review.country).frequency,
//                 totalStars: countryBasedReviews.get(review.country).totalStars + review.stars,
//                 avgStarsFromThisCountry: countryBasedReviews.get(review.country).totalStars / countryBasedReviews.get(review.country).frequency,
//             });
//         } else {
//             countryBasedReviews.set(review.country, {
//                 frequency: 1,
//                 totalStars: review.stars,
//                 avgStarsFromThisCountry: review.stars / 1,
//             });
//         }
// });

ref.on('child_added', function (snapshot) {
    console.log("newEntryAdded");
});

// Vis Spec: Styles that have the highest average rating
// styleAvgStarsVisSpec = {
//     "$schema": "https://vega.github.io/schema/vega-lite/v4.0.0-beta.8.json",
//     "description": "",
//     "width": 500,
//     "data": {
//         "values": arr
//     },
//     "mark": "bar",
//     "encoding": {
//         "x": {
//             "field": "style",
//             "axis": { "labelAngle": 45 },
//             "type": "nominal",
//             "title": "Style of Ramen",
//             "sort": "-y"
//         },
//         "y": {
//             "field": "TimeTaken",
//             "type": "quantitative",
//             "title": "Average Ramen Rating",
//         },
//     },
// };
// vegaEmbed('#styleAvgStarsVis', styleAvgStarsVisSpec, { actions: false });