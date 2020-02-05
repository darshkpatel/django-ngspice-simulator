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

class UploadCard extends React.Component {
    render() {
        return (
            <Card className="cardStyle">
                <CardHeader>Card header</CardHeader>
                <CardBody className="cardBodyStyle">
                    <Container>

                        <CardTitle>Upload Netlist for Circuit</CardTitle>
                        <Row>
                            <p>Upload Multiple files to process</p>
                        </Row>

                        <Row>
                            <Button>Read more &rarr;</Button>
                        </Row>
                    </Container>
                </CardBody>
            </Card>

        );




    }
}

export default UploadCard;