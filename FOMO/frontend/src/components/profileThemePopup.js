import React from "react";
import Popup from "reactjs-popup";
import { useSelector, useDispatch } from "react-redux";
import { undo, light, lime, dark, twilight } from "./themeSlice";

export default function ProfileThemeSelect() {
  const dispatch = useDispatch();
  const theme = useSelector((state) => state.theme.value);

  return (
    <Popup
      trigger={
        <button className="panelbutton">
          <img className="panelicon" src="/icons/profileTheme.svg" alt="Icon"></img>
          <p className="paneltext">Change theme</p>
          <p className="panelsubtext">Light mode • Dark mode • Colour theme</p>
        </button>
      }
      modal
      nested
    >
      {(close) => (
        <div className="modal">
          <div className="popuppanel">
            <div className="prompt">
              <div>
                <p>Choose Your Theme</p>
              </div>
              <button
                className="themebutton"
                onClick={() => {
                  console.log("Theme changed");
                  dispatch(light());
                }}
              >
                <div
                  className="themesample"
                  style={{ backgroundColor: "#e7e7e7" }}
                ></div>
                <p className="themesubtext">Light Mode</p>
              </button>
              <button
                className="themebutton"
                onClick={() => {
                  console.log("Theme changed");
                  dispatch(lime());
                }}
              >
                <div
                  className="themesample"
                  style={{ backgroundColor: "#2B9134" }}
                ></div>
                <p className="themesubtext">Light Lime</p>
              </button>
              <button
                className="themebutton"
                onClick={() => {
                  console.log("Theme changed");
                  dispatch(dark());
                }}
              >
                <div
                  className="themesample"
                  style={{ backgroundColor: "#121212" }}
                ></div>
                <p className="themesubtext">Dark Mode</p>
              </button>
              <button
                className="themebutton"
                onClick={() => {
                  console.log("Theme changed");
                  dispatch(twilight());
                }}
              >
                <div
                  className="themesample"
                  style={{ backgroundColor: "#DF8E18" }}
                ></div>
                <p className="themesubtext">Dark Twilight</p>
              </button>
            </div>
            <div className="actions">
              <button
                className="acceptbutton"
                onClick={() => {
                  console.log("modal closed ");
                  localStorage.setItem('theme', theme);
                  close();
                }}
              >
                Save
              </button>
              <button
                className="cancelbutton"
                onClick={() => {
                  console.log("modal closed ");
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
