let requestTimer;
let timeoutDuration = 5000;

//created new Murri grid with dragNDrop functionality
const grid = new Muuri('.grid', {
    dragEnabled: true
})

//event handler for when grid items are moved on drag
grid.on('move', () => {
    //creates array containing all charts and their positional orders
    const chartPositions = grid.getItems().map((item, idx) => {
        return {
            position: idx,
            chartId: item._element.children.item(0).children.item(0).dataset.id,
            chartName: item._element.children.item(0).children.item(0).id
        }
    })

    //request buffering to only make POST request to django after 5 seconds of no further dragging
    clearTimeout(requestTimer) //clears previous timer

    //sets new timer to send chart information after 5 seconds
    requestTimer = setTimeout(async () => {
        await axios.post('/reorder_dashboard/', { chartPositions }, { headers: { 'X-CSRFToken': csrftoken } })
    }, timeoutDuration)
})