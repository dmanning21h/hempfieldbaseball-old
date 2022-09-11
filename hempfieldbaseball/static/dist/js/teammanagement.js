const accordionTabSlide = () => {
  $("#progressHeader")
    .animate({ opacity: 1 }, { queue: false, duration: 100 });

  $(".accordion-item")
    .animate({ opacity: 1 }, { queue: false, duration: 150 });
}

accordionTabSlide();

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

function fetchDataWithDatesAsync(url, playerId) {
  return $.ajax({
    url: url,
    type: 'GET',
    data: {
      'player_id': playerId,
    },
    dataType: 'json',
  });
}

function populateBodyWeightTab(dataResponse) {
  var bodyWeightSectionData = getBodyWeightSectionData();

  bodyWeightSectionData.dataToDisplay.bodyWeight.data = dataResponse.bodyWeight;
  bodyWeightSectionData.allDates = dataResponse.allDates;

  if (bodyWeightSectionData.allDates.length > 0) {
    generateChart(bodyWeightSectionData);
    generateTables(bodyWeightSectionData);
  }
}

function populateLiftingTab(dataResponse) {
  var liftSectionData = getLiftSectionData();

  liftSectionData.dataToDisplay.deadlift.data = dataResponse.deadlift;
  liftSectionData.dataToDisplay.squat.data = dataResponse.squat;
  liftSectionData.dataToDisplay.benchPress.data = dataResponse.benchPress;
  liftSectionData.allDates = dataResponse.allDates;

  if (liftSectionData.allDates.length > 0) {
    generateChart(liftSectionData);
    generateTables(liftSectionData);
  }
}

function populateVelocityTab(dataResponse) {
  var velocitySectionData = getVelocitySectionData();

  velocitySectionData.dataToDisplay.exit.data = dataResponse.exit;
  velocitySectionData.dataToDisplay.pitching.data = dataResponse.pitching;
  velocitySectionData.dataToDisplay.outfield.data = dataResponse.outfield;
  velocitySectionData.dataToDisplay.infield.data = dataResponse.infield;
  velocitySectionData.allDates = dataResponse.allDates;

  if (velocitySectionData.allDates.length > 0) {
    generateChart(velocitySectionData);
    generateTables(velocitySectionData);
  }
}

function populateWeightedMoundTab(dataResponse) {
  populateWeightedBallVelocityTab(dataResponse, "weightedMound", "Mound Velocity");
}

function populatePulldownTab(dataResponse) {
  populateWeightedBallVelocityTab(dataResponse, "pulldown", "Pulldown");
}

function populateWeightedBallVelocityTab(dataResponse, lowerName, upperName) {
  let sectionData = getWeightedBallVelocitySectionData(lowerName, upperName);

  sectionData.dataToDisplay[`${lowerName}ThreeOunce`].data = dataResponse.three;
  sectionData.dataToDisplay[`${lowerName}FourOunce`].data = dataResponse.four;
  sectionData.dataToDisplay[`${lowerName}FiveOunce`].data = dataResponse.five;
  sectionData.dataToDisplay[`${lowerName}SixOunce`].data = dataResponse.six;
  sectionData.dataToDisplay[`${lowerName}SevenOunce`].data = dataResponse.seven;
  sectionData.allDates = dataResponse.allDates;

  if (sectionData.allDates.length > 0) {
    generateChart(sectionData);
    generateTables(sectionData);
  }
}

function populatePlyoDrillsTab(dataResponse) {
  generatePlyoDrillChart(dataResponse.funnel_front, "funnelFront", "Funnel Front");
  generatePlyoDrillChart(dataResponse.step_back, "stepBack", "Step Back");
  generatePlyoDrillChart(dataResponse.drop_step, "dropStep", "Drop Step");
  generatePlyoDrillChart(dataResponse.walking_windup, "walkingWindup", "Walking Windup");
}

function generatePlyoDrillChart(plyoDrillData, htmlName, graphTitle) {
  var plyoDrillSectionData = getPlyoDrillSectionData(htmlName, graphTitle);

  plyoDrillSectionData.dataToDisplay.blue.data = plyoDrillData["450"];
  plyoDrillSectionData.dataToDisplay.red.data = plyoDrillData["225"];
  plyoDrillSectionData.dataToDisplay.yellow.data = plyoDrillData["150"];
  plyoDrillSectionData.dataToDisplay.gray.data = plyoDrillData["100"];
  plyoDrillSectionData.allDates = plyoDrillData.all_dates;

  if (plyoDrillSectionData.allDates.length > 0) {
    generateChart(plyoDrillSectionData);
  }
}

function populateTimesTab(dataResponse) {
  var timeSectionData = getTimeSectionData();

  timeSectionData.dataToDisplay.sixty.data = dataResponse.sixty;
  timeSectionData.allDates = dataResponse.allDates;

  if (timeSectionData.allDates.length > 0) {
    generateTables(timeSectionData);
  }
}

function getBodyWeightSectionData() {
  const bodyWeightMeta = createMetricTypeMetaDataObject("rgb(199, 44, 58)", "bodyWeight", "Table", "Weight");

  const bodyWeightTypeMetas = [bodyWeightMeta];
  const bodyWeightMainMeta = createMetricMetaDataObject("bodyWeight", "Body Weight", "lbs", true, bodyWeightTypeMetas);

  return createMetricSectionDataObject(bodyWeightMainMeta);
}

function getLiftSectionData() {
  const deadliftMeta = createMetricTypeMetaDataObject("rgb(199, 44, 58)", "deadlift");
  const squatMeta = createMetricTypeMetaDataObject("black", "squat");
  const benchPressMeta = createMetricTypeMetaDataObject("gold", "benchPress", "Bench Press");

  const liftTypeMetas = [deadliftMeta, squatMeta, benchPressMeta];
  const liftMeta = createMetricMetaDataObject("lift", "Lift", "SP", true, liftTypeMetas, "Lift Sets");

  return createMetricSectionDataObject(liftMeta);
};

function getVelocitySectionData() {
  const exitMeta = createMetricTypeMetaDataObject("rgb(199, 44, 58)", "exit");
  const pitchingMeta = createMetricTypeMetaDataObject("black", "pitching");
  const outfieldMeta = createMetricTypeMetaDataObject("gold", "outfield");
  const infieldMeta = createMetricTypeMetaDataObject("purple", "infield");

  const velocityTypeMetas = [exitMeta, pitchingMeta, outfieldMeta, infieldMeta];
  const velocityMeta = createMetricMetaDataObject("velocity", "Velocity", "MPH", true, velocityTypeMetas);

  return createMetricSectionDataObject(velocityMeta);
}

function getWeightedBallVelocitySectionData(lowerName, upperName) {
  const threeMeta = createMetricTypeMetaDataObject("lightskyblue", `${lowerName}ThreeOunce`, "3oz", "3oz");
  const fourMeta = createMetricTypeMetaDataObject("royalblue", `${lowerName}FourOunce`, "4oz", "4oz");
  const fiveMeta = createMetricTypeMetaDataObject("black", `${lowerName}FiveOunce`, "5oz", "5oz");
  const sixMeta = createMetricTypeMetaDataObject("orange", `${lowerName}SixOunce`, "6oz", "6oz");
  const sevenMeta = createMetricTypeMetaDataObject("red", `${lowerName}SevenOunce`, "7oz", "7oz");

  const weightedBallVelocityTypeMetas = [threeMeta, fourMeta, fiveMeta, sixMeta, sevenMeta];
  const weightedBallVelocityMeta = createMetricMetaDataObject(lowerName, upperName, "MPH", true, weightedBallVelocityTypeMetas);

  return createMetricSectionDataObject(weightedBallVelocityMeta);
}

function getPlyoDrillSectionData(htmlName, graphTitle) {
  const blueMeta = createMetricTypeMetaDataObject("blue", "blue", "450g", "450g");
  const redMeta = createMetricTypeMetaDataObject("orangered", "red", "225g", "225g");
  const yellowMeta = createMetricTypeMetaDataObject("gold", "yellow", "150g", "150g");
  const grayMeta = createMetricTypeMetaDataObject("dimgray", "gray", "100g", "100g");

  plyoDrillWeightMetas = [blueMeta, redMeta, yellowMeta, grayMeta];
  const plyoDrillMeta = createMetricMetaDataObject(htmlName, graphTitle, "MPH", true, plyoDrillWeightMetas);

  return createMetricSectionDataObject(plyoDrillMeta);
}

function getTimeSectionData() {
  const sixtyMeta = createMetricTypeMetaDataObject("rgb(199, 44, 58)", "sixty", "60-yd Dash");

  const timeTypeMetas = [sixtyMeta];
  const timeMeta = createMetricMetaDataObject("time", "Time", "s", false, timeTypeMetas);

  return createMetricSectionDataObject(timeMeta);
}

function createMetricTypeMetaDataObject(lineColor, name, alternateTabTitle = null, alternateGraphLabel = null) {
  return {
    lineColor: lineColor,
    lowerName: name,
    upperName: name.charAt(0).toUpperCase() + name.slice(1),
    alternateTabTitle: alternateTabTitle,
    alternateGraphLabel: alternateGraphLabel
  }
}

function createMetricTypeDataToDisplayObject(metricTypeMetaData) {
  const tabTitle = metricTypeMetaData.alternateTabTitle == null ?
    metricTypeMetaData.upperName : metricTypeMetaData.alternateTabTitle;
  const graphLabel = metricTypeMetaData.alternateGraphLabel == null ?
    metricTypeMetaData.upperName : metricTypeMetaData.alternateGraphLabel;

  return {
    chartColor: metricTypeMetaData.lineColor,
    data: [],
    idPrefix: metricTypeMetaData.lowerName,
    table: {
      tabTitle: tabTitle
    },
    title: graphLabel
  }
}

function createMetricMetaDataObject(name, title, unitOfMeasure, hasGraph, metricTypeMetaDatas, additionalColumn = null) {
  const upperName = name.charAt(0).toUpperCase() + name.slice(1);
  const titleString = `${title} (${unitOfMeasure})`;

  const columns = [titleString];
  if (additionalColumn != null) {
    columns.push(additionalColumn);
  }

  return {
    lowerName: name,
    upperName: upperName,
    metricTypes: metricTypeMetaDatas,
    unitOfMeasure: unitOfMeasure,
    hasGraph: hasGraph,
    columns: columns
  }
}

function createMetricSectionDataObject(metricMetaData) {
  return {
    allDates: [],
    dataToDisplay:
      metricMetaData.metricTypes.reduce(function (map, metricType) {
        map[metricType.lowerName] = createMetricTypeDataToDisplayObject(metricType);
        return map;
      }, {}),
    graph: {
      hasGraph: metricMetaData.hasGraph,
      timeUnit: 'month',
      title: metricMetaData.columns[0]
    },
    idPrefix: metricMetaData.lowerName,
    metricLabel: metricMetaData.unitOfMeasure,
    table: {
      columns: ['Date', ...metricMetaData.columns]
    }
  }
}

function getDatasetDataArray(data) {
  var dataForDataset = [];
  data.forEach(tuple => dataForDataset.push({ x: tuple[0], y: tuple[1] }));

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
  if ($("#".concat(sectionData.idPrefix).concat("Chart")).length) {
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
            label: function (context) {
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