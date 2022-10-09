import React, { useState, useEffect } from "react";
import Popup from "reactjs-popup";
import { useSelector, useDispatch } from "react-redux";
import { undo, chadwick, kilburn, mecd, uniplace, alang } from "./imageSlice";

import KilburnIMG from "../images/profileKilburn.png";
import MECDIMG from "../images/profileMECD.png";
import ChadwickIMG from "../images/profileChadwick.png";
import AlanGIMG from "../images/profileAlanG.png";
import UniPlaceIMG from "../images/profileUniPlace.png";

export default function ProfilePictureSelect() {
  const dispatch = useDispatch();
  const [userData, setUserData] = useState({});
  const image = useSelector((state) => state.image.value);

  const getDetails = async () => {
    try {
      const res = await fetch("/api/jsonUserDetails/");
      const data = await res.json();
      setUserData(data);
    } catch (err) {
      console.log("Error:", err);
    }
  };

  useEffect(() => {
    getDetails();

    //Have a fetch call to check if the user ics exists
  }, []);

  return (
    <Popup
      trigger={
        <button className="panelbutton">
          <img className="panelicon" src="/icons/profileProfile.svg"></img>
          <p className="paneltext">Profile name and picture</p>
          <p className="panelsubtext">
            Change display name • Change profile picture
          </p>
        </button>
      }
      modal
      nested
    >
      {(close) => (
        <div className="modal">
          <div className="popuppanel">
            <div className="contenthead">
              <p>Profile Picture</p>

              <ul className="selection">
                <li>
                  <img
                    className="profilepictureselect"
                    src={KilburnIMG}
                    onClick={() => dispatch(kilburn())}
                  ></img>
                </li>

                <li>
                  <img
                    className="profilepictureselect"
                    src={MECDIMG}
                    onClick={() => dispatch(mecd())}
                  ></img>
                </li>
                <li>
                  <img
                    className="profilepictureselect"
                    src={ChadwickIMG}
                    onClick={() => dispatch(chadwick())}
                  ></img>
                </li>
                <li>
                  <img
                    className="profilepictureselect"
                    src={AlanGIMG}
                    onClick={() => dispatch(alang())}
                  ></img>
                </li>
                <li>
                  <img
                    className="profilepictureselect"
                    src={UniPlaceIMG}
                    onClick={() => dispatch(uniplace())}
                  ></img>
                </li>
              </ul>
            </div>
            <div className="content">
              <p>Full Name</p>
              <p className="popupdata">{userData.fullname}</p>
            </div>
            <div className="content">
              <p>Username</p>
              <p className="popupdata">{userData.username}</p>
            </div>
            <div className="actions">
              <button
                className="acceptbutton"
                onClick={() => {
                  console.log("Changes saved ");
                  localStorage.setItem("image", image);
                  close();
                }}
              >
                Save
              </button>
              <button
                className="cancelbutton"
                onClick={() => {
                  console.log("Popup closed ");
                  dispatch(undo());
                  close();
                }}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>
      )}
    </Popup>
  );
}
