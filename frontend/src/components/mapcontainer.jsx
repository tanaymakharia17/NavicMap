import React from 'react';
import Joi from 'joi-browser';

import Map, { GeolocateControl, Layer, Marker, Source } from 'react-map-gl';

import Form from './common/form';

import marker from '../images/marker.png'

import coordinates from '../data/lnmCoordinates.json';

import path from '../service/pathService';

import 'mapbox-gl/dist/mapbox-gl.css';
import '@mapbox/mapbox-gl-geocoder/dist/mapbox-gl-geocoder.css';

class MapComponent extends Form {
    state = {
        data: {
            source: "",
            destination: ""
        },
        viewState: {
            longitude: 75.9235,
            latitude: 26.9363,
            zoom: 16.5
        },
        options: {
            source: new Array(),
            destination: new Array()
        },
        direction: [[]],
        errors: {}
    }

    setViewState(viewState) {
        this.setState({ viewState });
    }

    schema = {
        source: Joi.string().label("Source"),
        destination: Joi.string().label("Destination")
    }

    render() {

        const source = this.state.data.source;
        const destination = this.state.data.destination;
        const direction = this.state.direction;

        const data = {
            type: "Feature",
            properties: {},
            geometry: {
                type: "LineString",
                coordinates: direction
            }
        };

        return (
            <React.Fragment>
                <div id="container">
                    <div id="search">
                        <form className="mt-3 mx-3" onSubmit={this.handleSubmit}>
                            {this.renderInput("source", "Search Starting Point...")}
                            {this.renderInput("destination", "Search Destination...")}
                            {this.renderButton("Get Direction")}
                        </form>
                    </div>

                    <div id="map">
                        <Map
                            {...this.state.viewState}
                            mapboxAccessToken={process.env.REACT_APP_MAPBOX_TOKEN}
                            onMove={vs => this.setViewState(vs.viewState)}
                            style={{ width: '100vw', height: '100vh' }}
                            mapStyle="mapbox://styles/mapbox/streets-v9">

                            {coordinates[source] && coordinates[destination] &&
                                <Source type="geojson" data={data}>
                                    <Layer
                                        id="route"
                                        type="line"
                                        source="route"
                                        layout={{
                                            "line-join": "round",
                                            "line-cap": "round"
                                        }}
                                        paint={{
                                            "line-color": "rgba(3, 170, 238, 0.5)",
                                            "line-width": 5
                                        }} />
                                </Source>}

                            <GeolocateControl
                                position='top-right'
                                positionOptions={{ "enableHighAccuracy": true }}
                                trackUserLocation="true"
                                showUserHeading="true" />

                            {coordinates[source] &&
                                <Marker
                                    longitude={coordinates[source]['longitude']}
                                    latitude={coordinates[source]['latitude']}>
                                    <img src={marker} style={{ width: '25px', height: '25px' }} />
                                </Marker>}

                            {coordinates[destination] &&
                                <Marker
                                    longitude={coordinates[destination]['longitude']}
                                    latitude={coordinates[destination]['latitude']}>
                                    <img src={marker} style={{ width: '25px', height: '25px' }} />
                                </Marker>}

                        </Map >
                    </div>
                </div>
            </React.Fragment>
        );
    }

    doSubmit = async () => {

        const source = this.state.data.source;
        const destination = this.state.data.destination;

        const locations = {
            startX: coordinates[source]['latitude'],
            startY: coordinates[source]['longitude'],
            endX: coordinates[destination]['latitude'],
            endY: coordinates[destination]['longitude']
        }

        const { data } = await path.getDir(locations);
        this.setState({
            direction: data.path
        });
    }
}

export default MapComponent;