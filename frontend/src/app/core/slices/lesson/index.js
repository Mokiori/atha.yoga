/* eslint no-param-reassign: 0 */
import { createSlice } from '@reduxjs/toolkit';
import getLessonSlice from './getLesson';

const initialState = {
  lesson: [],
  errorMessage: null,
};

const lessonSlice = createSlice({
  name: 'lesson',
  initialState,
  extraReducers: {
    // [getLessonSlice.pending]: state => {
    //   state.errorMessage = null;
    // },
    [getLessonSlice.fulfilled]: (state, action) => {
      state.lessons = action.payload;
      state.errorMessage = null;
    },
    [getLessonSlice.rejected]: (state, action) => {
      state.lessons = null;
      state.errorMessage = action.payload;
    },
  },
});

export default lessonSlice.reducer;
