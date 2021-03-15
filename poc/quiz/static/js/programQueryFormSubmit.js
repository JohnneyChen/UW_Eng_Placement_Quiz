
$(function () {
    let queryForm = $('#filterProgramForm')
    queryForm.on('submit', async (e) => {
        e.preventDefault() //prevents form submission

        $('#chartDisplay').hide() //hides chart if there was a previous chart rendered
        $('#dataCard').show() //shows datacard incase it was hidden by searchToggle.js

        let url = window.location.origin + queryForm.attr('action') + '?' + queryForm.serialize() //generates url for api returning program query information
        let payload = await axios.get(url) //fetches data
        data = payload.data.data //gets the actual data of the payload

        //clears previous datatable if it was rendered by a past query
        $('#dataTable').empty()

        //creates new datatable based on data
        const newTable = createDatatable(data)

        //adds created table to dataTable display
        $('#dataTable').append(newTable)

        //convert query data for future chart rendering
        initializeProgramDataGraph(data)

        //saves url for when chart is to be saved to dashboard (requires the url to make the same query when rendering dashboard elements)
        localStorage.setItem('url', url)
    })
})

//creates new datatable from given data
const createDatatable = data => {
    let dataTable = document.createElement('table') //creates new table
    dataTable.classList.add('table') //adds table class for bootstrap styling
    let tr = dataTable.insertRow(-1) //inserts a row on the bottom of table for headers

    //creates header row from keys in data
    let cols = []
    for (let key in data[0]) {
        cols.push(key)
    }

    //inserts table headers containing the keys in data
    for (let col of cols) {
        const th = document.createElement('th')
        th.innerHTML = col
        tr.appendChild(th)
    }


    //creates new rows of data
    data.forEach((row) => {
        //creates new row
        const tr = dataTable.insertRow(-1)
        //for each key value pair in row, a cell is inserted with value inside
        for (let col in row) {
            //creates new cell
            const cell = tr.insertCell(-1)
            //populates new cell with value at that key
            cell.innerHTML = row[col]
        }
    })

    return dataTable
}

//generating data for use of chart rendering
const initializeProgramDataGraph = data => {
    //contains the name of the program or the program/ranking combination
    let labels = []

    //contains the actual # of recommendations made for a specific program or program/ranking combination
    let dataSet = []

    data.forEach((data) => {
        labels.push(data.program_position || data.program)
        dataSet.push(data.total_recommendations)
    })

    //saves labels and dataset to localStorage for later access to generate chart
    localStorage.setItem('labels', JSON.stringify(labels))
    localStorage.setItem('dataSet', JSON.stringify(dataSet))
}