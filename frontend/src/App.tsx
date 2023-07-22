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

// React helmet async: configure the page's title
import { Helmet, HelmetProvider } from "react-helmet-async";

// Authentication Context: Check if user is logged in or not
import { AuthContextProvider } from "./AuthContext";

// React router
import Router from "./Router";

function App() {
  return (
    <AuthContextProvider>
      <HelmetProvider>
        <Helmet>
          <title>Todo</title>
        </Helmet>
        <ThemeProvider>
          <Container maxWidth="md">
            <Router />
          </Container>
        </ThemeProvider>
      </HelmetProvider>
    </AuthContextProvider>
  );
}

export default App;
