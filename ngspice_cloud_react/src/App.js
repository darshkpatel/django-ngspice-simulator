import React, { Component } from 'react';
import './App.css';
import FullNavBar from './components/navbar'
import "bootstrap/dist/css/bootstrap.min.css";
import "shards-ui/dist/css/shards.min.css"
import { Container, Row } from "shards-react";
import UploadCard from './components/uploadCard'




class App extends Component {
  constructor(props) {
    super(props)
    this.state = {showResultCard: false}
    this.updateMainState = this.updateMainState.bind(this);
  }

  updateMainState = (state) => {console.log('Setting State:', state);this.setState(state)}


  render() {
    return (
      <div>
        <FullNavBar />
        <Container>
          <Row style={{ justifyContent: "center", padding: "2%" }}>
            <UploadCard updateMainState={this.updateMainState} />
          </Row>
        </Container>
        <div>{
        this.state.showResultCard &&
        "HELLO WORLD!"}</div>

      </div>
    );
  }
}
export default App;
