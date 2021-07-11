$("#accordion").on("hide.bs.collapse show.bs.collapse", e => {
    $(e.target)
  .prev()
  .find("i:last-child")
  .toggleClass("fa-minus-square fa-plus-square");
});

$("#accordion").on("shown.bs.collapse", e => {
    $("html, body").animate(
      {
            scrollTop: $(e.target)
          .prev()
          .offset().top
      },
      400
    );
});

async function generateChart(chartId, metricName, dataType, label)
{
    if ($("#".concat(chartId).concat("Chart")).length)
    {
        const ajaxResponse = await getDataAndDates(metricName, dataType);

        const dates = ajaxResponse.dates;
        const data = ajaxResponse.data;

        var line_chart_options = {
            maintainAspectRatio: false,
            scales: {
                x: {
                    type: 'time',
                    distribution: 'linear',
                    time: {
                        parser: 'MM/DD/YYYY',
                        unit: 'month'
                    },
                    bounds: 'labels'
                },
                yAxes: [{
                    scaleLabel: {
                        display: true,
                        labelString: label
                    }
                }]
            },
            legend: {
                display: false
            }
        }
        var line_chart_data = {
            labels: dates,
            datasets: [
                {
                    label: label,
                    backgroundColor: 'transparent',
                    borderColor: 'rgb(199, 44, 58)',
                    borderWidth: 2,
                    pointBackgroundColor: 'rgb(199, 44, 58)',
                    data: data,
                    fill: false,
                    lineTension: 0
                }
            ]
        }

        var ctx = document.getElementById(chartId.concat("Chart")).getContext('2d');
        var chart = new Chart(ctx, {
                    type: 'line',
                    data: line_chart_data,
                    options: line_chart_options
                });
    }
}