import readingsApi from "../api/readings_api";

const readingsService = {
  fetchAllRecords: (req, res) => {
    readingsApi
      .fetchAllRecords()
      .then(readingsList => {
        res.status(200).json({ readingsList: readingsList }); //Success
      })
      .catch(err => {
        console.log(err);
        res.status(500).json({ err: err }); //Internal Server Error
      });
  }
};

export default readingsService;
