import React from 'react';
import {
    Card,
    CardHeader,
    CardBody,
} from "shards-react";
import './css/uploadCard.css';
import { Container, Row } from "shards-react";
import UploadBox from "./uploadBox.js"

class UploadCard extends React.Component {
    render() {
        return (
            <Card className="cardStyle">
                <CardHeader>Upload Netlist for Circuit</CardHeader>
                <CardBody className="uploadCardBodyStyle1">
                    <Container>

                        <Row>
                        </Row>
                        <UploadBox updateMainState={this.props.updateMainState}/>
                        <Row>

                        </Row>
                    </Container>
                </CardBody>
            </Card>

        );




    }
}

export default UploadCard;