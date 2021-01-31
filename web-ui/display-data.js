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
ref.on('child_added', (childSnapshot) => {
    var childData = childSnapshot.val();
    addDensityDataElement(childData.TimeTaken, childData.EXECUTIVE,
        childData.GENERAL, childData.HANDICAP, childData.PREFERRED,
        childData.RESERVED, childData.Total);
});

let densityMap = new Map()

function formatDate(dateTime) {
    dateObj = new Date(dateTime);
    let mmddyyyy = dateObj.toLocaleDateString('en-US');
    let hhmm = dateObj.toLocaleTimeString('en-US', { hour12: false })
    return mmddyyyy + ' ' + hhmm
}

function addDensityDataElement(TimeTaken, EXECUTIVE, GENERAL, HANDICAP, PREFERRED, RESERVED, Total) {
    densityMap.set(formatDate(TimeTaken), {
        EXECUTIVE: EXECUTIVE,
        GENERAL: GENERAL,
        HANDICAP: HANDICAP,
        PREFERRED: PREFERRED,
        RESERVED: RESERVED,
        Total: Total,
    });
    let flattenedDensity = Array.from(densityMap).map(
        ([TimeTaken, { EXECUTIVE, GENERAL, HANDICAP, PREFERRED, RESERVED, Total }]) =>
            ({ TimeTaken, EXECUTIVE, GENERAL, HANDICAP, PREFERRED, RESERVED, Total })
    );

    // Vis Spec: Total Vacancy
    densityTotal = {
        "$schema": "https://vega.github.io/schema/vega-lite/v4.0.0-beta.8.json",
        "description": "Total Parking Lot Vacancy",
        "width": 500,
        "data": {
            "values": flattenedDensity
        },
        "mark": "bar",
        "encoding": {
            "x": {
                "field": "TimeTaken",
                "axis": { "labelAngle": 45 },
                "type": "nominal",
                "title": "Time Recorded",
            },
            "y": {
                "field": "Total",
                "type": "quantitative",
                "title": "Proportion of Total Lot Vacant",
            },
        },
    };
    vegaEmbed('#densityTotalVis', densityTotal, { actions: false });

    // Vis Spec: General Vacancy
    densityGeneral = {
        "$schema": "https://vega.github.io/schema/vega-lite/v4.0.0-beta.8.json",
        "description": "General Parking Lot Vacancy",
        "width": 500,
        "data": {
            "values": flattenedDensity
        },
        "mark": "bar",
        "encoding": {
            "x": {
                "field": "TimeTaken",
                "axis": { "labelAngle": 45 },
                "type": "nominal",
                "title": "Time Recorded",
            },
            "y": {
                "field": "GENERAL",
                "type": "quantitative",
                "title": "Proportion of General Stalls Vacant",
            },
        },
    };
    vegaEmbed('#densityGeneralVis', densityGeneral, { actions: false });

    // Vis Spec: Preferred Vacancy
    densityPreferred = {
        "$schema": "https://vega.github.io/schema/vega-lite/v4.0.0-beta.8.json",
        "description": "Preferred Parking Lot Vacancy",
        "width": 500,
        "data": {
            "values": flattenedDensity
        },
        "mark": "bar",
        "encoding": {
            "x": {
                "field": "TimeTaken",
                "axis": { "labelAngle": 45 },
                "type": "nominal",
                "title": "Time Recorded",
            },
            "y": {
                "field": "PREFERRED",
                "type": "quantitative",
                "title": "Proportion of Preferred Stalls Vacant",
            },
        },
    };
    vegaEmbed('#densityPreferredVis', densityPreferred, { actions: false });

    // Vis Spec: Reserved Vacancy
    densityReserved = {
        "$schema": "https://vega.github.io/schema/vega-lite/v4.0.0-beta.8.json",
        "description": "Reserved Parking Lot Vacancy",
        "width": 500,
        "data": {
            "values": flattenedDensity
        },
        "mark": "bar",
        "encoding": {
            "x": {
                "field": "TimeTaken",
                "axis": { "labelAngle": 45 },
                "type": "nominal",
                "title": "Time Recorded",
            },
            "y": {
                "field": "RESERVED",
                "type": "quantitative",
                "title": "Proportion of Reserved Stalls Vacant",
            },
        },
    };
    vegaEmbed('#densityReservedVis', densityReserved, { actions: false });

    // Vis Spec: Executive Vacancy
    densityExecutive = {
        "$schema": "https://vega.github.io/schema/vega-lite/v4.0.0-beta.8.json",
        "description": "Executive Parking Lot Vacancy",
        "width": 500,
        "data": {
            "values": flattenedDensity
        },
        "mark": "bar",
        "encoding": {
            "x": {
                "field": "TimeTaken",
                "axis": { "labelAngle": 45 },
                "type": "nominal",
                "title": "Time Recorded",
            },
            "y": {
                "field": "EXECUTIVE",
                "type": "quantitative",
                "title": "Proportion of Executive Stalls Vacant",
            },
        },
    };
    vegaEmbed('#densityExecutiveVis', densityExecutive, { actions: false });


    // Vis Spec: Handicap Vacancy
    densityHandicap = {
        "$schema": "https://vega.github.io/schema/vega-lite/v4.0.0-beta.8.json",
        "description": "Handicap Parking Lot Vacancy",
        "width": 500,
        "data": {
            "values": flattenedDensity
        },
        "mark": "bar",
        "encoding": {
            "x": {
                "field": "TimeTaken",
                "axis": { "labelAngle": 45 },
                "type": "nominal",
                "title": "Time Recorded",
            },
            "y": {
                "field": "HANDICAP",
                "type": "quantitative",
                "title": "Proportion of Handicap Stalls Vacant",
            },
        },
    };
    vegaEmbed('#densityHandicapVis', densityHandicap, { actions: false });
}
