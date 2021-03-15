$(function () {
    $('#graphFormSubmit').on('submit', (e) => {
        //prevents form from submitting
        e.preventDefault()

        //clears chart display to prepare for newly rendered chart
        resetChartDisplay()

        //shows chart incase it was hidden by QueryForm submission logic or searchToggle
        showChartDisplay()

        //retrieves values inputted in form
        const title = e.target[0].value
        const type = e.target[1].value
        const width = parseInt(e.target[2].value)
        const height = parseInt(e.target[3].value)

        //retrieves data stored by QueryForm submission for axis labels and actual values
        const labels = JSON.parse(localStorage.getItem('labels'))
        const dataSet = JSON.parse(localStorage.getItem('dataSet'))

        //stores dimensions and information regarding chart instance for saving to dashboard
        localStorage.setItem('width', width)
        localStorage.setItem('height', height)
        localStorage.setItem('title', title)
        localStorage.setItem('type', type)

        //sets canvas's dimensions to values from form
        $('#myChart').width(width).height(height)

        //creates new chart using Chart.js
        var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: type,
            data: {
                labels: labels,
                datasets: [{
                    label: title,
                    data: dataSet,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: false,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
        //Note* because the canvas is cleared everytime, the event listener to saveGraph has to be re-attached every time a graph is rendered
        //when saveGraph is clicked
        $('#saveGraph').on('click', async () => {
            //retrieves nessesary chart data to POST to backend
            const title = localStorage.getItem('title')
            const type = localStorage.getItem('type')
            const width = parseInt(localStorage.getItem('width'))
            const height = parseInt(localStorage.getItem('height'))
            const url = localStorage.getItem('url')

            //gets csrf token to have POST request be accepted
            const csrftoken = Cookies.get('csrftoken')

            //sending POST request to backen to save instance of chart
            await axios.post('/dashboard/',
                {
                    title,
                    type,
                    width,
                    height,
                    url
                }
                , { headers: { 'X-CSRFToken': csrftoken } })
            //shows success message
            $('#graphContainer').append('<p id="successfulChartSaveMsg">Successfully saved your chart to the dashboard</p>').css('color', 'green')

            //remove saveGraph button to prevent more submissions
            $('#saveGraph').remove()

            //fade out success message then delete success message
            $('#successfulChartSaveMsg').fadeOut(3000, () => $('#successfulChartSaveMsg').remove())

        })
    })


})


const showChartDisplay = () => {
    $('#chartDisplay').show()
}