import readingsRoutes from "./readings_routes";
import locationsRoutes from "./locations_routes";

const routes = function(app) {
  console.debug("Readings routes registering....");
  readingsRoutes(app);
  console.debug("Readings routes registered");

  console.debug("locations routes registering....");
  locationsRoutes(app);
  console.debug("locations routes registered");
};

export default routes;
