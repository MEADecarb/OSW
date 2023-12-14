<!DOCTYPE html>
<html>
<head>
    <title>Map Visualization</title>
    <style>
        .legend {
            position: fixed;
            bottom: 50px;
            left: 50px;
            width: 150px;
            height: 90px;
            border: 2px solid grey;
            z-index: 9999;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <!-- Your iframe -->
    <iframe src="MD_OSW_map.html" height="900" width="900"></iframe>

    <!-- Legend -->
    <div class="legend">
        <b>Legend</b> <br>
        Wind Energy <i style="background:#2C557E;opacity:0.7;"></i><br>
        County Boundaries <i style="background:#fdda25;opacity:0.7;"></i><br>
        Other Layer <i style="background:#B7DCDF;opacity:0.7;"></i><br>
    </div>
</body>
</html>
