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
            y: data.y1,
            type: 'scatter',
        };
        var my_plot2 = {
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



