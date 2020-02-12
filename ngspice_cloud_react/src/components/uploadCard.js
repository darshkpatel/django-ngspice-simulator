import React from 'react';
import {
    Card,
    CardHeader,
    CardTitle,
    CardBody,
    Button
} from "shards-react";
import './css/uploadCard.css';
import { Container, Row } from "shards-react";
import UploadBox from "./uploadBox.js"
import MyUploader from "./uploadBoxNew"
class UploadCard extends React.Component {
    render() {
        return (
            <Card className="cardStyle">
                <CardHeader>Upload Netlist for Circuit</CardHeader>
                <CardBody className="cardBodyStyle">
                    <Container>

                        <Row>
                        </Row>
                        {/* {UploadBox()} */}
                        {/* <UploadBox /> */}
                        <MyUploader />
                        <Row>

                        </Row>
                    </Container>
                </CardBody>
            </Card>

        );




    }
}

export default UploadCard;