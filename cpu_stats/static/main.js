//var ctx = document.getElementById('myChart').getContext('2d');
//
//var graphData = {
//    type: 'circe',
//    data: {
//        labels: ['Время'],
//        datasets: [{
//            label: '# of Votes',
//            data: [],
//            backgroundColor: [
//                'rgba(73, 198, 230, 0.5)',
//            ],
//            borderWidth: 1
//        }]
//    },
//    options: {}
//}

//var myChart = new Chart(ctx, graphData);
//const socket =  new WebSocket('ws://localhost:8000/ws-url/');
//
//    socket.onmessage = function(event){
//        var djData = JSON.parse(event.data);
//        console.log(graphData);
//        var newGraphData = graphData.data.datasets[0].data;
//        newGraphData.shift();
//        newGraphData.push(djData.message);
//        graphData.data.datasets[0].data = newGraphData;
//        myChart.update();
//    }




// вариант вывода цифр



//    socket.onmessage = function(event){
//            var data = JSON.parse(event.data);
//            console.log(data);
//            document.querySelector('#app').innerText = data.message;
//
//        }

// вариант с графиком номер 2

ws = new WebSocket('ws://localhost:8000/ws-url/')
    var request_data_interval
    ws.onopen = function()
    {
        // Web Socket is connected, send data using send()
        ws.send("Message to send");

        request_data_interval = window.setInterval(requestData, 50);

    };

    ws.onmessage = function (evt)
    {
        var received_msg = evt.data;

        data = JSON.parse(evt.data);
        var my_plot1 = {
//            x: data.x,
            y: data.y1,
            type: 'scatter',
        };
        var my_plot2 = {
//            x: data.x,
            y: data.y2,
            type: 'scatter',
        };
        Plotly.newPlot('avg-graph', [my_plot1]);
        Plotly.newPlot('cpu-graph', [my_plot2]);
    };

    ws.onclose = function()
    {
      // websocket is closed.
      window.clearInterval(request_data_interval)
    };

    function requestData()
    {
        ws.send("get-data");
    }



