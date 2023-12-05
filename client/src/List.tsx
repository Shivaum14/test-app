import './App.css';
import {IconButton, ListItem, ListItemText, Paper} from "@mui/material";
import MUIList from '@mui/material/List';
import DeleteIcon from '@mui/icons-material/Delete';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from './store';

function List() {
  const dispatch = useDispatch()
  const items = useSelector((state: RootState) => state.todos.items)
  const onDelete = (item: string) => {
    dispatch({ type: "DELETE_TODO", payload: item })
  }
  return (
      <Paper>
          <MUIList>
              {items.map(item =>
                <ListItem
                    key={item}
                    secondaryAction={
                    <IconButton onClick={() => onDelete(item)}>
                      <DeleteIcon />
                    </IconButton>
                  }
                >
                  <ListItemText
                    primary={item}
                  />
                </ListItem>,
              )}
            </MUIList>
      </Paper>
  );
}

export default List;
