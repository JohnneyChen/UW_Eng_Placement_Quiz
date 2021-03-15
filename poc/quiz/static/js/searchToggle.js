$(function () {
    // hides the program filter form on load
    $('#filterProgramForm').toggle()

    //selects the label of the toggle button
    const toggleLabel = $('#searchToggleLabel')

    //event listener for logic when toggle is clicked
    $('#searchToggle').on('click', () => {
        //resets chart to blank chart
        resetChartDisplay()

        //hides both data table and chart until new query is performed
        hideDatatable()
        hideChartDisplay()

        //toggles both forms
        toggleForms()

        //changes label to program form if it was all form, vice versa as well
        if (toggleLabel.html() === 'Search all programs') {
            toggleLabel.html('Search select programs')
        } else {
            toggleLabel.html('Search all programs')
        }
    })
})

const resetChartDisplay = () => {
    $('#graphContainer').empty()
    $('#graphContainer').append('<canvas id="myChart"><canvas>');
    $('#graphContainer').append('<button type="button" id="saveGraph" class="btn btn-success">Save to dashboard</button>');
}

const hideDatatable = () => {
    $('#dataCard').hide()
}

const hideChartDisplay = () => {
    $('#chartDisplay').hide()
}

const toggleForms = () => {
    $('#filterProgramForm').toggle({ duration: 200 })
    $('#filterAllForm').toggle({ duration: 200 })
}