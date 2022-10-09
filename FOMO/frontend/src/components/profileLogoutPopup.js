import React from 'react';
import Popup from 'reactjs-popup';

export default function LogoutPrompt() {

  return (
    <Popup trigger={<button className="panelbutton">
      <img className='panelicon' src='/icons/profilePower.svg' alt='Signout'></img>
      <p className='paneltext'>Sign out</p>
      <p className='panelsubtext'>Sign out from FOMO</p>
    </button>}
      modal
      nested
    >

      {close => (
        <div className="modal">
          <div className='popuppanel'>
            <div className="prompt">
              <div>
                <p>Are you sure?</p>
              </div>
            </div>
            <div className="actions">
              <button
                className="acceptbutton"
                onClick={() => {
                  window.location.href = '/api/logout/'
                }}
              >
                Yes
              </button>
              <button
                className="cancelbutton"
                onClick={() => {
                  console.log('modal closed ');
                  close();
                }}
              >
                No
              </button>
            </div>
          </div>
        </div>
      )}
    </Popup>
  )
};
