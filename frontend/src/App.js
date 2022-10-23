import React from 'react';
import './App.css';

import MapComponent from './components/mapcontainer';

class App extends React.Component {
	state = {}

	render() {

		return (
			<React.Fragment>
				<MapComponent />
			</React.Fragment>
		);
	}
}

export default App;
