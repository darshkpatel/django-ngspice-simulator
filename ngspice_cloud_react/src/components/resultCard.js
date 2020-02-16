import React from 'react';
import {
    Card,
    CardHeader,
    CardBody,
} from "shards-react";
import './css/resultCard.css';
import { Collapse, Container, Row, Button } from "shards-react";
import SimpleStorage from "react-simple-storage";

class ResultCard extends React.Component {
    constructor(props) {
        super(props);
        this.toggle = this.toggle.bind(this);

        this.state = { collapse: false, pollResult: { 'state': 'UNFETCHED', 'details': [] } }
    }
    toggle() {
        this.setState({ collapse: !this.state.collapse });
    }
    componentDidMount() {
        this.timer = setInterval(() => this.getItems(), 5000);
    }

    componentWillUnmount() {
        this.timer = null; // here...
    }

    getItems() {
        fetch('http://localhost:8000/api/celery/' + this.props.jobDetails.fileID)
            .then(result => result.json())
            .then(result => this.setState({ pollResult: result }))
    }
    _handleDelete(id){
        this.props._handleDelete(id);
    }
    render() {
        console.log('result card: ', this.props.jobDetails)
        console.log('Poll Result State: ', this.state)

        let status = 'Waiting to Fetch'

        switch (this.state.pollResult.state) {
            case 'UNFETCHED': status = 'Waiting to Fetch'; break;
            case 'SUCCESS': status = (this.state.pollResult.details[0] == null) ? 'Error Processing File' : 'Completed Processing'; clearInterval(this.timer); break;
            case 'PENDING': status = 'Processing Pending'; break;
            default: status = 'Error Occured'; clearInterval(this.timer); console.log('state:', this.state.pollResult); break;
        }
        return (
            <Card className="cardStyle" >
                <SimpleStorage parent={this} prefix={this.props.jobDetails.fileID} />

                <CardHeader>
                    <span>Results for <strong>{this.props.jobDetails.fileName}</strong></span>
                    <button type="button" className="close" aria-label="Close" onClick={this._handleDelete.bind(this, this.props.jobDetails.fileID)}>
                        <span aria-hidden="true">&times;</span>
                    </button>
                </CardHeader>
                <CardBody className="cardBodyStyle">
                    <Container>
                        <Row style={{ justifyContent: "space-between", flexDirection: 'row', alignItems: 'stretch' }}>
                            <h5>Status:</h5><strong>{status}</strong> {'\u00A0'}{'\u00A0'}
                            {this.state.pollResult.state === 'SUCCESS' &&
                                <Button outline size='sm' onClick={this.toggle} >Show Output</Button>
                            }
                        </Row>
                        <Row>
                            <Collapse open={this.state.collapse}>
                                {this.state.pollResult.details[0] != null &&
                                    <div>
                                        <h5>Output</h5>
                                        <p>{JSON.stringify(this.state.pollResult.details[0])}</p>
                                    </div>
                                }
                                {typeof this.state.pollResult.details[1] != "undefined"  
                                        && this.state.pollResult.details[1] != null  
                                        && this.state.pollResult.details[1].length != null  
                                        && this.state.pollResult.details[1].length > 0 &&
                                    <div>
                                        <h5>Graphs</h5>
                                        {this.state.pollResult.details[1].map(path => (<img key={path} src={path} alt="Graph Plot" />))}
                                    </div>
                                }
                            </Collapse>
                        </Row>
                    </Container>
                </CardBody>
            </Card>

        );
    }
}

export default ResultCard;