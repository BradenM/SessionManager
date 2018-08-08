import React, { Component } from 'react';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCog, faPlus, faList, faTh } from '@fortawesome/free-solid-svg-icons';

// Font Awesome
library.add(faCog, faPlus, faList, faTh);

export const Icon = (icon, size = '1x', color = 'grey') => (
  <div className={'has-text-' + color}>
    <FontAwesomeIcon icon={icon} size={size} />
  </div>
);
