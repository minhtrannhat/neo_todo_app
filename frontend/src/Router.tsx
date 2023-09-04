import { BrowserRouter, Route, Routes } from "react-router-dom";

import ScrollToTop from "./components/ScrollToTop";
import TopBar from "./components/TopBar";
import Register from "./pages/Register";

const Router = () => (
  <BrowserRouter>
    <ScrollToTop />
    <TopBar />
    <Routes>
      <Route path="/register/" element={<Register />} />
    </Routes>
  </BrowserRouter>
);

export default Router;
