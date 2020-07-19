$(document).ready(function () {

  if (sessionStorage.getItem("pageState")) {
    // on page reload, from recommendations page

    $(".collapse").collapse('show');
    $('#submitButton').prop('disabled', false);
    sessionStorage.clear();
  }

  $('input[name="creative"]').click(function () {
    if ($(this).attr('value') == 'creative' || 'somewhat_creative' || 'not_creative') {
      $('html, body').animate({
        scrollTop: $("#question2").offset().top
      }, 600);
      $("#collapse2").collapse('show');
    }
  });

  $('input[name="essay"]').click(function () {
    if ($(this).attr('value') == 'yes' || 'partial' || 'no') {
      $('html, body').animate({
        scrollTop: $("#question3").offset().top
      }, 600);
      $("#collapse3").collapse('show');
    }
  });

  $('input[name="outdoors"]').click(function () {
    if ($(this).attr('value') == 'outdoors' || 'limited' || 'indoors') {
      $('html, body').animate({
        scrollTop: $("#question4").offset().top
      }, 600);
      $("#collapse4").collapse('show');
    }
  });

  $('input[name="career"]').click(function () {
    if ($(this).attr('value') == 'moving_parts' || 'buildings' || 'sensors' || 'resources' || 'molecules' || 'programming' || 'optimizing') {
      $('html, body').animate({
        scrollTop: $("#question5").offset().top
      }, 600);
      $("#collapse5").collapse('show');
    }
  });

  $('input[name="group_work"]').click(function () {
    if ($(this).attr('value') == 'yes' || 'occasionally' || 'no') {
      $('html, body').animate({
        scrollTop: $("#question6").offset().top
      }, 600);
      $("#collapse6").collapse('show');
    }
  });

  $('input[name="liked_courses"]').click(function () {
    if ($(this).attr('value') == 'autoshop' || 'biology' || 'business' || 'chemistry' || 'computer_science' || 'geography' || 'history' || 'language_arts' || 'math' || 'physics' || 'visual_arts') {
      $('html, body').animate({
        scrollTop: $("#question7").offset().top
      }, 600);
      $("#collapse7").collapse('show');
    }
  });

  $('input[name="disliked_courses"]').click(function () {
    if ($(this).attr('value') == 'autoshop' || 'biology' || 'business' || 'chemistry' || 'computer_science' || 'geography' || 'history' || 'language_arts' || 'math' || 'physics' || 'visual_arts') {
      $('html, body').animate({
        scrollTop: $("#question8").offset().top
      }, 600);
      $("#collapse8").collapse('show');
    }
  });

  $('input[name="join_clubs"]').click(function () {
    if ($(this).attr('value') == 'art/design' || 'autoshop' || 'business' || 'consulting' || 'environment' || 'robotics' || 'hacker_club' || 'student_council') {
      $('html, body').animate({
        scrollTop: $("#question9").offset().top
      }, 600);
      $("#collapse9").collapse('show');
    }
  });

  $('input[name="not_clubs"]').click(function () {
    if ($(this).attr('value') == 'art/design' || 'autoshop' || 'business' || 'consulting' || 'environment' || 'robotics' || 'hacker_club' || 'student_council') {
      $('html, body').animate({
        scrollTop: $("#question10").offset().top
      }, 600);
      $("#collapse10").collapse('show');
    }
  });

  $('input[name="liked_projects"]').click(function () {
    if ($(this).attr('value') == 'prototyping_instrument' || 'olympic_village' || 'robot' || 'supercomputer' || 'mars_water_treatment' || 'battery' || 'uber_pool') {
      $('html, body').animate({
        scrollTop: $("#question11").offset().top
      }, 600);
      $("#collapse11").collapse('show');
    }
  });
  $('input[name="disliked_projects"]').click(function () {
    if ($(this).attr('value') == 'prototyping_instrument' || 'olympic_village' || 'robot' || 'supercomputer' || 'mars_water_treatment' || 'battery' || 'uber_pool') {
      $('html, body').animate({
        scrollTop: $("#question12").offset().top
      }, 600);
      $("#collapse12").collapse('show');
    }
  });

  $('input[name="alternate_degree"]').click(function () {
    if ($(this).attr('value') == 'applied_science' || 'business' || 'cs' || 'econ' || 'lit' || 'env' || 'fin' || 'geo' || 'design' || 'health' || 'marketing' || 'math' || 'poli_sci' || 'psych' || 'visual_arts') {
      $('html, body').animate({
        scrollTop: $("#question13").offset().top
      }, 600);
      $("#collapse13").collapse('show');
    }
  });

  $('input[name="drawing"]').click(function () {
    if ($(this).attr('value') == 'good' || 'partial' || 'no') {
      $('html, body').animate({
        scrollTop: $("#question14").offset().top
      }, 600);
      $("#collapse14").collapse('show');
    }
  });

  $('input[name="industry"]').click(function () {
    if ($(this).attr('value') == 'architecture' || 'automotive' || 'business' || 'construction' || 'health' || 'environment' || 'manufacturing' || 'technology') {
      $('#submitButton').prop('disabled', false);
    }

  });

  $("#submit").submit(function () {
    var pageState = 1;
    sessionStorage.setItem("pageState", pageState);
  })
});


function openRequiredQuestions() {
  var q1 = $('input[name="problem_type"]:checked');
  var q2 = $('input[name="creative"]:checked');
  var q3 = $('input[name="essay"]:checked');
  var q4 = $('input[name="outdoors"]:checked');
  var q5 = $('input[name="career"]:checked');
  var q6 = $('input[name="group_work"]:checked');
  var q7 = $('input[name="liked_courses"]:checked');
  var q8 = $('input[name="disliked_courses"]:checked');
  var q9 = $('input[name="programming"]:checked');
  var q10 = $('input[name="join_clubs"]:checked');
  var q11 = $('input[name="not_clubs"]:checked');
  var q12 = $('input[name="liked_projects"]:checked');
  var q13 = $('input[name="disliked_projects"]:checked');
  var q14 = $('input[name="tv_shows"]:checked');
  var q15 = $('input[name="alternate_degree"]:checked');
  var q16 = $('input[name="expensive_equipment"]:checked');
  var q17 = $('input[name="drawing"]:checked');
  var q18 = $('input[name="industry"]:checked');

  if (q1.value == null) {
    $("#collapse1").collapse('show');
  }
  if (q2.value == null) {
    $("#collapse2").collapse('show');
  }
  if (q3.value == null) {
    $("#collapse3").collapse('show');
  }
  if (q4.value == null) {
    $("#collapse4").collapse('show');
  }
  if (q5.value == null) {
    $("#collapse5").collapse('show');
  }
  if (q6.value == null) {
    $("#collapse6").collapse('show');
  }
  if (q7.value == null) {
    $("#collapse7").collapse('show');
  }
  if (q8.value == null) {
    $("#collapse8").collapse('show');
  }
  if (q9.value == null) {
    $("#collapse9").collapse('show');
  }
  if (q10.value == null) {
    $("#collapse10").collapse('show');
  }
  if (q11.value == null) {
    $("#collapse11").collapse('show');
  }
  if (q12.value == null) {
    $("#collapse12").collapse('show');
  }
  if (q13.value == null) {
    $("#collapse13").collapse('show');
  }
  if (q14.value == null) {
    $("#collapse14").collapse('show');
  }
  if (q15.value == null) {
    $("#collapse15").collapse('show');
  }
  if (q16.value == null) {
    $("#collapse16").collapse('show');
  }
  if (q17.value == null) {
    $("#collapse17").collapse('show');
  }
  if (q18.value == null) {
    $("#collapse18").collapse('show');
  }

  return true;
}

