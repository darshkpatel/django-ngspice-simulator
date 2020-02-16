
// Auto-generated do not edit


/* eslint-disable import/no-extraneous-dependencies */
/* eslint-disable no-undef */
import React from 'react';
import renderer from 'react-test-renderer';
import uploadBox from '../uploadBox';


describe('uploadBox test', () => {
  it('uploadBox should match snapshot', () => {
    const component = renderer.create(<uploadBox
       />);
    const tree = component.toJSON();
    expect(tree).toMatchSnapshot();
  });
});
