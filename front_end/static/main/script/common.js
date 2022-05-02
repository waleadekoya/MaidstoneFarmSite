const getTime = () => {
    const today = new Date();
    // https://devhints.io/wip/intl-datetime
    // https://stackoverflow.com/a/54500197
    let options = {
        weekday: "long", year: "numeric", month: "long",
        day: "numeric", hour: "2-digit", minute: "2-digit",
        hour12: true, timeZoneName: 'short', timeZone: 'Africa/Lagos'
    };

    document.getElementById('date').innerHTML = today.toLocaleString('en-GB', options);
    console.log(today.toLocaleString());
};

getTime();

function getEggsSnapshot() {
    return fetch('/api/eggs-inventory/').then(
        response => response.json().then(data => {
            console.log(data.results[0]);
            return data.results[0];
        })
    ).catch(err => console.log('Fetch Error :-S', err))
}


// $("#managerTable td").each(function () {
//     if (this.textContent === "0") this.textContent = "-"
// })

const mainTable = document.getElementById("managerTable");

for (let i in mainTable.rows) {
    let row = mainTable.rows[i]
    //iterate trough columns
    //rows would be accessed using the "row" variable assigned in the for loop
    for (let j in row.cells) {
        let col = row.cells[j]
        console.log(col.innerText)
        console.log(typeof col.innerText)
        if (col.innerText === "0") {
            // https://www.generacodice.com/en/articolo/4775545/django-static-js-files-not-loading
            console.log(col.textContent)
            col.innerText = "0"
        }
        // do something
        //columns would be accessed using the "col" variable assigned in the for loop
    }
}
