import { createSlice } from "@reduxjs/toolkit";

export const imageSlice = createSlice({
  name: "image",
  initialState: {
    value: localStorage.getItem("image"),
  },
  reducers: {
    undo: (state) => {
      state.value = localStorage.getItem("image");
    },

    kilburn: (state) => {
      state.value = "./profileKilburn.png";
    },
    mecd: (state) => {
      state.value = "./profileMECD.png";
    },
    chadwick: (state) => {
      state.value = "./profileChadwick.png";
    },
    alang: (state) => {
      state.value = "./profileAlanG.png";
    },
    uniplace: (state) => {
      state.value = "./profileUniPlace.png";
    },
    changePicture: (state, action) => {
      state.value += action.payload;
    },
  },
});

export const { undo, kilburn, mecd, chadwick, alang, uniplace } =
  imageSlice.actions;

export default imageSlice.reducer;
