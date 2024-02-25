

// keydown handler

function handleKeyDown(event) {
    if (event.keyCode === 13) {
        submitRequest();
    }
}

let hostApi = "http://192.168.100.70:5005/api/v1"
let xtoxicaApi = `${hostApi}/xtoxica/predict` // GET with -d for data
let inputElement = document.getElementById("input-text");


function readyApi() {
    return fetch(hostApi)
        .then((response) => response.json())
        .then((json) => {console.log(json)})
        .catch((error) => {
            console.log(`--E--(ERR): ${error}`)
        })
}

readyApi()

function requestApi(data) {
    const url = `${xtoxicaApi}`

    return fetch(url, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: data
        })
        .then((response) => response.json())
        .then((json) => json)
        .catch((error) => console.log("Error while requestind xToxica", error))
}

function getInputValue() {
    let inputValue = inputElement.value;
    if (inputValue.length < 1) {
        console.log("No input provided")
        alert("You must provide some text")
        return false;
    }
    return inputValue;
}


function populatePredictions(predictions) {
    for (let key of Object.keys(predictions)) {
    for (let part of ["percentage", "height"]) {
        let id = `${key}-${part}`;
        // console.log(id)
        let elm = document.getElementById(id);
        // console.log(elm)

        let pred = predictions[key]

        if (part == "percentage") {
            pred = (pred*100)
            pred = String(pred);
            let preds = pred.split(".");
            pred = preds[0]


            let predP = `${pred}%`;
            elm.textContent = predP;
        }
        if (part == "height") {
            let predH = `${(pred*100)*2}px`
            elm.style.height = predH
        }
    }
}
}

function submitRequest() {
    inputText = getInputValue()
    if (inputText) {
        const inputdata = JSON.stringify({"data": inputText})
        console.log(`Input Text: ${inputdata}`); // Input Text: {"data":"I Love your work"}


        requestApi(inputdata)
            .then((response) => {
                let keys = Object.keys(response);
                let predictions = response[keys[0]];

                console.log(predictions);
                populatePredictions(predictions)
            })
            .catch((error) => {
                alert(error);
            })

    }
}

