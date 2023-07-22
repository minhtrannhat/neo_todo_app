import { useContext } from "react";
import { Navigate, useLocation } from "react-router-dom";
import { AuthContext } from "src/AuthContext";

interface IProps {
  children: React.ReactNode;
}

const RequireAuth = ({ children }: IProps) => {
  const { authenticated } = useContext(AuthContext);

  const location = useLocation();

  if (authenticated) {
    return <>{children}</>;
  } else {
    // re-route user back to login page if not logged in
    return <Navigate state={{ from: location }} to="/login/" />;
  }
};

export default RequireAuth;
