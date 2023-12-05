import React, {FormEventHandler, useState} from 'react';
import './App.css';
import { Button, Grid, TextField } from "@mui/material";
import { useDispatch } from 'react-redux';

function Form() {
    const dispatch = useDispatch()
    const [item, setItem] = useState<string>("");
    const submit: FormEventHandler = (e) => {
        dispatch({ type: "ADD_TODO", payload: item})
        setItem("");
        e.preventDefault();
    }
  return (
      <Grid container>
          <form onSubmit={submit}>
              <Grid item xs={12}>
                  <TextField label="New item" variant="outlined" value={item} onChange={(e) => setItem(e.target.value)} />
              </Grid>
              <Grid item xs={12}>
                  <Button disabled={!Boolean(item)} type="submit">Add</Button>
              </Grid>
          </form>
      </Grid>
  );
}

export default Form;
