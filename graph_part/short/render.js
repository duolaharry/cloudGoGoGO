var ws = new WebSocket("ws://192.168.1.106/ws/");

ws.onopen = function(event) {
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
        id: 'myChartStack',
        data: chartConfigStack,
        height: '100%',
        width: '100%',
    });
    zingchart.render({
        id: 'myChartStack1',
        data: chartConfigStack1,
        height: '100%',
        width: '100%',
    });
    zingchart.render({
        id: 'myChartStack2',
        data: chartConfigStack2,
        height: '100%',
        width: '100%',
    });
}

ws.onmessage = function(event) {
    command = event.data;
    arr = command.split(' ');

    if (arr[0] == "allpeople") {
        var max_val = 0;
        var values = chartConfigLine.series[0].values;
        var labels_x = chartConfigLine.scaleX.labels;
        for (var i = 0; i < values.length - 1; i++) {
            values[i] = values[i + 1];
            labels_x[i] = labels_x[i + 1];
            if (values[i] > max_val) {
                max_val = values[i];
            }
        }
        values[values.length - 1] = parseInt(arr[2], 10);
        if (arr[2] > max_val) {
            max_val = parseInt(arr[2], 10);
        }
        labels_x[labels_x.length - 1] = arr[4];
        
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
        var max_val = 0;
        var values = chartConfigLine1.series[0].values;
        var labels_x = chartConfigLine1.scaleX.labels;
        for (var i = 0; i < values.length - 1; i++) {
            values[i] = values[i + 1];
            labels_x[i] = labels_x[i + 1];
            if (values[i] > max_val) {
                max_val = values[i];
            }
        }
        values[values.length - 1] = parseInt(arr[2], 10);
        if (arr[2] > max_val) {
            max_val = parseInt(arr[2], 10);
        }
        labels_x[labels_x.length - 1] = arr[4];
        
        max_val = parseInt(max_val * 1.1, 10);
        var step = parseInt(max_val / 5, 10);
        chartConfigLine1.scaleY.values = "0:" + max_val.toString() + ":" + step.toString();

        zingchart.render({
            id: 'myChartLine1',
            data: chartConfigLine1,
            height: '100%',
            width: '100%'
        });
    } else if (arr[0] == "allmean") {
        var max_val = 0;
        var values = chartConfigLine2.series[0].values;
        var labels_x = chartConfigLine2.scaleX.labels;
        for (var i = 0; i < values.length - 1; i++) {
            values[i] = values[i + 1];
            labels_x[i] = labels_x[i + 1];
            if (values[i] > max_val) {
                max_val = values[i];
            }
        }
        values[values.length - 1] = parseInt(arr[1], 10);
        if (arr[1] > max_val) {
            max_val = parseInt(arr[1], 10);
        }
        labels_x[labels_x.length - 1] = arr[3];
        
        max_val = parseInt(max_val * 1.1, 10);
        var step = parseInt(max_val / 5, 10);
        chartConfigLine2.scaleY.values = "0:" + max_val.toString() + ":" + step.toString();

        zingchart.render({
            id: 'myChartLine2',
            data: chartConfigLine2,
            height: '100%',
            width: '100%'
        });
    } else if (arr[0] == "clear") {
        for (var i = 0; i < 10; i++) {
            chartConfigStack.scaleX[i] = '';
            chartConfigStack.series[0].values[i] = 0;
            chartConfigStack1.scaleX[i] = '';
            chartConfigStack1.series[0].values[i] = 0;
        }
        chartConfigStack2.series[0].values = [];
        chartConfigStack2.scaleX.labels = [];
        zingchart.render({
            id: 'myChartStack',
            data: chartConfigStack,
            height: '100%',
            width: '100%',
        });
        zingchart.render({
            id: 'myChartStack1',
            data: chartConfigStack1,
            height: '100%',
            width: '100%',
        });
        zingchart.render({
            id: 'myChartStack2',
            data: chartConfigStack2,
            height: '100%',
            width: '100%',
        });
    } else if (arr[0] == "peoplechange") {
        for (var i = 0; i < 10; i++) {
            if (chartConfigStack.scaleX.labels[i] == '') {
                chartConfigStack.scaleX.labels[i] = arr[1];
                chartConfigStack.series[0].values[i] = parseInt(arr[2], 10);
                break;
            }
        }
        zingchart.render({
            id: 'myChartStack',
            data: chartConfigStack,
            height: '100%',
            width: '100%',
        });
    } else if (arr[0] == "popuchange") {
        for (var i = 0; i < 10; i++) {
            if (chartConfigStack1.scaleX.labels[i] == '') {
                chartConfigStack1.scaleX.labels[i] = arr[1];
                chartConfigStack1.series[0].values[i] = parseInt(arr[2], 10);
                break;
            }
        }
        zingchart.render({
            id: 'myChartStack1',
            data: chartConfigStack1,
            height: '100%',
            width: '100%',
        });
    } else if (arr[0] == "namemean") {
        chartConfigStack2.series[0].values.push(parseInt(arr[2], 10));
        chartConfigStack2.scaleX.labels.push(arr[1]);
        zingchart.render({
            id: 'myChartStack2',
            data: chartConfigStack2,
            height: '100%',
            width: '100%',
        });
    }
}
