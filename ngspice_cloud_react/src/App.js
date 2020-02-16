import React, { Component } from 'react';
import './App.css';
import FullNavBar from './components/navbar'
import "bootstrap/dist/css/bootstrap.min.css";
import "shards-ui/dist/css/shards.min.css"
import { Container, Row } from "shards-react";
import UploadCard from './components/uploadCard'
import ResultCard from './components/resultCard'
import SimpleStorage from "react-simple-storage";




class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      showResultCard: false,
      files: []
    }
    this.updateMainState = this.updateMainState.bind(this);
  }

  updateMainState = (state) => {
     console.log('Setting State:', state); 
     this.setState(state)
    //  localStorage.setItem('files', JSON.stringify(state.files)) 
    }


  render() {
    console.log("Current main state", this.state)
    const resultCards = this.state.files.map(file => (
      <div style={{ padding: "2%" }}>
      <ResultCard jobDetails={file} key={file.fileName}/>
      </div>
    ));


    return (
      <div>

        <FullNavBar />
        <Container>
          <Row style={{ justifyContent: "center", padding: "2%" }}>
            <UploadCard updateMainState={this.updateMainState} />
          </Row>
          <Row style={{ justifyContent: "center", padding: "2%" }}>
            <SimpleStorage parent={this} />
            {
              this.state.showResultCard &&
              resultCards
            }
          </Row>

        </Container>

      </div>
    );
  }
}
export default App;
