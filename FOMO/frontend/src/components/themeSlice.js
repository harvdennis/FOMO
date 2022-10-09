import { createSlice } from "@reduxjs/toolkit";

export const themeSlice = createSlice({
  name: "theme",
  initialState: {
    value: localStorage.getItem("theme"),
  },
  reducers: {
    undo: (state) => {
      state.value = localStorage.getItem("theme");
    },

    light: (state) => {
      state.value = "light";
    },
    dark: (state) => {
      state.value = "dark";
    },
    lime: (state) => {
      state.value = "lime";
    },
    twilight: (state) => {
      state.value = "twilight";
    },

    // changePicture: (state, action) => {
    //   state.value += action.payload
    // },
  },
});

export const { undo, light, lime, dark, twilight } = themeSlice.actions;

export default themeSlice.reducer;
