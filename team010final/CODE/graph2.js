// const width = 200;
// const height = 100;
// const margin = { top: 20, right: 10, bottom: 30, left: 70 }
			
var svg2 = d3.select("#graph2")
			.append("svg")
	        .attr("width", width + margin.left + margin.right)
	        .attr("height", height + margin.top + margin.bottom)
	        .append("g")
	        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var foo2={}
var deaths = []
d3.json("data.json").then(function(d){
			
		for (var country of Object.keys(d)) {
			date_obj = d[country]
    		for (var dat of Object.keys(date_obj)) {
    			if (!foo2.hasOwnProperty(dat)) {
      				var tmp_obj = {
        				'deaths': 0
        			}
        			foo2[dat] = tmp_obj
      			}
     			foo2[dat]['deaths'] += date_obj[dat]['deaths']
    		}
		}

		for (var dat of Object.keys(foo2)) {
			var deaths_obj = {
		      date: d3.timeParse("%m/%d/%y")(dat),
		      count: foo2[dat]['deaths']
		    } 
		    deaths.push(deaths_obj)
		}
	
var data = deaths

console.log(data)
    
    var x = d3.scaleTime()
        .domain(d3.extent(data, function (d) { return d.date; }))
        .range([0, width]);

    svg2.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x).tickFormat(d3.timeFormat("%b")));

    var y = d3.scaleLinear()
        .domain([0, d3.max(data, function (d) { return +d.count; })])
        .range([height, 0]);


    svg2.append("g")
        .call(d3.axisLeft(y).tickFormat(d3.format(".2s")).ticks(5));

    svg2.append("path")
      .datum(data)
      .attr("fill", "yellow")
      .attr("fill-opacity", .3)
      .attr("stroke", "none")
      .attr("d", d3.area()
        .x(function(d) { return x(d.date) })
        .y0( height )
        .y1(function(d) { return y(d.count) })
        )

    svg2.append("text")
       .attr("x", ((width-margin.right-margin.left)/1.8))             
      .attr("y", 2)
      .attr("text-anchor", "middle")  
      .style("font-size", "15px")
      .attr("fill", "white")  
      .text("Deaths")

	svg2.append("path")
        .datum(data)
        .attr("stroke", "yellow")
        .attr("fill", "none")
        .attr("stroke-width", 1)
        .attr("d", d3.line()
        .x(function (d) { return x(d.date) })
        .y(function (d) { return y(d.count) })
        )
        })
