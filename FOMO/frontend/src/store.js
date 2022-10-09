import { configureStore } from '@reduxjs/toolkit'
import imageReducer from './components/imageSlice'
import themeReducer from './components/themeSlice'

export default configureStore({
  reducer: {
      image: imageReducer,
      theme: themeReducer,
  },
})
