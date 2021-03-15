$(function () {
    $('.alert').fadeOut(2000, () => {
        $('.alert').remove()
    })
    $('.flash-close').on('click', () => {
        $('.alert').remove()
    })
})