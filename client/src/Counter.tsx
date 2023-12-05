import './App.css';
import { useSelector } from 'react-redux';
import { RootState } from './store';

function Counter() {
    const items = useSelector((state: RootState) => state.todos.items)
  return (
      <div>
          There are {items.length} in the list.
      </div>
  );
}

export default Counter;
