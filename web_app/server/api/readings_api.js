import readingsModel from "../db/readings_model";

const readingsApi = {
  fetchAllRecords: function(filters) {
    return new Promise((resolve, reject) => {
      readingsModel.find(filters).exec((err, readingsList) => {
        if (err) {
          reject(err);
        } else {
          resolve(readingsList);
        }
      });
    });
  }
};

export default readingsApi;
