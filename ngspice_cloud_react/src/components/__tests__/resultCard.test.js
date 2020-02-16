
// Auto-generated do not edit


/* eslint-disable import/no-extraneous-dependencies */
/* eslint-disable no-undef */
import React from 'react';
import renderer from 'react-test-renderer';
import resultCard from '../resultCard';


describe('resultCard test', () => {
  it('resultCard should match snapshot', () => {
    const component = renderer.create(<resultCard
       />);
    const tree = component.toJSON();
    expect(tree).toMatchSnapshot();
  });
});
