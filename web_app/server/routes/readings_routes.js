import readingsService from "../service/readings_service";

const readingsRoutes = function(app) {
  app.route("/api/internal/readings").get(readingsService.fetchAllRecords);
};

export default readingsRoutes;
