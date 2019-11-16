import locationsService from "../service/locations_service";

const locationsRoutes = function(app) {
  app.route("/api/internal/locations").get(locationsService.fetchAllRecords);
};

export default locationsRoutes;
