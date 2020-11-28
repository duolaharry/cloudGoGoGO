let chartConfigBar1 = {
  type: 'bar3d',
  '3dAspect': {
    depth: 30,
    true3d: 0,
    yAngle: 10
  },
  backgroundColor: '#fff',
  title: {
    text: '直 播 人 气',
    fontWeight: 'normal',
    height: '40px',
    textColor: '#ffffff'
  },
  legend: {
    backgroundColor: 'none',
    borderColor: 'none',
    item: {
      fontColor: '#333'
    },
    layout: 'float',
    shadow: false,
    width: '90%',
    x: '37%',
    y: '10%'
  },
  plotarea: {
    margin: '95px 35px 50px 70px',
    alpha: 0.3,
    backgroundColor: '#fff'
  },
  scaleX: {
    values: ['总人气'],
    alpha: 0.5,
    backgroundColor: '#fff',
    borderColor: '#333',
    borderWidth: '1px',
    guide: {
      visible: false
    },
    item: {
      fontColor: '#333',
      fontSize: '11px'
    },
    tick: {
      alpha: 0.2,
      lineColor: '#333'
    }
  },
  scaleY: {
    alpha: 0.5,
    backgroundColor: '#fff',
    borderColor: '#333',
    borderWidth: '1px',
    format: '%v',
    guide: {
      alpha: 0.2,
      lineColor: '#333',
      lineStyle: 'solid'
    },
    item: {
      paddingRight: '6px',
      fontColor: '#333'
    },
    tick: {
      alpha: 0.2,
      lineColor: '#333'
    }
  },
  series: [
    {
      text: 'huya',
      values: [0],
      tooltip: {
        text: '%v',
        padding: '6px 12px',
        backgroundColor: '#03A9F4',
        borderColor: 'none',
        borderRadius: '5px',
        fontSize: '12px',
        shadow: false
      },
      backgroundColor: '#03A9F4 #4FC3F7',
      borderColor: '#03A9F4',
      legendMarker: {
        borderColor: '#03A9F4'
      }
    },
    {
      text: 'douyu',
      values: [0],
      tooltip: {
        text: '%v',
        padding: '6px 12px',
        backgroundColor: '#673AB7',
        borderColor: 'none',
        borderRadius: '5px',
        fontSize: '12px',
        shadow: false
      },
      backgroundColor: '#673AB7 #9575CD',
      borderColor: '#673AB7',
      legendMarker: {
        borderColor: '#673AB7'
      }
    }
  ]
};