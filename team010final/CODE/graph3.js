// const width = 200;
// const height = 100;
// const margin = { top: 20, right: 10, bottom: 30, left: 70 }
			
var svg3 = d3.select("#graph3")
			.append("svg")
	        .attr("width", width + margin.left + margin.right)
	        .attr("height", height + margin.top + margin.bottom)
	        .append("g")
	        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var foo3={}
var recoveries = []
d3.json("data.json").then(function(d){
			
		for (var country of Object.keys(d)) {
			date_obj = d[country]
    		for (var dat of Object.keys(date_obj)) {
    			if (!foo3.hasOwnProperty(dat)) {
      				var tmp_obj = {
        				'recoveries': 0
        			}
        			foo3[dat] = tmp_obj
      			}
     			foo3[dat]['recoveries'] += date_obj[dat]['recoveries']
    		}
		}
console.log(foo3)
		for (var dat of Object.keys(foo3)) {
			var recoveries_obj = {
		      date: d3.timeParse("%m/%d/%y")(dat),
		      count: foo3[dat]['recoveries']
		    } 
		    recoveries.push(recoveries_obj)
		}
	
        console.log(recoveries)
var data = recoveries
    
    var x = d3.scaleTime()
        .domain(d3.extent(data, function (d) { return d.date; }))
        .range([0, width]);

    svg3.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x).tickFormat(d3.timeFormat("%b")));

    var y = d3.scaleLinear()
        .domain([0, d3.max(data, function (d) { return +d.count; })])
        .range([height, 0]);


    svg3.append("g")
        .call(d3.axisLeft(y).tickFormat(d3.format(".2s")).ticks(4));

    svg3.append("path")
      .datum(data)
      .attr("fill", "green")
      .attr("fill-opacity", .3)
      .attr("stroke", "none")
      .attr("d", d3.area()
        .x(function(d) { return x(d.date) })
        .y0( height )
        .y1(function(d) { return y(d.count) })
        )
    svg3.append("text")
       .attr("x", ((width-margin.right-margin.left)/1.8))             
      .attr("y", 2)
      .attr("text-anchor", "middle")  
      .style("font-size", "15px")
      .attr("fill", "white")  
        .text("Recoveries")

	svg3.append("path")
        .datum(data)
        .attr("stroke", "green")
        .attr("fill", "none")
        .attr("stroke-width", 1)
        .attr("d", d3.line()
        .x(function (d) { return x(d.date) })
        .y(function (d) { return y(d.count) })
        )
        })
