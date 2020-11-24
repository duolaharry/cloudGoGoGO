let chartConfigLine1 = {
    type: 'line',
    globals: {
      fontSize: '14px'
    },
    title: {
      text: '斗鱼直播总数人气变化对比图',
      color: '#5D7D9A',

      _padding: '30 0 0 35',
      fontSize: '30px'
    },
    subtitle: {
    	text: '',
      color: '#5D7D9A',
      fontSize: '16px',
      fontWeight: 300,
      padding: '15px 0 0 40px'
    },
    _legend: {
      cursor: 'hand',
      draggable: true
    },
    legend: {
      cursor: 'hand',
      draggable: true,
      highlightPlot: true,
      item: {
        fontColor: '#373a3c',
        fontSize: '12px'
      },
      toggleAction: 'remove',
      borderRadius: '5px',
      header: {
        text: '图例',
        color: '#5D7D9A',
        padding: '10px'
      }
    },
    // plot represents general series, or plots, styling
    plot: {
      // hoverstate
      // animation docs here:
      // https://www.zingchart.com/docs/tutorials/design-and-styling/chart-animation/#animation__effect
      lineWidth: '3px',
      // line node styling
      marker: {
        borderWidth: '0px',
        size: '6px'
      }
    },
    plotarea: {
      margin: '85px'
    },
    scaleX: {
      // set scale label
      _markers: [
        {
          type: 'line',
          range: [35],
          lineColor: '#a3aeb8',
          lineWidth: '2px',
      		valueRange: true,
        }
      ],
      label: {
        text: '时间'
      },
      // convert text on scale indices
      values: '0:10:1',
      labels: [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    },
    scaleY: {
      // scale label with unicode character
      label: {
        text: '直播人气值'
      },
      values: '0:100:20'
    },
    crosshairX: {
      plotLabel: {
        _padding: '10px 15px',
        borderRadius: '3px',
        color: '#5D7D9A',
        padding: '10px',
        backgroundColor: '#fff',
        thousandsSeparator: ',',
      }
    },
    series: [
      {
        text: '斗鱼直播人气',
        // plot values
        values: [0,0,0,0,0,0,0,0,0,0,0],
        lineColor: '#3290be',
        marker: {
          backgroundColor: '#3290be'
        }
      }
    ]
};
