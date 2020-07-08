import { combineReducers } from "redux";

/**
 * You can import more reducers here
 */


//@BlueprintReduxImportInsertion
import EmailAuth8419Reducer from '../features/EmailAuth8419/redux/reducers';
import CalendarView8418Reducer from '../features/CalendarView8418/redux/reducers';
import CalendarReducer from '../features/Calendar/redux/reducers';
import EmailAuthReducer from '../features/EmailAuth/redux/reducers';

export const combinedReducers = combineReducers({
  blank: (state, action) => {
    if (state == null) state = [];
    return state;
  },


  //@BlueprintReduxCombineInsertion
EmailAuth8419: EmailAuth8419Reducer,
CalendarView8418: CalendarView8418Reducer,
Calendar: CalendarReducer,
EmailAuth: EmailAuthReducer,

});