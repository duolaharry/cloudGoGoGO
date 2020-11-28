var ws = new WebSocket("ws://192.168.0.121/ws/");

ws.onopen = function(event) {
    zingchart.render({
      id: 'myChartBar',
      data: chartConfigBar,
      height: '100%',
      width: '100%',
      defaults: {
        fontFamily: 'sans-serif'
      }
    });
    zingchart.render({
      id: 'myChartBar1',
      data: chartConfigBar1,
      height: '100%',
      width: '100%',
      defaults: {
        fontFamily: 'sans-serif'
      }
    });
    zingchart.render({
        id: 'myChartLine',
        data: chartConfigLine,
        height: '100%',
        width: '100%'
    });
    zingchart.render({
        id: 'myChartLine1',
        data: chartConfigLine1,
        height: '100%',
        width: '100%'
    });
    zingchart.render({
        id: 'myChartLine2',
        data: chartConfigLine2,
        height: '100%',
        width: '100%'
    });
    zingchart.render({
      id: 'myChartPie',
      data: chartConfigPie
    });
    zingchart.render({
      id: 'myChartPie1',
      data: chartConfigPie1
    });
};

ws.onmessage = function(event) {
    command = event.data;
    arr = command.split(' ');

    if (arr[0] == "allpeople") {
        for (var i = 0; i < chartConfigBar.series.length; i++) {
            if (chartConfigBar.series[i].text == arr[1]) {
                chartConfigBar.series[i].values[0] = parseInt(arr[2], 10);
                break;
            }
        }
        if (arr[1] == "douyu") {
            chartConfigPie.graphset[0].labels[0].text = arr[2];
            zingchart.render({
              id: 'myChartPie',
              data: chartConfigPie
            });
        }
        if (arr[1] == "huya") {
            chartConfigPie1.graphset[0].labels[0].text = arr[2];
            zingchart.render({
              id: 'myChartPie1',
              data: chartConfigPie1
            });
        }
        zingchart.render({
          id: 'myChartBar',
          data: chartConfigBar,
          height: '100%',
          width: '100%',
          defaults: {
            fontFamily: 'sans-serif'
          }
        });

        if (arr[1] == "douyu") {
            for (var i = 0; i < 11 - 1; i++) {
                chartConfigLine.scaleX.labels[i] = chartConfigLine.scaleX.labels[i + 1];
                chartConfigLine.series[0].values[i] = chartConfigLine.series[0].values[i + 1];
                chartConfigLine.series[1].values[i] = chartConfigLine.series[1].values[i + 1];
            }
            chartConfigLine.scaleX.labels[10] = arr[4];
            chartConfigLine.series[0].values[10] = parseInt(arr[2], 10);
        } else if (arr[1] == "huya") {
            chartConfigLine.series[1].values[10] = parseInt(arr[2], 10);
        } else {
            // do nothing
        }
        var max_val = 0;
        for (var i = 0; i < 11; i++) {
            if (chartConfigLine.series[0].values[i] > max_val) {
                max_val = chartConfigLine.series[0].values[i];
            }
            if (chartConfigLine.series[1].values[i] > max_val) {
                max_val = chartConfigLine.series[1].values[i];
            }
        }
        max_val = parseInt(max_val * 1.1, 10);
        var step = parseInt(max_val / 5, 10);
        chartConfigLine.scaleY.values = "0:" + max_val.toString() + ":" + step.toString();
        zingchart.render({
            id: 'myChartLine',
            data: chartConfigLine,
            height: '100%',
            width: '100%'
        });
    } else if (arr[0] == "allpopu") {
        for (var i = 0; i < chartConfigBar1.series.length; i++) {
            if (chartConfigBar1.series[i].text == arr[1]) {
                chartConfigBar1.series[i].values[0] = parseInt(arr[2], 10);
                break;
            }
        }
        if (arr[1] == "douyu") {
            chartConfigPie.graphset[1].labels[0].text = arr[2];
            zingchart.render({
              id: 'myChartPie',
              data: chartConfigPie
            });
        }
        if (arr[1] == "huya") {
            chartConfigPie1.graphset[1].labels[0].text = arr[2];
            zingchart.render({
              id: 'myChartPie1',
              data: chartConfigPie1
            });
        }
        zingchart.render({
          id: 'myChartBar1',
          data: chartConfigBar1,
          height: '100%',
          width: '100%',
          defaults: {
            fontFamily: 'sans-serif'
          }
        });

        if (arr[1] == "douyu") {
            var max_val = 0;
            for (var i = 0; i < 11 - 1; i++) {
                chartConfigLine1.scaleX.labels[i] = chartConfigLine1.scaleX.labels[i + 1];
                chartConfigLine1.series[0].values[i] = chartConfigLine1.series[0].values[i + 1];
                if (chartConfigLine1.series[0].values[i] > max_val) {
                    max_val = chartConfigLine1.series[0].values[i];
                }
            }
            chartConfigLine1.series[0].values[10] = parseInt(arr[2], 10);
            if (parseInt(arr[2], 10) > max_val) {
                max_val = parseInt(arr[2], 10);
            }
            max_val = parseInt(max_val * 1.1, 10);
            var step = parseInt(max_val / 5, 10);
            chartConfigLine1.scaleY.values = "0:" + max_val.toString() + ":" + step.toString();
            chartConfigLine1.scaleX.labels[10] = arr[4];
            zingchart.render({
                id: 'myChartLine1',
                data: chartConfigLine1,
                height: '100%',
                width: '100%'
            });
        } else if (arr[1] == "huya") {
            var max_val = 0;
            for (var i = 0; i < 11 - 1; i++) {
                chartConfigLine2.scaleX.labels[i] = chartConfigLine2.scaleX.labels[i + 1];
                chartConfigLine2.series[0].values[i] = chartConfigLine2.series[0].values[i + 1];
                if (chartConfigLine2.series[0].values[i] > max_val) {
                    max_val = chartConfigLine2.series[0].values[i];
                }
            }
            chartConfigLine2.series[0].values[10] = parseInt(arr[2], 10);
            if (parseInt(arr[2], 10) > max_val) {
                max_val = parseInt(arr[2], 10);
            }
            max_val = parseInt(max_val * 1.1, 10);
            var step = parseInt(max_val / 5, 10);
            chartConfigLine2.scaleY.values = "0:" + max_val.toString() + ":" + step.toString();
            chartConfigLine2.scaleX.labels[10] = arr[4];
            zingchart.render({
                id: 'myChartLine2',
                data: chartConfigLine2,
                height: '100%',
                width: '100%'
            });
        } else {
            // do nothing
        }
    } else if (arr[0] == "clear") {
        for (var i = 0; i < 10; i++) {
            chartConfigPie.graphset[0].series[i].text = '';
            chartConfigPie.graphset[0].series[i].values[0] = 0;

            chartConfigPie.graphset[1].series[i].text = '';
            chartConfigPie.graphset[1].series[i].values[0] = 0;

            chartConfigPie1.graphset[0].series[i].text = '';
            chartConfigPie1.graphset[0].series[i].values[0] = 0;

            chartConfigPie1.graphset[1].series[i].text = '';
            chartConfigPie1.graphset[1].series[i].values[0] = 0;
        }
        zingchart.render({
          id: 'myChartPie',
          data: chartConfigPie
        });
        zingchart.render({
          id: 'myChartPie1',
          data: chartConfigPie1
        });
    } else if (arr[0] == "eachpeople") {
        var series = chartConfigPie.graphset[0].series;
        if (arr[1] == "huya") {
            series = chartConfigPie1.graphset[0].series;
        }
        for (var i = 0; i < series.length; i++) {
            if (series[i].text == arr[2]) {
                series[i].values[0] = parseInt(arr[3], 10);
                break;
            }
            if (series[i].text == "") {
                series[i].text = arr[2];
                series[i].values[0] = parseInt(arr[3], 10);
                break;
            }
        }
        zingchart.render({
          id: 'myChartPie',
          data: chartConfigPie
        });
        zingchart.render({
          id: 'myChartPie1',
          data: chartConfigPie1
        });
    } else if (arr[0] == "eachpopu") {
        var series = chartConfigPie.graphset[1].series;
        if (arr[1] == "huya") {
            series = chartConfigPie1.graphset[1].series;
        }
        for (var i = 0; i < series.length; i++) {
            if (series[i].text == arr[2]) {
                series[i].values[0] = parseInt(arr[3], 10);
                break;
            }
            if (series[i].text == "") {
                series[i].text = arr[2];
                series[i].values[0] = parseInt(arr[3], 10);
                break;
            }
        }
        zingchart.render({
          id: 'myChartPie',
          data: chartConfigPie
        });
        zingchart.render({
          id: 'myChartPie1',
          data: chartConfigPie1
        });
    }
};
