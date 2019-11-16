import locationsModel from "../db/locations_model";

const locationsApi = {
  fetchAllRecords: function() {
    return new Promise((resolve, reject) => {
      locationsModel.find({}).exec((err, locationsList) => {
        if (err) {
          reject(err);
        } else {
          resolve(locationsList);
        }
      });
    });
  }
};

export default locationsApi;
