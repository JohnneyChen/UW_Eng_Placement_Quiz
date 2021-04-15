$(function () {
  let queryForm = $("#filterAllForm");
  queryForm.on("submit", async (e) => {
    e.preventDefault(); //prevents form submission

    $("#chartDisplay").hide(); //hides chart if there was a previous chart rendered
    $("#dataCard").show(); //shows datacard incase it was hidden by searchToggle.js
    $("#dataTable").empty();

    let url =
      window.location.origin +
      queryForm.attr("action") +
      "?" +
      queryForm.serialize(); //generates url for api returning program query information
    let payload = await axios.get(url); //fetches data
    data = payload.data.data; //gets the actual data of the payload

    //creates new datatable based on data
    const newTable = createDatatable(data);

    //adds created table to dataTable display
    $("#dataTable").append(newTable);

    //convert query data for future chart rendering
    initializeAllDataGraph(data);

    //saves url for when chart is to be saved to dashboard (requires the url to make the same query when rendering dashboard elements)
    localStorage.setItem("url", url);
  });
});

//generating data for use of chart rendering
const initializeAllDataGraph = (data) => {
  //contains the name of the program or the program/ranking combination
  let labels = [];

  //contains the actual # of recommendations made for a specific program or program/ranking combination
  let dataSet = [];

  data.forEach((data) => {
    labels.push(data.key);
    dataSet.push(data.total_recommendations);
  });

  //saves labels and dataset to localStorage for later access to generate chart
  localStorage.setItem("labels", JSON.stringify(labels));
  localStorage.setItem("dataSet", JSON.stringify(dataSet));
};
