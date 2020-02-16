
// Auto-generated do not edit


/* eslint-disable import/no-extraneous-dependencies */
/* eslint-disable no-undef */
import React from 'react';
import renderer from 'react-test-renderer';
import navbar from '../navbar';


describe('navbar test', () => {
  it('navbar should match snapshot', () => {
    const component = renderer.create(<navbar
       />);
    const tree = component.toJSON();
    expect(tree).toMatchSnapshot();
  });
});
