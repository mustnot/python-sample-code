chart_script = """
<script src="../js/chart.js"></script>
    <style>
    canvas {{
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select: none;
    }}
    </style>
<style type="text/css">/* Chart.js */
@keyframes chartjs-render-animation{{from{{opacity:.99}}to{{opacity:1}}}}.chartjs-render-monitor{{animation:chartjs-render-animation 1ms}}.chartjs-size-monitor,.chartjs-size-monitor-expand,.chartjs-size-monitor-shrink{{position:absolute;direction:ltr;left:0;top:0;right:0;bottom:0;overflow:hidden;pointer-events:none;visibility:hidden;z-index:-1}}.chartjs-size-monitor-expand>div{{position:absolute;width:1000000px;height:1000000px;left:0;top:0}}.chartjs-size-monitor-shrink>div{{position:absolute;width:200%;height:200%;left:0;top:0}}</style></head>

<body>
    <div id="container" style="width: 1000px;"><div class="chartjs-size-monitor"><div class="chartjs-size-monitor-expand"><div class=""></div></div><div class="chartjs-size-monitor-shrink"><div class=""></div></div></div>
        <canvas id="canvas" style="display: block; width: 699px; height: 349px;" width="699" height="349" class="chartjs-render-monitor"></canvas>
    </div>

    <script>
        Chart.elements.Rectangle.prototype.draw = function() {{
    
            var ctx = this._chart.ctx;
            var vm = this._view;
            var left, right, top, bottom, signX, signY, borderSkipped, radius;
            var borderWidth = vm.borderWidth;
            // Set Radius Here
            // If radius is large enough to cause drawing errors a max radius is imposed
            var cornerRadius = 20;
        
            if (!vm.horizontal) {{
                // bar
                left = vm.x - vm.width / 2;
                right = vm.x + vm.width / 2;
                top = vm.y;
                bottom = vm.base;
                signX = 1;
                signY = bottom > top? 1: -1;
                borderSkipped = vm.borderSkipped || 'bottom';
            }} else {{
                // horizontal bar
                left = vm.base;
                right = vm.x;
                top = vm.y - vm.height / 2;
                bottom = vm.y + vm.height / 2;
                signX = right > left? 1: -1;
                signY = 1;
                borderSkipped = vm.borderSkipped || 'left';
            }}
        
            // Canvas doesn't allow us to stroke inside the width so we can
            // adjust the sizes to fit if we're setting a stroke on the line
            if (borderWidth) {{
                // borderWidth shold be less than bar width and bar height.
                var barSize = Math.min(Math.abs(left - right), Math.abs(top - bottom));
                borderWidth = borderWidth > barSize? barSize: borderWidth;
                var halfStroke = borderWidth / 2;
                // Adjust borderWidth when bar top position is near vm.base(zero).
                var borderLeft = left + (borderSkipped !== 'left'? halfStroke * signX: 0);
                var borderRight = right + (borderSkipped !== 'right'? -halfStroke * signX: 0);
                var borderTop = top + (borderSkipped !== 'top'? halfStroke * signY: 0);
                var borderBottom = bottom + (borderSkipped !== 'bottom'? -halfStroke * signY: 0);
                // not become a vertical line?
                if (borderLeft !== borderRight) {{
                    top = borderTop;
                    bottom = borderBottom;
                }}
                // not become a horizontal line?
                if (borderTop !== borderBottom) {{
                    left = borderLeft;
                    right = borderRight;
                }}
            }}
        
            ctx.beginPath();
            ctx.fillStyle = vm.backgroundColor;
            ctx.strokeStyle = vm.borderColor;
            ctx.lineWidth = borderWidth;
        
            // Corner points, from bottom-left to bottom-right clockwise
            // | 1 2 |
            // | 0 3 |
            var corners = [
                [left, bottom],
                [left, top],
                [right, top],
                [right, bottom]
            ];
        
            // Find first (starting) corner with fallback to 'bottom'
            var borders = ['bottom', 'left', 'top', 'right'];
            var startCorner = borders.indexOf(borderSkipped, 0);
            if (startCorner === -1) {{
                startCorner = 0;
            }}
        
            function cornerAt(index) {{
                return corners[(startCorner + index) % 4];
            }}
        
            // Draw rectangle from 'startCorner'
            var corner = cornerAt(0);
            ctx.moveTo(corner[0], corner[1]);
        
            for (var i = 1; i < 4; i++) {{
                corner = cornerAt(i);
                nextCornerId = i+1;
                if(nextCornerId == 4){{
                    nextCornerId = 0
                }}
        
                nextCorner = cornerAt(nextCornerId);
        
                width = corners[2][0] - corners[1][0];
                height = corners[0][1] - corners[1][1];
                x = corners[1][0];
                y = corners[1][1];
                
                var radius = cornerRadius;
                
                // Fix radius being too large
                if(radius > height/2){{
                    radius = height/2;
                }}if(radius > width/2){{
                    radius = width/2;
                }}
        
                ctx.moveTo(x + radius, y);
                ctx.lineTo(x + width - radius, y);
                ctx.quadraticCurveTo(x + width, y, x + width, y + radius);
                ctx.lineTo(x + width, y + height - radius);
                ctx.quadraticCurveTo(x + width, y + height, x + width - radius, y + height);
                ctx.lineTo(x + radius, y + height);
                ctx.quadraticCurveTo(x, y + height, x, y + height - radius);
                ctx.lineTo(x, y + radius);
                ctx.quadraticCurveTo(x, y, x + radius, y);
        
            }}
        
            ctx.fill();
            if (borderWidth) {{
                ctx.stroke();
            }}
        }}; 

        var color = Chart.helpers.color;
        var barChartData = {{
            labels: {labels},
            datasets: [{{
                label: 'Label1',
                backgroundColor: '#355b94',
                //barThickness: 10,
                barPercentage: 0.3,
                maxBarThickness: 10,
                
                data: {label1_data},
            }}, {{
                label: 'Label2',
                backgroundColor: '#edc382',
                //barThickness: 10,
                barPercentage: 0.3,
                maxBarThickness: 10,
                data: {label2_data}
            }}],
        }};
        

        window.onload = function() {{
            var ctx = document.getElementById('canvas').getContext('2d');
            window.myBar = new Chart(ctx, {{
                type: 'bar',
                data: barChartData,
                options: {{
                    animation: false,
                    responsive: true,

                    legend: {{
                        position: 'top',
                        align: 'end',
                        labels:{{
                            boxWidth: 10
                        }}
                    }},
                    title: {{
                        display: true,
                        text: 'sample bar chart',
                        fontSize: 14
                    }},
                    
                    scales: {{
                        xAxes: [{{
                            gridLines: {{
                                display: true,
                                drawBorder: true,
                                drawOnChartArea: false,
                            }},
                        }}],
                        yAxes: [{{
                            gridLines: {{
                                display: true,
                                drawBorder: true,
                                drawOnChartArea: false,
                            }},
                        }}]
                    }}
                }}
            }});
        }};
    </script>"""