import React from 'react';
import {
    Card,
    CardHeader,
    CardBody,
} from "shards-react";
import './css/resultCard.css';
import { Container, Row } from "shards-react";

class ResultCard extends React.Component {
    constructor(props){
        super(props);
        this.state = {pollResult:{'state':'UNFETCHED', 'details':[]}}
    }
    componentDidMount() {
        this.timer = setInterval(()=> this.getItems(), 5000);
      }
      
      componentWillUnmount() {
        this.timer = null; // here...
      }
      
      getItems() {
        fetch('http://localhost:8000/api/celery/'+this.props.jobDetails.fileID)
          .then(result =>result.json())
          .then(result => this.setState({ pollResult: result }))
      }

    render() {
        console.log('result card: ',this.props.jobDetails)
        console.log('Poll Result State: ',this.state)

        let status = 'Waiting to Fetch'
        
        switch(this.state.pollResult.state){
            case 'UNFETCHED': status = 'Waiting to Fetch'; break;
            case 'SUCCESS': status = (this.state.pollResult.details[0]==null)?'Error Processing File':'Completed Processing';clearInterval(this.timer);break;
            case 'PENDING': status = 'Processing Pending'; break;
            default: status = 'Error Occured';clearInterval(this.timer); console.log('state:', this.state.pollResult);break;
        }
        return (
            <Card className="cardStyle">
    <CardHeader>Results for <strong>{this.props.jobDetails.fileName}</strong> </CardHeader>
                <CardBody className="cardBodyStyle">
                    <Container>
                        <Row>
<h5>Status:</h5><strong>{status}</strong>
{this.state.pollResult.details[0]!=null &&
    <div>
    <h5>Output</h5>
    <p>{JSON.stringify(this.state.pollResult.details[0])}</p>
    </div>
}
{   this.state.pollResult.details.length!=0 &&
    <div>
    <h5>Graphs</h5>
    {this.state.pollResult.details[1].map(path=>(<img key={path} src={path}/>))}
    </div>
}
                        </Row>
                    </Container>
                </CardBody>
            </Card>

        );
    }
}

export default ResultCard;