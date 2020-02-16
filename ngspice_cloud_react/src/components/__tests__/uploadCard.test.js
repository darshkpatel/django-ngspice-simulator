
// Auto-generated do not edit


/* eslint-disable import/no-extraneous-dependencies */
/* eslint-disable no-undef */
import React from 'react';
import renderer from 'react-test-renderer';
import uploadCard from '../uploadCard';


describe('uploadCard test', () => {
  it('uploadCard should match snapshot', () => {
    const component = renderer.create(<uploadCard
       />);
    const tree = component.toJSON();
    expect(tree).toMatchSnapshot();
  });
});
