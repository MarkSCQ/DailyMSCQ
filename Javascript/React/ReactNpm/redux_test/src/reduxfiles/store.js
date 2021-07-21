import { createStore } from "redux";

import counterReducer from './counter_reducer'


export default createStore(counterReducer)