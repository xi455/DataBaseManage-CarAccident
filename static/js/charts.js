var endpoint = '/chart/api/chart/data/';
var defaultData = [];
var labels = [];
$.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
        labels = data.labels
        defaultData = data.default
        labels1 = data.labels1
        defaultData1 = data.default1
        labels2 = data.labels2
        defaultData2 = data.default2
        labels3 = data.labels3
        defaultData3 = data.default3
        defaultData4 = data.default4
        defaultData5 = data.default5
        defaultData6 = data.default6
        defaultData7 = data.default7
        defaultData8 = data.default8
        setChart()
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})

function setChart(){
    
    var ctx = document.getElementById("myChart");
    var ctx2 = document.getElementById("myChart2");
    var ctx3 = document.getElementById("myChart3");
    var ctx4 = document.getElementById("myChart4");
    var ctx5 = document.getElementById("myChart5");
    var ctx6 = document.getElementById("myChart6");
    var ctx7 = document.getElementById("myChart7");

//顏色
var colors = [
    'rgba(255, 99, 132, 0.2)',
    'rgba(54, 162, 235, 0.2)',
    'rgba(255, 206, 86, 0.2)',
    'rgba(75, 192, 192, 0.2)',
    'rgba(153, 102, 255, 0.2)',
    'rgba(255, 159, 64, 0.2)'
];
//線條顏色
var borderColorVariants = [
    'rgba(255, 99, 132, 1)',
    'rgba(54, 162, 235, 1)',
    'rgba(255, 206, 86, 1)',
    'rgba(75, 192, 192, 1)',
    'rgba(153, 102, 255, 1)',
    'rgba(255, 159, 64, 1)'
];

// 各月份車禍事件數量

var datasets = [];
Object.keys(defaultData4).forEach(function(year, index) {
    var colorIndex = index % colors.length;
    var dataset = {
        label: '車禍事件數量 (' + year + ')',
        data: defaultData4[year],
        backgroundColor: colors[colorIndex],
        borderColor: borderColorVariants[colorIndex],
        borderWidth: 1,
        fill: false // 确保线条不填充颜色
    };
    datasets.push(dataset);
});

//是否肇事逃逸
var datasets1 = [];
    var labels = Object.keys(defaultData6); // The years will be used as labels

    // Separate data for "是" and "否"
    var dataYes = [];
    var dataNo = [];

    labels.forEach(function(year) {
        dataYes.push(defaultData6[year]["是"] || 0); // Use 0 if no data for "是"
        dataNo.push(defaultData6[year]["否"] || 0); // Use 0 if no data for "否"
    });
    // Create the datasets for "是"
    datasets1.push({
        label: '是否肇事逃逸(是)',
        data: dataYes,
        backgroundColor: colors[0], // Use the first color for "是"
        borderColor: borderColorVariants[0],
        borderWidth: 1,
        type: 'line',
        fill: false,
        yAxisID: 'y-axis-yes'
    });

    // Create the datasets for "否"
    datasets1.push({
        label: '是否肇事逃逸(否)',
        data: dataNo,
        backgroundColor: colors[2], // Use the second color for "否"
        borderColor: borderColorVariants[2],
        borderWidth: 1
    });
var ctx6 = document.getElementById("myChart6");
    var myChart = new Chart(ctx6, {
        type: 'bar',
        data: {
            labels: labels1,
            datasets: datasets1
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                },
                yAxes: [
                    {
                        id: 'y-axis-no',
                        type: 'linear',
                        position: 'left',
                        ticks: {
                            beginAtZero: true
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '是否肇事逃逸(是)'
                        }
                    },
                    {
                        id: 'y-axis-yes',
                        type: 'linear',
                        position: 'right',
                        ticks: {
                            beginAtZero: true
                        },
                        grid: {
                            drawOnChartArea: false // This will remove the grid lines for the secondary y-axis
                        },
                        scaleLabel: {
                            display: true,
                            labelString: '是否肇事逃逸(是)'
                        }
                    }
                ]
                }
            }
    });

//各年度每個月的車禍統計
var ctx2 = document.getElementById("myChart2");
    var myChart = new Chart(ctx2, {
        type: 'line',
        data: {
            labels: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
            datasets: datasets
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
        }
    });

// 各年度車禍事件統計數量
var myChart1 = new Chart(ctx, {
      type: 'pie',
        data: {
            labels: labels1,
            datasets: [{
                label: '車禍數量',
                data: defaultData1,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
    });

// A1,A2車禍事件數量
var myChart2 = new Chart(ctx3, {
        type: 'pie',
  
          data: {
              labels: labels2,
              datasets: [{
                  label: '車禍事件數量',
                  data: defaultData2,
                  backgroundColor: [
                      'rgba(255, 206, 86, 0.2)',
                      'rgba(255, 159, 64, 0.2)'
                  ],
                  borderColor: [
                      'rgba(255, 206, 86, 1)',
                      'rgba(255, 159, 64, 1)'
                  ],
                  borderWidth: 1
              }]
          }
      });     

// 各縣市發生車禍事件數量
var myChart4 = new Chart(ctx4, {
        type: 'bar',
  
        data: {
              labels: labels3,
              datasets: [{
                  label: '車禍事件數量',
                  data: defaultData3,
                  backgroundColor:'rgba(54, 162, 235, 0.2)',
                  borderColor:'rgba(54, 162, 235, 1)',
                  borderWidth: 1
              }]
          },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
      });    
      

//各縣市道路類型車禍
let d5 = [];
      for(let i = 0; i < defaultData5.length; i++){
        let rowData = defaultData5[i][0].split(':');
        let city = rowData[0];
        let roadType = rowData[1].split('-')[0];
        let roadValue = parseInt(rowData[1].split('-')[1])
        let roadData = {};
        roadData[roadType] = roadValue;
        for(let j = 0; j <= d5.length; j++) {
            if(j < d5.length) {
                if(d5[j].city == city){
                    d5[j].data[roadType] = roadValue;
                    break;
                }    
            }else {
                d5.push({index:d5.length , city:city, data:roadData});
                break;
            }
        }
      }
      console.log(d5);
      var myChart5 = new Chart(ctx5, {
        type: 'horizontalBar',
        data: {
            labels: Object.keys(d5[0].data),
            datasets: [{
                label: '車禍事件數量',
                data: Object.values(d5[0].data),
                backgroundColor: colors.slice(0, Object.values(d5[0].data).length),
                borderColor: borderColorVariants.slice(0, Object.values(d5[0].data).length),
                borderWidth: 1,
                fill: false,
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            scales: {
                x:{
                    beginAtZero: true
                }
            }
        }
    });

    const selectElement = document.getElementById('chart_5_select');
      // 根據 d5 的鍵生成下拉選單選項
      d5.forEach(obj => {
        const option = document.createElement('option');
        option.value = obj.index;
        option.textContent = obj.city;
        selectElement.appendChild(option);
    });

    // 當選擇改變時重新繪製圖表
    selectElement.addEventListener('change', function() {
        const selectedKey = this.value;
        const selectedData = Object.values(d5[selectedKey].data);
        const selectedLabels = Object.keys(d5[selectedKey].data);

        // 更新圖表數據
        myChart5.data.datasets[0].labels = selectedLabels;
        myChart5.data.datasets[0].data = selectedData;
        myChart5.update();
    });

    // 初始化下拉選單並觸發一次更改事件以顯示初始圖表
    selectElement.value = Object.keys(d5)[0];
    selectElement.dispatchEvent(new Event('change'));

//各縣市肇因
let data7 = [];
    for(let i = 0; i < defaultData7.length; i++){
        let rowData = defaultData7[i][0].split(':');
        let city = rowData[0];
        let roadType = rowData[1].split('-')[0];
        let roadValue = parseInt(rowData[1].split('-')[1]);
        let roadData = {};
        roadData[roadType] = roadValue;
        let cityFound = false;
        for(let j = 0; j < data7.length; j++) {
            if(data7[j].city === city){
                data7[j].data[roadType] = roadValue;
                cityFound = true;
                break;
            }
        }
        if (!cityFound) {
            data7.push({index: data7.length, city: city, data: roadData});
        }
    }

    console.log(data7);
    var myChart7 = new Chart(ctx7, {
        type: 'doughnut',
        data: {
            labels: Object.keys(data7[0].data).slice(0, 5),
            datasets: [{
                axis: 'y',
                label: '車禍事件數量',
                data: Object.values(data7[0].data).slice(0, 5),
                backgroundColor: colors.slice(0, Object.values(data7[0].data).length).slice(0, 5),
                borderColor: borderColorVariants.slice(0, Object.values(data7[0].data).length).slice(0, 5),
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y', 
            responsive: true,
            scales: {
                x: {
                    beginAtZero: true
                }
            }
        }
    });

    const selectElement7 = document.getElementById('chart_7_select');

    data7.forEach(obj => {
        const option = document.createElement('option');
        option.value = obj.index;
        option.textContent = obj.city;
        selectElement7.appendChild(option);
    });

    // 當選擇改變時重新繪製圖表
    selectElement7.addEventListener('change', function() {
        const selectedKey = this.value;
        const selectedData = Object.values(data7[selectedKey].data).slice(0, 5);
        const selectedLabels = Object.keys(data7[selectedKey].data).slice(0, 5);

        // 更新圖表數據
        myChart7.data.labels = selectedLabels;
        myChart7.data.datasets[0].data = selectedData;
        myChart7.update();
    });

    // 初始化下拉選單並觸發一次更改事件以顯示初始圖表
    selectElement7.value = 0;
    selectElement7.dispatchEvent(new Event('change'));


    const a1Data = defaultData8.filter(item => item[0].startsWith("A1")).map(item => {
        const parts = item[0].split(" - ");
        return {
            label: parts[0].split(": ")[1],
            value: parseInt(parts[1])
        };
    });
    
    const a2Data = defaultData8.filter(item => item[0].startsWith("A2")).map(item => {
        const parts = item[0].split(" - ");
        return {
            label: parts[0].split(": ")[1],
            value: parseInt(parts[1])
        };
    });
    
    // 合并A1和A2的数据
    const combinedData = a1Data.map((item, index) => {
        return {
            label: item.label,
            a1Value: item.value,
            a2Value: a2Data[index].value
        };
    });
    


    // 创建第一个饼图 (A1)
var ctx8 = document.getElementById('myChart8').getContext('2d');
var myChart8 = new Chart(ctx8, {
    type: 'doughnut',
    data: {
        labels: a1Data.map(item => item.label),
        datasets: [{
            data: a1Data.map(item => item.value),
            backgroundColor: colors,
            borderColor: borderColorVariants,
        }]
    },
    options: {
        title: {
            display: true,
            text: '造成死亡車禍事件的保護裝置統計'
        },
        legend: {
            position: 'left'
        }
    }
});

// 创建第二个饼图 (A2)
var ctx9 = document.getElementById('myChart9').getContext('2d');
var myChart9 = new Chart(ctx9, {
    type: 'doughnut',
    data: {
        labels: a2Data.map(item => item.label),
        datasets: [{
            data: a2Data.map(item => item.value),
            backgroundColor: colors,
            borderColor: borderColorVariants,
        }]
    },
    options: {
        title: {
            display: true,
            text: '沒有造成死亡車禍事件的保護裝置統計'
        },
        legend: {
            position: 'left'
        }
    }
});
}
// var ctx = document.getElementById("myChart");