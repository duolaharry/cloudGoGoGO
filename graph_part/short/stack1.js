let chartConfigStack1 = {
  type: 'bar',
  stacked: true,
  title: {
    text: '人气值最新变动图',
    color: '#5D7D9A',
    adjustLayout: true
  },
  legend: {
    align: 'center',
    layout: 'x3',
    toggleAction: 'remove',
    verticalAlign: 'bottom'
  },
  plot: {
    valueBox: {
      text: '',
      thousandsSeparator: ',',
      rules: [
        {
          rule: '%stack-top == 0',
          visible: false
        }
      ]
    },
    offsetY: '-1px',
    rules: [
      {
        offsetY: '1px',
        rule: '%v <= 0'
      }
    ]
  },
  plotarea: {
    margin: 'dynamic'
  },
  scaleX: {
    labels: ['', '', '', '', '', '', '', '', '', '']
  },
  scaleY: {
    format: '%v',
    guide: {
      items: [
        {
          backgroundColor: '#f5f5f5'
        },
        {
          backgroundColor: '#eeeeee'
        }
      ]
    },
    multiplier: true,
    negation: 'currency',
    refLine: {
      lineColor: '#212121',
      lineWidth: '2px'
    }
    
  },
  tooltip: {
    text: '%v',
    align: 'left',
    borderRadius: '3px',
    decimals: 2,
    fontColor: '#ffffff',
    negation: 'currency'
  },
  series: [
    {
      text: '人气变动值',
      values: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      backgroundColor: '#3290be',
      stack: 1
    }
  ]
};