import React from 'react';
import './App.css';
import FullNavBar from './components/navbar'
import "bootstrap/dist/css/bootstrap.min.css";
import "shards-ui/dist/css/shards.min.css"
import { Container, Row} from "shards-react";
import UploadCard from './components/uploadCard'

function App() {
  return (
    <div>
    <FullNavBar />
    <Container>
      <Row style={{justifyContent: "center", padding: "2%"}}>
        <UploadCard/>
      </Row>
    </Container>
    </div>
  );
}

export default App;
