import { all, takeEvery, take } from "redux-saga/effects";


//@BlueprintReduxSagaImportInsertion
import EmailAuth8419Saga from '../features/EmailAuth8419/redux/sagas';
import CalendarView8418Saga from '../features/CalendarView8418/redux/sagas';
import CalendarSaga from '../features/Calendar/redux/sagas';
import EmailAuthSaga from '../features/EmailAuth/redux/sagas';

function* helloSaga() {
  console.log("Hello from saga!");
}

export function* mainSaga() {
  yield all([
    takeEvery("TEST/ALO", helloSaga),
    // other sagas go here


    //@BlueprintReduxSagaMainInsertion
EmailAuth8419Saga,
CalendarView8418Saga,
CalendarSaga,
EmailAuthSaga,
    
  ]);
}