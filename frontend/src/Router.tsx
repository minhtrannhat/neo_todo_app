import { BrowserRouter, Route, Routes } from "react-router-dom";

import ScrollToTop from "./components/ScrollToTop";
import TopBar from "./components/TopBar";
import Register from "./pages/Register";
import ConfirmEmail from "./pages/ConfirmEmail";
import Login from "./pages/Login";
import RequireAuth from "./components/RequireAuth";
import ChangePassword from "./pages/ChangePassword";
import ForgottenPassword from "./pages/ForgottenPassword";
import ResetPassword from "./pages/ResetPassword";

const Router = () => (
  <BrowserRouter>
    <ScrollToTop />
    <TopBar />
    <Routes>
      <Route path="/register/" element={<Register />} />
      <Route path="/confirm-email/:token/" element={<ConfirmEmail />} />
      <Route path="/login/" element={<Login />} />
      <Route
        path="/change-password/"
        element={
          <RequireAuth>
            <ChangePassword />
          </RequireAuth>
        }
      />
      <Route path="/forgotten-password/" element={<ForgottenPassword />} />
      <Route path="/reset-password/:token/" element={<ResetPassword />} />
    </Routes>
  </BrowserRouter>
);

export default Router;
