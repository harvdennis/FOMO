import React, {useMemo} from 'react'
import "./Modal.css";
import {Compdynamic}  from './Compdynamic';

export const Modal = (props) => {
  return (
   <div className= "modalBackground">
      <div className="modalContainer">
        <div className="titleCloseBtn">
          <button
            onClick={() => {
              props.setOpenModal(false);
            }}
          >
            X
          </button>
        </div>
        <div className="title">
          <h1>Review Course {props.courseName}</h1>
        </div>
        <div className="body">
          <Compdynamic/>
         
        </div>
        <div className="footer">
          <button
            onClick={() => {
                props.setOpenModal(false);
            }}
            id="cancelBtn"
          >
            Cancel
          </button>
          <button>Save</button>
        </div>
      </div>
  </div>
  );
}

