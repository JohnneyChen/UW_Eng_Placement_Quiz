//note* I used model instead of modal because bootstrap overrides modal class
//selects all model open buttons
const openModelButtons = document.querySelectorAll('[data-model-target]')

//selects all model close buttons
const closeModelButtons = document.querySelectorAll('[data-close-button]')

//selected overlay
const overlay = document.querySelector('#overlay')

//added event listener to open buttons for model and overlay display
openModelButtons.forEach(button => {
    button.addEventListener('click', () => {
        if (drag) return
        //finds the targeted model using the data-model-target attribute on open buttons
        const model = document.querySelector(button.dataset.modelTarget)
        openModel(model)
    })
})

//adds active class to both overlay and model to show them (refer to queryForm.css for specific styles)
const openModel = model => {
    model.classList.add('active')
    overlay.classList.add('active')
}

//added event listener to close buttons for model and overlay hiding
closeModelButtons.forEach(button => {
    button.addEventListener('click', () => {
        //finds the targeted model by finding closest model to the close button
        const model = button.closest('.model')
        closeModel(model)
    })

})

//removes active class to both overlay and model to hide them (refer to queryForm.css for specific styles)
const closeModel = model => {
    model.classList.remove('active')
    overlay.classList.remove('active')
}