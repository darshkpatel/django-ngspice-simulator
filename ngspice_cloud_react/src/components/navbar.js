import React from "react";
import "./css/navbar.css"
import {
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  Collapse
} from "shards-react";

class FullNavBar extends React.Component {
  constructor(props) {
    super(props);

    this.toggleNavbar = this.toggleNavbar.bind(this);

    this.state = {
      collapseOpen: false
    };
  }


  toggleNavbar() {
    this.setState({
      ...this.state,
      ...{
        collapseOpen: !this.state.collapseOpen
      }
    });
  }

  render() {
    return (
      <Navbar type="dark" theme="primary" expand="md">
        <NavbarBrand href="#">ngSpice Cloud</NavbarBrand>
        <NavbarToggler onClick={this.toggleNavbar} />

        <Collapse open={this.state.collapseOpen} navbar>
          <Nav navbar>



          </Nav>


        </Collapse>
      </Navbar>
    );
  }
}

export default FullNavBar;