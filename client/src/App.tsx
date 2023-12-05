import './App.css';
import List from "./List";
import Counter from "./Counter";
import Form from "./Form";
import {Container, Grid} from "@mui/material";

function App() {
  return (
      <Container maxWidth="sm">
        <Grid container spacing={2} className="App">
             <Grid item xs={12}>
                <Counter/>
             </Grid>
            <Grid item xs={12}>
                <List/>
            </Grid>
            <Grid item xs={12}>
                <Form/>
            </Grid>
        </Grid>
      </Container>
  );
}

export default App;
