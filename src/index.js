import Globe from 'globe.gl';
import * as d3 from 'd3';

async function request(url) {
    try {
        const res = await fetch(url);
        const data = await res.json();
        return data;
    } catch (e) {
        throw e;
    }
}

async function getCoordinates() {
    try {
        const { latitude, longitude } = await request('https://geolocation-db.com/json/');
        return {latitude, longitude,};
    } catch (e) {
        throw e;
    }
}

function getDailyNumber(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

// Globe container
const globeContainer = document.getElementById('globeViz');
const colorScale = d3.scaleSequentialPow(d3.interpolate("#2354a3", "red")).exponent(1 / 3);
const getVal = (feat) => {
    return feat.covidData.confirmed / feat.properties.POP_EST;
};

let world;
let flagName;
const flagEndpoint = 'https://corona.lmao.ninja/assets/img/flags';

init();

function init() {
    // country layout on the 3D globe
    world = Globe()(globeContainer)
        .backgroundColor('rgba(0, 0, 0, 0)')
        .showGraticules(false)
        .polygonAltitude(0.06)
        .polygonCapColor((feat) => colorScale(getVal(feat)))
        .polygonSideColor(() => 'rgba(0, 100, 0, 0.05)')
        .polygonStrokeColor(() => '#111')
        .polygonLabel(({ properties: d, covidData: c }) => {
            if (d.ADMIN === 'France') {flagName = 'fr';}
            else if (d.ADMIN === 'Norway') {flagName = 'no';}
            else {flagName = d.ISO_A2.toLowerCase();}
            // return each country's flag and data
            return `
            <div class="card">
                <img class="card-img" src="${flagEndpoint}/${flagName}.png" alt="flag" />
                <div class="container">
                    <span class="card-title"><b>${d.NAME}</b></span> <br />
                    <div class="card-spacer"></div>
                    <hr>
                    <div class="card-spacer"></div>
                    <span>Cases: ${getDailyNumber(c.confirmed)}</span>  <br />
                    <span>Deaths: ${getDailyNumber(c.deaths)}</span> <br />
                    <span>Recovered: ${getDailyNumber(c.recoveries)}</span> <br />
                    <span>Population: ${d3.format('.3s')(d.POP_EST)}</span>
               </div>
            </div>`;
        })
        .onPolygonHover((hoverD) =>
            world
                .polygonAltitude((d) => (d === hoverD ? 0.12 : 0.06))
                .polygonCapColor((d) =>
                    d === hoverD ? 'steelblue' : colorScale(getVal(d))
                )
        )
        .polygonsTransitionDuration(200);
    getCases();
}

let dates = [];
let countries = [];
let featureCollection = [];

// Play button, slider, and slider date
const playButton = document.querySelector('.play-button');
const slider = document.querySelector('.slider');
const sliderDate = document.querySelector('.slider-date');

const geojson_link = "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson"
async function getCases() {
    countries = await request("./data.json");
    featureCollection = (await request(geojson_link)).features;
    document.querySelector('.title-desc').innerHTML = '';
    dates = Object.keys(countries.China);

    // Set slider values
    slider.max = dates.length - 1;
    slider.value = dates.length - 1;
    slider.disabled = false;
    playButton.disabled = false;

    updateCounters();
    updatePolygonsData();
    try {
        const { latitude, longitude } = await getCoordinates();
        world.pointOfView(
            {lat: latitude, lng: longitude,},
            1000
        );
    } catch (e) {
        console.log('Failure');
    }
}

const confirmedEl = document.querySelector('#confirmed');
const deathsEl = document.querySelector('#deaths');
const recoveriesEl = document.querySelector('#recovered');

function updateCounters() {
    sliderDate.innerHTML = dates[slider.value];
    let totalConfirmed = 0;
    let totalDeaths = 0;
    let totalRecoveries = 0;

    Object.keys(countries).forEach((item) => {
        if (countries[item][dates[slider.value]]) {
            const countryDate = countries[item][dates[slider.value]];
            totalConfirmed += +countryDate.confirmed;
            totalDeaths += +countryDate.deaths;
            totalRecoveries += countryDate.recoveries ? +countryDate.recoveries : 0;
        }
    });

    confirmedEl.innerHTML = totalConfirmed.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    deathsEl.innerHTML = totalDeaths.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    recoveriesEl.innerHTML = totalRecoveries.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

function updatePolygonsData() {
    for (let x = 0; x < featureCollection.length; x++) {
        const country = featureCollection[x].properties.NAME;
        if (countries[country]) {
            featureCollection[x].covidData = {
                confirmed: countries[country][dates[slider.value]].confirmed,
                deaths: countries[country][dates[slider.value]].deaths,
                recoveries: countries[country][dates[slider.value]].recoveries,
            };
        } else {
            featureCollection[x].covidData = {
                confirmed: 0,
                deaths: 0,
                recoveries: 0,
            };
        }
    }

    const maxVal = Math.max(...featureCollection.map(getVal));
    colorScale.domain([0, maxVal]);
    world.polygonsData(featureCollection);
}

let interval;

playButton.addEventListener('click', () => {
    if (playButton.innerText === 'Play') {
        playButton.innerText = 'Pause';
    } else {
        playButton.innerText = 'Play';
        clearInterval(interval);
        return;
    }

    // Check if slider position is max
    if (+slider.value === dates.length - 1) {
        slider.value = 0;
    }

    sliderDate.innerHTML = dates[slider.value];

    interval = setInterval(() => {
        slider.value++;
        sliderDate.innerHTML = dates[slider.value];
        updateCounters();
        updatePolygonsData();
        if (+slider.value === dates.length - 1) {
            playButton.innerHTML = 'Play';
            clearInterval(interval);
        }
    }, 200);
});

if ('oninput' in slider) {
    slider.addEventListener(
        'input',
        function () {
            updateCounters();
            updatePolygonsData();
        },
        false
    );
}

window.addEventListener('resize', (event) => {
    world.width([event.target.innerWidth]);
    world.height([event.target.innerHeight]);
});