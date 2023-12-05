import { AnyAction, configureStore } from "@reduxjs/toolkit";
import { createLogger } from "redux-logger";

const logger = createLogger();


interface TodosState {
	items: string[];
}

const initialState: TodosState = {
	items: []
}

export function todoReducer(
	state = initialState,
	action: AnyAction
) {
	switch (action.type) {
		case "ADD_TODO":
			return {
				...state,
				items: [
					...state.items,
					action.payload,
				]
			};
		case "DELETE_TODO":
			return {
				...state,
				items: state.items.filter(i => i !== action.payload)
			};
		default:
			return state;
	}
}

const reducer = {
	todos: todoReducer,
}


const store = configureStore({
	reducer,
	middleware: [logger]
})

export default store;

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch
