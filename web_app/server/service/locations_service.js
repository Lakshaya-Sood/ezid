import locationsApi from "../api/locations_api";

const locationsService = {
  fetchAllRecords: (req, res) => {
    locationsApi
      .fetchAllRecords()
      .then(locationsList => {
        res.status(200).json({ locationsList: locationsList }); //Success
      })
      .catch(err => {
        console.log(err);
        res.status(500).json({ err: err }); //Internal Server Error
      });
  }
};

export default locationsService;
