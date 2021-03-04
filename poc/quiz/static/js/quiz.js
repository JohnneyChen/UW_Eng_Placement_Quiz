$(function () {
  let toOpen = 1;
  if (!hasNotSubmitted) {
    $('#submitButton').prop('disabled', true)
  }
  const q1 = $('input[name="creative"]')
  const q2 = $('input[name="essay"]')
  const q3 = $('input[name="outdoors"]')
  const q4 = $('input[name="career"]')
  const q5 = $('input[name="group_work"]')
  const q6 = $('input[name="liked_courses"]')
  const q7 = $('input[name="disliked_courses"]')
  const q8 = $('input[name="join_clubs"]')
  const q9 = $('input[name="not_clubs"]')
  const q10 = $('input[name="liked_projects"]')
  const q11 = $('input[name="disliked_projects"]')
  const q12 = $('input[name="alternate_degree"]')
  const q13 = $('input[name="drawing"]')
  const q14 = $('input[name="industry"]')
  const questionArr = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14]

  const areAllAnswered = () => {
    let allAnswered = true
    let answered = Array(14).fill(false)

    questionArr.forEach((q, idx) => {
      for (let key in q) {
        answered[idx] = answered[idx] || q[key].checked
      }
    })

    for (let answer of answered) {
      allAnswered = allAnswered && answer
    }
    return allAnswered
  }

  const toEnableBtn = () => {
    if (areAllAnswered()) {
      $('#submitButton').prop('disabled', false)
    }
  }


  const openTab = () => {
    $(`#collapse${toOpen}`).toggleClass('in')
  }

  openTab()

  for (let i = 1; i < 15; ++i) {
    $(`#question${i}`).on('click', (e) => {
      if (e.target.className === 'panel-title') {
        toOpen = i
        openTab()
      }
    })
  }

  for (let i = 1; i < 14; ++i) {
    $(`#panel-body${i}`).on('click', (e) => {
      if (e.target.value !== undefined) {
        $(`#collapse${toOpen}`).toggleClass('in')
        toOpen = i + 1;
        $('html, body').animate({
          scrollTop: $(`#question${i + 1}`).offset().top
        }, 600);
        openTab()
        toEnableBtn()
      }
    })
  }

  $('#panel-body14').on('click', () => {
    toEnableBtn()
  })
})
