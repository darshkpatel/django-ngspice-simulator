import React from 'react';
import {
    Card,
    CardHeader,
    CardTitle,
    CardImg,
    CardBody,
    CardFooter,
    Button
} from "shards-react";
import './css/uploadCard.css';
import { Container, Row, Col } from "shards-react";

class UploadCard extends React.Component {
    render() {
        return (
            <Card className="cardStyle">
                    <CardHeader>Card header</CardHeader>
                    <CardBody className="cardBodyStyle">
                <Container>

                            <CardTitle>Lorem Ipsum</CardTitle>
                        <Row>
                            <p>Lorem ipsum dolor sit amet.</p>
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