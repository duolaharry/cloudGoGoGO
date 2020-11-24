var ws = new WebSocket("ws://127.0.0.1/ws/");

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