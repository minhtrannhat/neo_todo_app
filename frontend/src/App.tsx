import React from "react";
import "./App.css";

// Roboto font and its weights
import "@fontsource/roboto/300.css";
import "@fontsource/roboto/400.css";
import "@fontsource/roboto/500.css";
import "@fontsource/roboto/700.css";

// Theming
import ThemeProvider from "./ThemeProvider";

// Material UI stuffs
import Container from "@mui/material/Container";

function App() {
  return (
    <ThemeProvider>
      <Container maxWidth="md"></Container>
    </ThemeProvider>
  );
}

export default App;
