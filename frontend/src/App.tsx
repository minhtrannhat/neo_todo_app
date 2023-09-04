import React from "react";
import "./App.css";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

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

const queryClient = new QueryClient();

const App = () => {
  return (
    <QueryClientProvider client={queryClient}>
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
    </QueryClientProvider>
  );
};

export default App;
