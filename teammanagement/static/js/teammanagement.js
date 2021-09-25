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

function fetchDataWithDatesAsync(url, playerId)
{
  return $.ajax({
    url: url,
    type: 'GET',
    data: {
      'player_id': playerId,
    },
    dataType: 'json',
  });
}

function generateBodyWeightTab(playerId, dataResponse) {
  var sectionData = GetBodyWeightSectionData();

  sectionData.dataToDisplay.bodyWeight.data = dataResponse.bodyWeight;
  sectionData.allDates = dataResponse.allDates;

  if (sectionData.allDates.length > 0) {
    createTabScaffolding(sectionData.idPrefix, sectionData.title, sectionData.graph.hasGraph);
    generateChart(sectionData);
    generateTables(sectionData);
  }
}

function generateLiftingTab(playerId, dataResponse) {
  var sectionData = getLiftSectionData();

  sectionData.dataToDisplay.deadlift.data = dataResponse.deadlift;
  sectionData.dataToDisplay.squat.data = dataResponse.squat;
  sectionData.dataToDisplay.benchPress.data = dataResponse.benchPress;
  sectionData.allDates = dataResponse.allDates;
  
  if (sectionData.allDates.length > 0) {
    createTabScaffolding(sectionData.idPrefix, sectionData.title, sectionData.graph.hasGraph);
    generateChart(sectionData);
    generateTables(sectionData);
  }
}

function generateVelocityTab(playerId, dataResponse) {
  var sectionData = getVelocitySectionData();

  sectionData.dataToDisplay.exit.data = dataResponse.exit;
  sectionData.dataToDisplay.pitching.data = dataResponse.pitching;
  sectionData.dataToDisplay.outfield.data = dataResponse.outfield;
  sectionData.dataToDisplay.infield.data = dataResponse.infield;
  sectionData.allDates = dataResponse.allDates;
  
  if (sectionData.allDates.length > 0) {
    createTabScaffolding(sectionData.idPrefix, sectionData.title, sectionData.graph.hasGraph);
    generateChart(sectionData);
    generateTables(sectionData);
  }
}

function generateTimesTab(playerId, dataResponse) {
  var sectionData = getTimeSectionData();

  sectionData.dataToDisplay.sixty.data = dataResponse.sixty;
  sectionData.allDates = dataResponse.allDates;

  if (sectionData.allDates.length > 0) {
    createTabScaffolding(sectionData.idPrefix, sectionData.title, sectionData.graph.hasGraph);
    generateTables(sectionData);
  }
}

function GetBodyWeightSectionData() {
  return {
    allDates: [],
    dataToDisplay: {
      bodyWeight: {
        chartColor: 'rgb(199, 44, 58)',
        data: [],
        idPrefix: "bodyWeightData",
        table: {
          tabTitle: "Table"
        },
        title: "Body Weight"
      }
    },
    graph: {
      hasGraph: true,
      timeUnit: 'week',
      title: "Body Weight (lbs)",
    },
    idPrefix: "bodyWeight",
    metricLabel: "lbs",
    table: {
      columns: ['Date', 'Body Weight (lbs)']
    },
    title: "Body Weight"
  }
}

function getLiftSectionData() {
  return {
    allDates: [],
    dataToDisplay: {
      deadlift: {
        chartColor: 'rgb(199, 44, 58)',
        data: [],
        idPrefix: "deadlift",
        table: {
          tabTitle: "Deadlift"
        },
        title: "Deadlift"
      },
      squat: {
        chartColor: 'black',
        data: [],
        idPrefix: "squat",
        table: {
          tabTitle: "Squat"
        },
        title: "Squat"
      },
      benchPress: {
        chartColor: 'Gold',
        data: [],
        idPrefix: "benchPress",
        table: {
          tabTitle: "Bench"
        },
        title: "Bench Press"
      }
    },
    graph: {
      hasGraph: true,
      timeUnit: 'day',
      title: "Lift Results in Strength Points (SP)",
    },
    idPrefix: "lifting",
    metricLabel: "SP",
    table: {
      columns: ['Date', 'Strength Points (SP)', 'Lift Sets']
    },
    title: "Lifting"
  }
};

function getVelocitySectionData() {
  return {
    allDates: [],
    dataToDisplay: {
      exit: {
        chartColor: 'rgb(199, 44, 58)',
        data: [],
        idPrefix: "exit",
        table: {
          tabTitle: "Exit"
        },
        title: "Exit"
      },
      pitching: {
        chartColor: 'black',
        data: [],
        idPrefix: "pitching",
        table: {
          tabTitle: "Pitching"
        },
        title: "Pitching"
      },
      outfield: {
        chartColor: 'Gold',
        data: [],
        idPrefix: "outfield",
        table: {
          tabTitle: "Outfield"
        },
        title: "Outfield"
      },
      infield: {
        chartColor: 'Purple',
        data: [],
        idPrefix: "infield",
        table: {
          tabTitle: "Infield"
        },
        title: "Infield",
      }
    },
    graph: {
      hasGraph: true,
      timeUnit: 'month',
      title: "Velocity (MPH)"
    },
    idPrefix: "velocity",
    metricLabel: "MPH",
    table: {
      columns: ['Date', 'Velocity (MPH)']
    },
    title: "Velocities"
  }
}

function getTimeSectionData() {
  return {
    allDates: [],
    dataToDisplay: {
      sixty: {
        chartColor: 'rgb(199, 44, 58)',
        data: [],
        idPrefix: "sixty",
        table: {
          tabTitle: "60-yd Dash"
        },
        title: "60-yd Dash"
      }
    },
    graph: {
      hasGraph: false,
      timeUnit: 'month',
      title: "Time (s)"
    },
    idPrefix: "time",
    metricLabel: "s",
    table: {
      columns: ['Date', 'Time']
    },
    title: "Times"
  }
}

function createTabScaffolding(idPrefix, accordionTabTitle, hasGraph)
{
  var tabAppend = $(`
    <div id="${idPrefix}Data" class="accordion-item">
      <div id="${idPrefix}Heading" class="accordion-header text-center">
        <button id="${idPrefix}Button" class="accordion-button collapsed text-danger bg-dark text-center" type="button" data-bs-toggle="collapse" data-bs-target="#${idPrefix}Content" aria-expanded="false" aria-controls="${idPrefix}Content">
          <h3>
            <span class="text-shadow-lg">
              ${accordionTabTitle}
            </span>
            <span>
                <i class="text-light fa fa-plus-square"></i>
            </span>
          </h3>
        </button>
      </div>

      <div id="${idPrefix}Content" class="accordion-collapse collapse" aria-labelledby="${idPrefix}Heading" data-bs-parent="#accordion">
        <div id="${idPrefix}DataBody" class="accordion-body">
          <ul id="${idPrefix}Tabs" class="nav nav-tabs justify-content-center" role="tablist"></ul>
          <br>
          <div id="${idPrefix}TabContent" class="tab-content"></div>
        </div>
      </div>

    </div>
  `);

  if (hasGraph) {
    $(tabAppend).find(`#${idPrefix}Tabs`).append(
      `<li class="nav-item" role="presentation">
        <a id="${idPrefix}ChartTab" class="nav-link active" data-bs-toggle="tab" href="#${idPrefix}ChartContainer" role="tab" aria-controls="${idPrefix}ChartContainer" aria-selected="true">Graph</a>
      </li>`
    );
    $(tabAppend).find(`#${idPrefix}TabContent`).append(
      `<div id="${idPrefix}ChartContainer" class="tab-pane fade show active" style="height: 50vh; width: 100%" role="tabpanel" aria-labelledby="${idPrefix}ChartTab">
        <canvas id="${idPrefix}Chart"></canvas>
      </div>`
    );
  }

  $("#accordion").append(tabAppend);
}

function getDatasetDataArray(data) {
  var dataForDataset = [];
  data.forEach(tuple => dataForDataset.push({x: tuple[0], y: tuple[1]}));

  return dataForDataset;
}

function getChartDatasets(dataToDisplay) {
  var datasets = [];
  for (const dataCategory in dataToDisplay) {
    if (dataToDisplay[dataCategory].data.length > 0) {
      var categoryDataset = {
        label: dataToDisplay[dataCategory].title,
        backgroundColor: dataToDisplay[dataCategory].chartColor,
        borderColor: dataToDisplay[dataCategory].chartColor,
        borderWidth: 2,
        pointBackgroundColor: dataToDisplay[dataCategory].chartColor,
        fill: false,
        lineTension: 0,
        data: getDatasetDataArray(dataToDisplay[dataCategory].data),
      };

      datasets.push(categoryDataset);
    }
  }

  return datasets;
}

function generateChart(sectionData) {
  if ($("#".concat(sectionData.idPrefix).concat("Chart")).length)
  {
    var line_chart_options = {
      legend: {
        display: true
      },
      maintainAspectRatio: false,
      plugins: {
        legend: {
          labels: {
            font: {
              size: 10
            }
          }
        },
        title: {
          color: 'black',
          display: true,
          font: {
            size: 15
          },
          text: sectionData.graph.title 
        },
        tooltip: {
          callbacks: {
            label: function(context) {
              var label = context.dataset.label || '';

              if (label) {
                label += ': ';
              }

              label += context.parsed.y + ' ' + sectionData.metricLabel;

              return label;
            }
          }
        }
      },
      scales: {
        x: {
          bounds: 'labels',
          type: 'time',
          time: {
            parser: 'MM-DD-YYYY',
            unit: sectionData.graph.timeUnit,
            displayFormats: {
              day: 'MM/DD/YY',
              week: 'MM/DD/YY'
            },
            tooltipFormat: "MM/DD/YY"
          },
          ticks: {
            autoSkip: true,
            font: {
              size: 11
            },
            //maxTicksLimit: 20,
            includeBounds: true
          }
        },
        y: {
          ticks: {
            font: {
              size: 10
            }
          }, 
          title: {
            display: false,
            text: sectionData.metricLabel,
            font: {
              size: 10
            }
          }
        }
      }
    }
    var line_chart_data = {
      labels: sectionData.allDates,
      datasets: getChartDatasets(sectionData.dataToDisplay)
    }

    var ctx = document.getElementById(sectionData.idPrefix.concat("Chart")).getContext('2d');
    var chart = new Chart(ctx, {
          type: 'line',
          data: line_chart_data,
          options: line_chart_options
        });
  }
}

function generateTables(sectionData) {
  var sectionTabs = $(`#${sectionData.idPrefix}Tabs`);
  var sectionTabContent = $(`#${sectionData.idPrefix}TabContent`);
  var hasMultipleTables = sectionData.dataToDisplay.length > 1;

  for (const dataCategory in sectionData.dataToDisplay) {
    let currentCategory = sectionData.dataToDisplay[dataCategory];
    
    if (currentCategory.data.length > 0) {
      var tabToAppend;
      var tabContentToAppend;
      if (sectionData.graph.hasGraph) {
        tabToAppend = $(`
          <li class="nav-item" role="presentation">
            <a id="${currentCategory.idPrefix}TableTab" class="nav-link" data-bs-toggle="tab" href="#${currentCategory.idPrefix}TableContainer" role="tab" aria-controls="${currentCategory.idPrefix}TableContainer" aria-selected="false">
              ${currentCategory.table.tabTitle}
            </a>
          </li>
        `);

        tabContentToAppend = $(`
          <div id="${currentCategory.idPrefix}TableContainer" class="container tab-pane fade" role="tabpanel" aria-labelledby="${currentCategory.idPrefix}TableTab">
            <table id="${currentCategory.idPrefix}Table" class="table table-dark table-striped table-bordered">
              <thead id="${currentCategory.idPrefix}TableHead" class="">
                <tr id="${currentCategory.idPrefix}TableHeadRow" class="text-center"></tr>
              </thead>
              <tbody id="${currentCategory.idPrefix}TableBody"></tbody>
            </table>
          </div>
        `);
      }
      else {
        tabToAppend = $(`
          <li class="nav-item" role="presentation">
            <a id="${currentCategory.idPrefix}TableTab" class="nav-link active" data-toggle="tab" href="#${currentCategory.idPrefix}TableContainer" role="tab" aria-controls="${currentCategory.idPrefix}TableContainer" aria-selected="true">
              ${currentCategory.table.tabTitle}
            </a>
          </li>
        `);

        tabContentToAppend = $(`
          <div id="${currentCategory.idPrefix}TableContainer" class="container tab-pane fade show active" role="tabpanel" aria-labelledby="${currentCategory.idPrefix}TableTab">
            <table id="${currentCategory.idPrefix}Table" class="table table-dark table-striped table-bordered">
              <thead id="${currentCategory.idPrefix}TableHead" class="">
                <tr id="${currentCategory.idPrefix}TableHeadRow" class="text-center"></tr>
              </thead>
              <tbody id="${currentCategory.idPrefix}TableBody"></tbody>
            </table>
          </div>
        `);
      }

      for (const columnName of sectionData.table.columns) {
        $(tabContentToAppend).find(`#${currentCategory.idPrefix}TableHeadRow`).append(`
          <th class="col">${columnName}</th>
        `);
      } 

      for (const tuple of currentCategory.data) {
        let currentRow = $(`<tr class="text-center"></tr>`)
        for (const value of tuple) {
          $(currentRow).append(`
            <td class="align-middle">
              ${value}
            </td>
          `);
        }

        $(tabContentToAppend).find(`#${currentCategory.idPrefix}TableBody`).append(currentRow);
      }

      $(sectionTabs).append(tabToAppend);
      $(sectionTabContent).append(tabContentToAppend);
    }
  }
}